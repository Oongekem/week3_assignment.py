def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
