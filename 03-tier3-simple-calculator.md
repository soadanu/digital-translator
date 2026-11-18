# Tier 3: The Simple Calculator

| Operation      | Input | Processing | Output |
|----------------|-------|------------|--------|
| Addition       | 20, 5 | 20 + 5     | 25     |
| Subtraction    | 20, 5 | 20 − 5     | 15     |
| Multiplication | 20, 5 | 20 × 5     | 100    |
| Division       | 20, 5 | 20 ÷ 5     | 4      |

## What if number_2 is 0?

Division by zero has no answer, so the computer can't produce a valid result. A badly designed program would crash or give nonsense.

A well-designed one checks before dividing: "is the second number 0?" If yes, it skips the division and shows a message like "Cannot divide by zero. Please enter a different number." Then it carries on instead of failing.
