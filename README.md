# TradeDocCheck

A small, open-source Python tool for checking common shipment-document data before customs or freight processing.

## What it does

TradeDocCheck performs simple, transparent checks on structured shipment data, including:

- Required invoice number and origin
- Positive quantities and prices
- 8-digit HS-code format
- Missing item descriptions
- Duplicate item codes

It is intentionally dependency-free so it can be used as a small library or command-line tool.

> This project is a general document-quality checker. It does not provide legal, customs, or tax advice.

## Quick start

```bash
git clone https://github.com/YOUR-USERNAME/tradedoccheck.git
cd tradedoccheck

python -m tradedoccheck.cli example.json
```

## Example input

```json
{
  "invoice_number": "INV-1001",
  "origin": "Germany",
  "items": [
    {
      "item_code": "ABC-100",
      "description": "Example basin",
      "quantity": 10,
      "unit_price": 25.5,
      "hs_code": "39249090"
    }
  ]
}
```

## Development

Run tests with:

```bash
python -m unittest discover -s tests -v
```

## License

MIT
