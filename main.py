import tier1_breakfast
import tier2_atm
import tier3_calculator
import tier4_data
import tier5_store

TIERS = {
    "1": ("Tier 1: The Literal Assistant", tier1_breakfast),
    "2": ("Tier 2: The ATM", tier2_atm),
    "3": ("Tier 3: The Simple Calculator", tier3_calculator),
    "4": ("Tier 4: Data Translator", tier4_data),
    "5": ("Tier 5: The Online Store", tier5_store),
}

while True:
    print("\nThe Digital Translator")
    for key, (title, _) in TIERS.items():
        print(f"  {key}) {title}")
    print("  q) Quit")
    choice = input("Choose: ").strip().lower()

    if choice == "q":
        break
    if choice in TIERS:
        print()
        TIERS[choice][1].run()
    else:
        print("Invalid choice.")
