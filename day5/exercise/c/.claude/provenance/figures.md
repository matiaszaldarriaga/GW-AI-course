# Recording a figure

Every figure you leave behind needs an entry under `figures:` in
`provenance/claims.yaml`.

```yaml
figures:
  - file: <the file as written on disk>
    produced_by: <file>::<function that draws it>
    shows: >
      <what is on the axes, and what a reader should take from it>
    from_scratch: <what you computed yourself>
    from_library: <what you called>
    choices: ["<each decision that had a defensible alternative>"]
    supports: [<claim ids this figure is evidence for>]
```

A figure with no entry is a picture nobody can regenerate.
