# Tier 4: Data Translator

| Information | Kind of data   |
|-------------|----------------|
| Victor      | Text           |
| 30          | Whole number   |
| 150000.50   | Decimal number |
| Yes         | True/false     |

## Why each kind needs its own representation

A computer needs to know the kind of each value because it handles them differently. You can add 30 + 1, but you can't add "Victor" + 1. Money needs decimals, but age doesn't. A yes/no only needs two states.

## How it becomes binary

Underneath, everything becomes binary (0s and 1s):

- Letters in "Victor" are stored as numeric codes, one per character.
- Numbers are stored in binary form.
- True/false is just 1 or 0.

## If the balance were read wrongly

The same stored bits would mean a different value. 150000.50 might show as 15000050, or as text. The customer could appear to have far more or far less money than they really do, which could cause wrong withdrawals, blocked payments, or even financial loss.

Data is only useful when it's interpreted the way it was stored.
