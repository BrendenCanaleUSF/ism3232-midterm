"""Business rules module for rental calculations and pricing logic."""

from typing import Any

DELIVERY_FEE: float = 35.00
WAIVER_LIMIT: float = 500.00
DEPOSIT_THRESHOLD: float = 1000.00
INSPECTION_DAYS_LIMIT: int = 7
INSPECTION_QUOTE_LIMIT: float = 800.00


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Calculate base rental cost w/o discounts"""
    return daily_rate * days


def format_rental_cost(daily_rate: float, days: int) -> float:
    """for when calculate_rental_cost is refernced by tests"""
    return calculate_rental_cost(daily_rate, days)


def get_rental_discount(days: int, contractor: bool) -> float:
    """determining discount rate"""
    if not contractor:
        return 0.0
    if days >= 4:
        return 0.10
    return 0.05


def calculate_quote(daily_rate: float, days: int, contractor: bool) -> float:
    """calculate total including discount and delivery fee"""
    base_cost = calculate_rental_cost(daily_rate, days)
    discount_rate = get_rental_discount(days, contractor)
    discounted_cost = base_cost * (1.0 - discount_rate)

    if discounted_cost <= WAIVER_LIMIT:
        return discounted_cost
    return discounted_cost + DELIVERY_FEE


def requires_deposit(quote: float) -> bool:
    """Determine is security deposit is required"""
    return quote > DEPOSIT_THRESHOLD


def needs_inspection(days: int, quote: float) -> bool:
    """Determine if inspection is required"""
    return days > INSPECTION_DAYS_LIMIT or quote > INSPECTION_QUOTE_LIMIT


def total_quoted(rentals: list[dict[str, Any]]) -> float:
    """Calculate the sum of all rental quotes in the list"""
    total = 0.0
    for rental in rentals:
        rate = rental.get("daily_rate", 0.0)
        days = rental.get("days", 0)
        contractor = rental.get("contractor", False)
        total += calculate_quote(rate, days, contractor)
    return total


def largest_rental(rentals: list[dict[str, Any]]) -> str:
    """Find the highest quote"""
    if not rentals:
        return ""

    highest_customer = ""
    highest_quote = -1.0

    for rental in rentals:
        customer = rental.get("customer")
        rate = rental.get("daily_rate", 0.0)
        days = rental.get("days", 0)
        contractor = rental.get("contractor", False)
        quote = calculate_quote(rate, days, contractor)

        if quote > highest_quote:
            highest_quote = quote
            highest_customer = customer

    return highest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Format a single rental record line for reporting"""
    deposit_str = "yes" if deposit else "no"
    inspection_str = "yes" if inspection else "no"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_str} | inspection: {inspection_str}"
