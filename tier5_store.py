# Tier 5: The online store
# Customer -> Application -> Instructions -> Processing -> Stored data -> Result

PRODUCTS = {"laptop bag": {"price": 50000, "stock": 10}}  # stored data
ORDERS = []                                               # stored data


def place_order(customer, product, quantity, address):
    # Instructions: identify product, check stock, calculate total, save, update
    if product not in PRODUCTS:
        return "Order failed: product not found."

    item = PRODUCTS[product]

    if quantity <= 0:
        return "Order failed: quantity must be at least 1."
    if quantity > item["stock"]:
        return f"Order failed: only {item['stock']} in stock."

    total = item["price"] * quantity          # data processing
    item["stock"] -= quantity                 # update stored data

    ORDERS.append({
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "total": total,
        "address": address,
        "status": "confirmed",
    })

    return f"Order confirmed. Total: {total:,}."  # output


def run():
    # Customer input
    customer = input("Your name: ").strip()
    print("Available:", ", ".join(PRODUCTS))
    product = input("Product: ").strip().lower()
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Order failed: quantity must be a whole number.")
        return
    address = input("Delivery address: ").strip()

    print(place_order(customer, product, quantity, address))

    print("\nStored order records:")
    for order in ORDERS:
        print(" ", order)
    print("Stock left:", PRODUCTS["laptop bag"]["stock"])


if __name__ == "__main__":
    run()
