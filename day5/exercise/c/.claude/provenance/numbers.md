# Recording a number

`provenance/numbers.json` is a JSON object. One entry per number you report,
keyed by a short slug of your choosing.

```json
{
  "<slug>": {
    "value": <the number>,
    "statement": "<what this number is, in one line>",
    "produced_by": "<file>::<function that computed it>",
    "from_scratch": "<what you derived or implemented yourself>",
    "from_library": "<what you called, and from where>",
    "choices": ["<each decision that had a defensible alternative, and why you made it that way>"]
  }
}
```

All six fields are required. `choices` may be an empty list only if there was
genuinely nothing to decide — write `[]` explicitly rather than omitting it.

If a number appears in your reply and not here, the record is incomplete.
