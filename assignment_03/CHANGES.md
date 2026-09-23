# Assignment 03 — CHANGES

**Name:** Han Htoo Aung  **Student ID:** 6705140067

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product stored as bare tuple `("Laptop", 1200.0, "electronics")` | Created `Product` and `FoodProduct` classes with explicit attributes | Domain Modelling & Classes | Ran `python Assignment_03.py` -> PASS |
| 2 | Direct `if cat == "food"` check during tax calculation | Overrode `tax_for()` in `FoodProduct` to return `0.0` tax | Inheritance & Polymorphism | Ran `python Assignment_03.py` -> PASS |
| 3 | Long `if/elif t == "silver"` chains for discounts and points | Created `Customer` base class and `Silver`, `Gold`, `Platinum` subclasses | Inheritance & Polymorphism | Ran `python Assignment_03.py` -> PASS |
| 4 | Tuple-based order representations and direct list operations | Structured `OrderItem` (has-a `Product`) and `Order` (has-a `Customer`, has-many `OrderItem`) | Composition (Has-A) | Ran `python Assignment_03.py` -> PASS |
| 5 | Hardcoded values (`0.07`, `100`, `10`) and leftover `global TAXRATE` | Replaced with uppercase constants (`STANDARD_TAX_RATE`, `DISCOUNT_THRESHOLD`, etc.) | Encapsulation & Clean Code | Ran `python Assignment_03.py` -> PASS |

## 2 · Short reflection (4–6 sentences)

> Replacing the tier conditional chains with polymorphic customer classes improved the code the most because it eliminated messy branch logic and made adding new membership tiers straightforward without modifying core order processing[cite: 1]. Separating the product tax logic into a `FoodProduct` subclass further cleaned up calculation logic by letting objects handle their own behavior[cite: 1]. Keeping the behavior identical forced me to be extra careful with exact string formatting, rounding behavior, and space placement in the printed receipt output[cite: 1]. I ensured that all financial calculations remained pure functions that return numeric values rather than printing directly within calculation methods[cite: 1]. This strict separation of concerns made testing against `GOLDEN_OUTPUT` seamless[cite: 1].

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Refactor this tier discount if/elif into subclasses" | Base `Customer` + 4 subclasses for membership tiers | Edited (renamed methods and simplified return statements) | Self-test PASS; read every line |
| 2 | "Fix Requirement 4 and 5: Tax Polymorphism & Tier Factory" | Refactored `Product` into `Product` and `FoodProduct` subclasses to remove `if category` check, and cleaned `make_customer` factory lookup | Accepted | Ran `python Assignment_03.py` -> PASS; verified zero output diff |
| 3 | "Help me update CHANGES.md" | Completion of `CHANGES.md` including change table, prompt log and reflection | Accepted | Verified alignment with codebase and rubric |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.