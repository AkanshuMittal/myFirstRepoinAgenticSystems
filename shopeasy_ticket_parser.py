import json
import re

REQUIRED_KEYS = ["category", "priority", "summary", "needs_human", "suggested_reply"]
ALLOWED_CATEGORIES = {"billing", "shipping", "product", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def strip_markdown_fences(text: str) -> str:
    cleaned = text.strip()
    match = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", cleaned, flags=re.IGNORECASE)
    return match.group(1).strip() if match else cleaned


def extract_json_object(text: str) -> str:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object braces found in model output.")
    return text[start : end + 1]


def safe_parse_model_json(raw: str) -> dict:
    step1 = strip_markdown_fences(raw)
    step2 = extract_json_object(step1)
    data = json.loads(step2)
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON must be an object (dict).")
    return data


# Implement validate_ticket
def validate_ticket(data: dict) -> tuple[bool, str]:
    # Check required keys
    for key in REQUIRED_KEYS:
        if key not in data:
            return False, f"Missing required key: '{key}'"

    # Check category
    if data["category"] not in ALLOWED_CATEGORIES:
        return False, f"Invalid category: '{data['category']}'"

    # Check priority
    if data["priority"] not in ALLOWED_PRIORITIES:
        return False, f"Invalid priority: '{data['priority']}'"

    return True, "ok"


# Implement validate_or_raise
def validate_or_raise(data: dict) -> dict:
    valid, message = validate_ticket(data)
    if not valid:
        raise ValueError(message)
    return data


TEST_CASES = [
    # Case 1 — valid ticket (should print SUCCESS)
    '{"category": "shipping", "priority": "medium", "summary": "Order 4412 arrived late", '
    '"needs_human": false, "suggested_reply": "We are tracking your parcel."}',
    # Case 2 — wrong priority casing (should print FAILED)
    '{"category": "billing", "priority": "HIGH", "summary": "Duplicate charge", '
    '"needs_human": false, "suggested_reply": "Refund initiated."}',
]


# Implement main
def main() -> None:
    for raw in TEST_CASES:
        try:
            parsed = safe_parse_model_json(raw)
            validated = validate_or_raise(parsed)
            print("SUCCESS:", validated)
        except ValueError as e:
            print("FAILED:", e)


if __name__ == "__main__":
    main()