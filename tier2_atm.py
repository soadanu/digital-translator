# Tier 2: The ATM
# Problem: withdraw money.  Algorithm: the ordered steps below.
# Program: this code. Failures are handled at each step.

ACCOUNT = {"card": "1234", "pin": "0000", "balance": 50000}
ATM_CASH = 100000
MAX_PIN_TRIES = 3
SMALLEST_NOTE = 500


def run():
    global ATM_CASH

    # 1-2. Insert and read card
    card = input("Insert card (type the card number, e.g. 1234): ").strip()
    if card != ACCOUNT["card"]:
        print("Card cannot be read. Card returned.")
        return

    # 3-4. Request and validate PIN, with limited tries
    tries = 0
    while True:
        pin = input("Enter PIN (hint: 0000): ").strip()
        if pin == ACCOUNT["pin"]:
            break
        tries += 1
        if tries >= MAX_PIN_TRIES:
            print("Too many wrong PINs. Card retained and locked.")
            return
        print(f"Wrong PIN. {MAX_PIN_TRIES - tries} tries left.")

    # 5. Select withdrawal
    choice = input("Choose: 1) Withdraw  2) Cancel : ").strip()
    if choice != "1":
        print("Session ended. Card returned.")
        return

    # 6-9. Get an amount and check everything that could go wrong
    while True:
        text = input("Enter amount: ").strip()

        if not text.isdigit() or int(text) <= 0:
            print("Invalid amount. Enter a positive whole number.")
            continue

        amount = int(text)

        if amount % SMALLEST_NOTE != 0:
            print(f"Amount must be a multiple of {SMALLEST_NOTE}.")
            continue
        if amount > ACCOUNT["balance"]:
            print("Insufficient funds. Try a smaller amount.")
            continue
        if amount > ATM_CASH:
            print("ATM cannot dispense this amount. Try a smaller amount.")
            continue
        break

    # 10-12. Deduct, dispense, and undo if dispensing fails
    ACCOUNT["balance"] -= amount
    dispensed = dispense_cash(amount)

    if not dispensed:
        ACCOUNT["balance"] += amount  # reverse the deduction
        print("Transaction failed. No money was deducted.")
        return

    ATM_CASH -= amount
    print(f"Dispensing {amount}. Please take your cash.")

    # 13-14. Receipt and return card
    print(f"Remaining balance: {ACCOUNT['balance']}")
    print("Card returned. Goodbye.")


def dispense_cash(amount):
    # In a real ATM this talks to hardware, which can fail.
    return True


if __name__ == "__main__":
    run()
