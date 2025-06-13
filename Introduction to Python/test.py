def center_text(text, width=50):
    return text.center(width)

# Header
print("=" * 50)
print(center_text("🌟 WELCOME TO INTERNATIONAL BOOKSTORE 🌟"))
print("=" * 50)

# Accept the price per unit of each item
print("\n📌 Enter the cost of the following items:")
prices = {
    "Paper": float(input("   📄 Paper (per sheet)   : P ")),
    "Pencil": float(input("   ✏ Pencil (per piece)   : P ")),
    "Scissors": float(input("   ✂ Scissors (per pair)  : P ")),
    "Eraser": float(input("   🧼 Eraser (per piece)   : P "))
}

# Accept the quantity of each item purchased
print("\n🛒 How many items did you buy?")
quantities = {
    "Paper": int(input("   📄 Paper       : ")),
    "Pencil": int(input("   ✏ Pencil      : ")),
    "Scissors": int(input("   ✂ Scissors    : ")),
    "Eraser": int(input("   🧼 Eraser      : "))
}

# Calculate total price per item and total amount due
total_per_item = {item: prices[item] * quantities[item] for item in prices}
total_amount_due = sum(total_per_item.values())

# Accept the cash amount given by the customer
print("\n" + "=" * 50)
print(center_text(f"💰 TOTAL PRICE: P {total_amount_due:.2f}"))
cash_given = float(input("   🔹 Enter Cash Given: P "))

# Compute change, VAT, and other details
change = cash_given - total_amount_due
price_before_vat = total_amount_due / 1.12
vat_amount = total_amount_due - price_before_vat
total_items = sum(quantities.values())

# Display final sales invoice
print("\n" + "=" * 50)
print(center_text("🧾 OFFICIAL SALES INVOICE "))
print("=" * 50)

# Centering the sales invoice content
print(center_text(f"{'Item':<15}{'Qty':>5}{'Unit Price':>15}{'Total':>15}"))
print(center_text("-" * 45))

for item in prices:
    print(center_text(f"{item:<15}{quantities[item]:>5}  P{prices[item]:>12.2f}  P{total_per_item[item]:>12.2f}"))

print(center_text("-" * 45))
print(center_text(f"{'TOTAL AMOUNT DUE':<35} P{total_amount_due:>12.2f}"))
print(center_text(f"{'CASH GIVEN':<35} P{cash_given:>12.2f}"))
print(center_text(f"{'CHANGE':<35} P{change:>12.2f}"))
print(center_text("-" * 45))
print(center_text(f"{'Price Before VAT (12%)':<35} P{price_before_vat:>12.2f}"))
print(center_text(f"{'VAT Amount':<35} P{vat_amount:>12.2f}"))
print(center_text(f"{'Total Number of Items':<35} {total_items:>12}"))
print("=" * 50)
print(center_text("💖 Thank you for shopping with us! Have a great day! 💖"))
print("=" * 50)
