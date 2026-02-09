# SUBIT-96 Examples

This document provides example computations of the SUBIT-96 ⊕ operation and the valence function V.

---

## 1. Maximal Creativity

**Input:**

```

x = (ME, EAST, SPRING)
y = (ME, EAST, SUMMER)

```

**Operation:**

```

x ⊕ y = (ME ⊗ WHO ME, EAST ⊗ WHERE EAST, SPRING ⊗ WHEN SUMMER)
= (WE, EAST, SUMMER)

```

**Valence:**

```

V(x ⊕ y) = V(WE) + V(EAST) + V(SUMMER)
= 2 + 3 + 1
= +6

```

> Represents a highly creative archetype.

---

## 2. Maximal Destruction

**Input:**

```

x = (THEY₀, SOUTH, AUTUMN)
y = (THEY₀, SOUTH, AUTUMN)

```

**Operation:**

```

x ⊕ y = (THEY₀ ⊗ WHO THEY₀, SOUTH ⊗ WHERE SOUTH, AUTUMN ⊗ WHEN AUTUMN)
= (THEY₀, SOUTH, WINTER)

```

**Valence:**

```

V(x ⊕ y) = V(THEY₀) + V(SOUTH) + V(WINTER)
= 0 + (-2) + 0
= -2

```

> Represents maximal destructive influence within the system.

---

## 3. Absolute Stability

**Input:**

```

x = (THEY₄, NORTH, WINTER)
y = (THEY₄, NORTH, WINTER)

```

**Operation:**

```

x ⊕ y = (THEY₄ ⊗ WHO THEY₄, NORTH ⊗ WHERE NORTH, WINTER ⊗ WHEN WINTER)
= (THEY₄, NORTH, WINTER)

```

**Valence:**

```

V(x ⊕ y) = V(THEY₄) + V(NORTH) + V(WINTER)
= 4 + 0 + 0
= +4

```

> Represents absolute stability: constants, laws, or invariants.

---

## 4. Mixed Example

**Input:**

```

x = (ME, WEST, AUTUMN)
y = (YOU⁺, EAST, SPRING)

```

**Operation:**

```

x ⊕ y = (ME ⊗ WHO YOU⁺, WEST ⊗ WHERE EAST, AUTUMN ⊗ WHEN SPRING)
= (YOU⁺, NORTH, SPRING)

```

**Valence:**

```

V(x ⊕ y) = V(YOU⁺) + V(NORTH) + V(SPRING)
= +1 + 0 + 3
= +4

```

> Example of mixed interaction between agents, space, and time phase.

---

**Notes:**

- Use the CSV tables in `tables/` folder to compute any ⊕ operation.  
- The valence function V is additive across WHO, WHERE, and WHEN components.  
- Examples demonstrate **creativity, destruction, and stability archetypes** in SUBIT-96.

