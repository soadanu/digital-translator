# Tier 4: Data representation
import struct


def run():
    customer = {
        "name": "Victor",
        "age": 30,
        "balance": 150000.50,
        "active": True,
    }

    print("Kinds of data:")
    for key, value in customer.items():
        print(f"  {key:8} = {value!r:12} type: {type(value).__name__}")

    print("\nHow each becomes binary:")

    print("  Name 'Victor' -> one numeric code per character:")
    for ch in customer["name"]:
        print(f"    {ch} -> {ord(ch):3} -> {ord(ch):08b}")

    print(f"  Age 30 -> {customer['age']:08b}")

    raw = struct.pack(">d", customer["balance"])
    print("  Balance 150000.50 -> 64 bits:")
    print("    " + "".join(f"{byte:08b}" for byte in raw))

    print(f"  Active True -> {int(customer['active'])}")

    # Reasoning challenge: same stored bits, wrong interpretation
    wrong = struct.unpack(">q", raw)[0]
    print("\nWhat if the balance bits are read as a whole number instead?")
    print(f"  Correct value : {customer['balance']}")
    print(f"  Wrongly read  : {wrong}")
    print("  Same bits, completely different meaning.")


if __name__ == "__main__":
    run()
