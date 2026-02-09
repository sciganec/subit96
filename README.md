# SUBIT-96: Finite Algebra of Agent–Vector–Phase States

## Overview

SUBIT-96 is a finite algebra modeling states of the form WHO × WHERE × WHEN.
- Total elements: |S| = 96
- Binary operation: ⊕
- Neutral element: 0ₛ = (THEY₀, NORTH, WINTER)
- Valence function: V : S → ℤ

This repository includes:
- Formal PDF article: `SUBIT-96.pdf`
- Component tables and full table CSVs
- Python script to generate the full 96×96 ⊕ table
- Interactive HTML demo for exploration

---

## Tables

- `tables/WHO_table.csv` : WHO ⊗ WHO
- `tables/WHERE_table.csv` : WHERE ⊗ WHERE
- `tables/WHEN_table.csv` : WHEN ⊗ WHEN
- `tables/FULL_TABLE.csv` : Complete ⊕ table

---

## Scripts

- `scripts/generate_full_table.py` : Generate FULL_TABLE.csv from component tables
- `scripts/interactive_demo.html` : Web demo of ⊕ operation and valence

---

## Examples

See `docs/examples.md` for example computations:
- Maximal creativity: `(ME, EAST, SPRING) ⊕ …`
- Maximal destruction: `(THEY₀, SOUTH, AUTUMN) ⊕ …`
- Absolute stability: `(THEY₄, NORTH, WINTER) ⊕ …`

---

## License

MIT License
