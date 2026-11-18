# Tier 2: The ATM

## The problem

Withdraw money from an ATM.

## The algorithm

1. Wait for a card to be inserted.
2. Read the card. If it can't be read, eject it and show "Card cannot be read." Stop.
3. Ask for the PIN.
4. Check the PIN against the bank's record. If it's wrong, let the user try again. After 3 wrong tries, keep the card and lock it.
5. Show the menu and wait for the user to choose "Withdraw."
6. Ask for the amount.
7. Check the amount is valid (a positive number, in multiples of the smallest note).
8. Check the account balance. If the amount is more than the balance, show "Insufficient funds" and let them enter a smaller amount or cancel.
9. Check the ATM has enough cash. If not, show "ATM cannot dispense this amount" and offer a smaller amount.
10. Deduct the amount from the account.
11. Dispense the cash.
12. Confirm the cash was taken. If the transaction failed halfway (cash not dispensed), reverse the deduction.
13. Offer a receipt.
14. Return the card and end the session.

## Why each step matters, and what could go wrong

- **Card unreadable:** eject it and show an error. Never continue with unknown data.
- **Wrong PIN:** allow a few retries, then lock the card to protect the owner.
- **Amount greater than balance:** refuse it and let them try again.
- **ATM out of cash:** tell the user and offer a smaller amount.
- **Transaction fails:** cancel it and make sure no money is deducted. The customer should never lose money for cash they didn't receive.

## Problem vs algorithm vs program

- **Problem:** the goal ("withdraw money").
- **Algorithm:** the step-by-step plan above.
- **Program:** that plan written in code the computer can run.
