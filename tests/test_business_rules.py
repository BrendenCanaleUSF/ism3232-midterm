from business_rules import (calculate_quote, calculate_rental_cost, format_rental_cost, format_rental_line, get_rental_discount, largest_rental, needs_inspection, requires_deposit, total_quoted )

def test_calculate_rental_cost_standard() -> None:
    """Test calculate_rental_cost calculates correctly"""
    assert calculate_rental_cost(50.0, 3) == 150.0

def test_calculate_rental_cost_zero_days() -> None:
    """Test variable returns zero cost at zero days"""
    assert calculate_rental_cost(100.0, 0) == 0

def test_get_rental_discount_non_contractor() -> None:
    """Test variable returns 0.0 for non contractors"""
    assert get_rental_discount(5, contractor=False) == 0

def test_get_rental_discount_contractor_below_limit() -> None:
    """Test variable for contractor under 3 days"""
    assert get_rental_discount(2, contractor=True) == 0.05

def test_get_rental_discount_contractor_at_limit() -> None:
    """Tests variable at exactly 3 day limit"""
    assert get_rental_discount(3, contractor=True) == 0.05

def test_get_rental_discount_contractor_above_limit() -> None:
    """Test variable for contractor above 3 days"""
    assert get_rental_discount(4, contractor=True) == 0.10

def test_calculate_quote_below_waiver_limit() -> None:
    """Test variable when discounted cost is below waiver threshold"""
    assert calculate_quote(100.0, 4, contractor=False) == 400.0

def test_calculate_quote_at_waiver_limit() -> None:
    """Test variable when discounted cost is exactly at waiver threshold"""
    assert calculate_quote(125.0, 4, contractor=False) == 500.0

def test_calculate_quote_above_waiver_limit() -> None:
    """Test variable when discounted cost is over waiver amount"""
    assert calculate_quote(100.0, 6, contractor=False) == 635.0

def test_requires_deposit_below_limit() -> None:
    """Test variable reutnrs False when quote is below deposit amount"""
    assert requires_deposit(999.99) is False 

def test_requires_deposit_at_limit() -> None:
    """Test variable returns False when quote is at deposit amount"""
    assert requires_deposit(1000.00) is False

def test_requires_deposit_above_limit() -> None:
    """Test variable returns False when quote exceeds deposit amount"""
    assert requires_deposit(1000.01) is True

def test_needs_inspection_days_at_limit() -> None:
    """Test variable returns false when days are at limit of 7"""
    assert needs_inspection(7, 500.0) is False

def test_needs_inspection_days_above_limit() -> None:
    """Test variable returns true when days exceed limit of 7"""
    assert needs_inspection(8, 500.0) is True

def test_needs_inspection_quote_at_limit() -> None:
    """Test variable returns false when quote is at the limit 800 with low number of days"""
    assert needs_inspection(5, 800.0) is False

def test_needs_inspection_quote_above_limit() -> None:
    """Test variable returns True when quote exceeds the limit 800"""
    assert needs_inspection(5, 800.01) is True

def test_contractor_flag_changes_answer() -> None:
    """Tests that contractor=True changes calculated quote"""
    rate, days = 100.0, 4
    quote_regular = calculate_quote(rate, days, contractor=False)
    quote_contractor = calculate_quote(rate, days, contractor=True)
    assert quote_regular != quote_contractor

def test_total_quoted_custom_list() -> None:
    """Test total_quoted correctly adds quotes for the custome rental list"""
    rentals = [
        {"customer": "Alice", "daily_rate": 50.0, "days": 2, "contractor": False},
        {"customer": "Bob", "daily_rate": 200.0, "days": 5, "contractor": False}
    ]
    assert round(total_quoted(rentals), 2) == 1135.0

def test_largest_rental_custom_list() -> None:
    """Tets largest_rental correctly identifies the customer with highest quote"""
    rentals = [
        {"customer": "Alice", "daily_rate": 50.0, "days": 2, "contractor": False},
        {"customer": "Bob", "daily_rate": 200.0, "days": 5, "contractor": False}
    ]
    assert largest_rental(rentals) == "Bob"

def test_largest_rental_tie() -> None:
    """Test largest_rental returns first customer in case of tie"""
    rentals = [
        {"customer": "First", "daily_rate": 100.0, "days": 2, "contractor": False},
        {"customer": "Second", "daily_rate": 100.0, "days": 2, "contractor": False}
    ]
    assert largest_rental(rentals) == "First"

def test_largest_rental_empty() -> None:
    """Test largest_rental returns an empty string when given empty list"""
    assert largest_rental([]) == ""

def test_format_rental_line() -> None:
    """Test format_rental_line produces expected line format"""
    line = format_rental_line("Alvarez", 145.0, False, False)
    assert line == "Alvarez: $145.00 | deposit: no | inspection: no"
