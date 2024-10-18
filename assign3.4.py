def get_item_details():
    items = {
        '001': {'name': 'Apple', 'price': 1.0},
        '002': {'name': 'Banana', 'price': 0.5},
        '003': {'name': 'Orange', 'price': 0.75},
    }
    return items

def start_new_receipt(items):
    receipt = []
    total = 0

    while True:
        barcode = input("Enter item barcode (or 'done' to finish): ")
        if barcode.lower() == 'done':
            break

        if barcode not in items:
            print("Item not found.")
            continue

        quantity = int(input("Enter quantity: "))
        item = items[barcode]
        item_total = item['price'] * quantity
        receipt.append((item['name'], quantity, item_total))
        total += item_total

    print("\nReceipt:")
    for item in receipt:
        print(f"{item[0]}: {item[1]} x ${item[2]:.2f}")
    print(f"Total: ${total:.2f}")

def main():
    items = get_item_details()

    while True:
        start_new = input("Start a new receipt? (yes/no): ")
        if start_new.lower() != 'yes':
            break
        start_new_receipt(items)

if __name__ == "__main__":
    main()