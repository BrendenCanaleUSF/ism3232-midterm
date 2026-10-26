# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Brenden Canale
- **Version:** 1.0
- **Date:** 10-25-2026

## This program calculates cost of equipment rental, utilizes a discount system with tiers and waivers, determines whether security deposits or further inspections are necessary

## Business Rules
1. rental cost equals the daily rate times the number of days
2. discounts are tiered, 3 days at 0%, 3-6 days at 10% and 7+ days at 20%
3. LIcensed contractors automativally get a 10% discount
4. $25 damage fee is added when discounted rental cost is below $150
5. Any quotes at $1000 or more have to have a security deposit
6. rentals with a 5 or more day run time that have a $800+ quote must have a pickup inspection
## How to Run
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to Test
ruff format .
ruff check .
pytest -v

## Files in This Repository
business_rules.py
main.py
commands.md
README.md
requirements.txt
.gitignore
tests/__init__.py
test_business_rules.py

## AI Use Statement

I did not use AI on this exam