import json
import sys
from pathlib import Path

from .checker import check_shipment


def main():
    if len(sys.argv) != 2:
        print("Usage: tradedoccheck <shipment.json>")
        return 2

    path = Path(sys.argv[1])

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 2
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}")
        return 2

    errors = check_shipment(data)

    if errors:
        print("CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CHECK PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
