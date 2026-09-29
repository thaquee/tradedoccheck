import re

HS_CODE_RE = re.compile(r"^\d{8}$")


def check_shipment(data):
    """Return a list of human-readable validation errors."""
    errors = []

    if not data.get("invoice_number"):
        errors.append("Missing invoice_number.")

    if not data.get("origin"):
        errors.append("Missing origin.")

    items = data.get("items")
    if not isinstance(items, list) or not items:
        errors.append("At least one item is required.")
        return errors

    seen_codes = set()

    for index, item in enumerate(items, start=1):
        prefix = f"Item {index}"

        if not item.get("description"):
            errors.append(f"{prefix}: missing description.")

        quantity = item.get("quantity")
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            errors.append(f"{prefix}: quantity must be greater than zero.")

        unit_price = item.get("unit_price")
        if not isinstance(unit_price, (int, float)) or unit_price < 0:
            errors.append(f"{prefix}: unit_price must be zero or greater.")

        hs_code = str(item.get("hs_code", ""))
        if not HS_CODE_RE.fullmatch(hs_code):
            errors.append(f"{prefix}: hs_code must contain exactly 8 digits.")

        item_code = item.get("item_code")
        if item_code:
            if item_code in seen_codes:
                errors.append(f"{prefix}: duplicate item_code '{item_code}'.")
            seen_codes.add(item_code)

    return errors
