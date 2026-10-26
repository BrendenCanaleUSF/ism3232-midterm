# mkdir ism3232-midterm
# cd ism3232-midterm
# python3 -m venv .venv
# source .venv/bin/activate
# pip install pytest ruff
# touch business_rules.py main.py requirements.txt .gitignore commands.md README.md
#  mkdir tests
# touch tests/__init__.py tests/test_business_rules.py
# pip freeze > requirements.txt
# echo ".venv/" >> .gitignore
# echo "__pycache__/" >> .gitignore


# % which python3
/home/brend/ism3232/ism3232-midterm/.venv/bin/python3

# % tree -L 2
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

#  % rg 'def'
business_rules.py
11:def calculate_rental_cost(daily_rate: float, days: int) -> float:
15:def format_rental_cost(daily_rate: float, days: int) -> float:
19:def get_rental_discount(days: int, contractor: bool) -> float:
27:def calculate_quote(daily_rate: float, days: int, contractor: bool) -> float:
37:def requires_deposit(quote: float) -> bool:
41:def needs_inspection(days: int, quote: float) -> bool:
45:def total_quoted(rentals: List[Dict[str, Any]]) -> float:
55:def largest_rental(rentals: List[Dict[str, Any]]) -> str:
76:def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:

main.py
14:def main() -> None:

tests/test_business_rules.py
3:def test_calculate_rental_cost_standard() -> None:
7:def test_calculate_rental_cost_zero_days() -> None:
11:def test_get_rental_discount_non_contractor() -> None:
15:def test_get_rental_discount_contractor_below_limit() -> None:
19:def test_get_rental_discount_contractor_at_limit() -> None:
23:def test_get_rental_discount_contractor_above_limit() -> None:
27:def test_calculate_quote_below_waiver_limit() -> None:
31:def test_calculate_quote_at_waiver_limit() -> None:
35:def test_calculate_quote_above_waiver_limit() -> None:
39:def test_requires_deposit_below_limit() -> None:
43:def test_requires_deposit_at_limit() -> None:
47:def test_requires_deposit_above_limit() -> None:
51:def test_needs_inspection_days_at_limit() -> None:
55:def test_needs_inspection_days_above_limit() -> None:
59:def test_needs_inspection_quote_at_limit() -> None:
63:def test_needs_inspection_quote_above_limit() -> None:
67:def test_contractor_flag_changes_answer() -> None:
74:def test_total_quoted_custom_list() -> None:
82:def test_largest_rental_custom_list() -> None:
90:def test_largest_rental_tie() -> None:
98:def test_largest_rental_empty() -> None:
102:def test_format_rental_line() -> None:

#  % rg -l 'print'
main.py

#  % git log --oneline
ba77a2f (HEAD -> master) finished main script including print lines and accompanying logic
40fb8b1 Added tests for business rules #2
25ce5a1 Finished main business rules and calculations along with debugging
de7b970 finished tests for business rules
2a883cf added required imported files in test_business_rules.py
8ec86d4 added gitignore and reqiurements.txt

# 
# 