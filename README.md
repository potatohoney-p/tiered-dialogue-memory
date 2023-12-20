# Tiered Dialogue Memory

Separate a recent-turn window from an archived conversation store and assemble a bounded evidence context.

## Run locally

Use a currently supported Python 3 interpreter. No third-party packages, credentials, downloads, or network access are required.

```sh
python -m unittest discover -s tests -v
python demo.py
```

Run from the repository directory. The demo reads `examples/input.json`; inputs are reproducible, authored examples.

## Scope and behavior

Recent turns are selected newest-first, then lexical matches from the archive fill the remaining word budget. Turns remain verbatim; oversized turns are omitted, never summarized or partially quoted. A word budget is not a provider tokenizer budget. Session filtering is enforced by the database query, but this library does not provide authentication or encryption. All demo conversations are synthetic.

## Layout

- `core.py`: primary algorithm or storage contract.
- `features.py`: pipeline or integration layer.
- `tests/`: independent behavioral assertions, failure cases, and regressions.
- `demo.py` and `examples/input.json`: repeatable end-to-end example.

## Example output

```json
{
  "budget": 12,
  "turns": [
    {
      "id": 4,
      "role": "user",
      "text": "Use a square canvas.",
      "tier": "recent"
    },
    {
      "id": 3,
      "role": "user",
      "text": "The next task is drawing.",
      "tier": "recent"
    }
  ],
  "words": 9
}
```

## Compatibility and license

The implementation uses language features and standard-library APIs available in [Python 3.4](https://docs.python.org/3.4/library/index.html), released in [March 2014](https://www.python.org/downloads/release/python-340/). Use a supported runtime; an old interpreter is not required. Compatibility with a historical runtime is not certified by current-runtime tests.

MIT licensed. No third-party source code or datasets are bundled.
