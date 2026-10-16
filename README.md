# Scaffold Math

Honest scaffold arithmetic. The box claims a twelve-foot reach; Scaffold Math subtracts, divides
and tells you how high the platform really stands.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The reach truth** - claimed reach minus the person norm: the honest platform height.
- **The tower truth** - wall length vs. what one tower covers: the honest tower count.
- **The plank truth** - planks per level times levels: the honest plank count.

## The boundary

Scaffold Math keeps reach, tower and plank arithmetic only. It gives no verdicts about load
ratings or safe assembly - what holds weight is the manufacturer's rating, and the manual owns
guardrails, outriggers and ties. Never improvise a stack, and follow local height-safety rules.
Every figure is hypothetical arithmetic on labeled norms, not a statement about any real equipment
or structure.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 25 cases / 25 checks
```

Live at https://ilanis-agent.github.io/scaffoldmath/
