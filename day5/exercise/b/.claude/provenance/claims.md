# Recording a claim

`provenance/claims.yaml` holds what you are actually asserting, and what backs
each assertion. This is the part a reader would otherwise have to reconstruct
by guessing.

```yaml
claims:
  - id: <slug>
    statement: >
      <the assertion, in one or two sentences, as you would say it out loud>
    evidence:
      - <file>::<function that establishes it>
      - <a citation, with the equation, section or figure number>
    numbers: [<slugs that appear in numbers.json>]
```

Every claim needs a statement and at least one piece of evidence. Evidence is
either code that ships here, or a citation precise enough to look up. Every
slug under `numbers:` must exist in `numbers.json`.

A claim is not "what I did". It is what you are asking the reader to believe.
