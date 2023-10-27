def generate_shoe_receipt(customer_name, brand_name, model, size, price):
    receipt = f"╔══════════════════════════════════╗\n"
    receipt += f"║     {brand_name} Shoe Receipt      ║\n"
    receipt += f"║                                  ║\n"
    receipt += f"║ Customer: {customer_name}     ║\n"
    receipt += f"║ Model:    {model}        ║\n"
    receipt += f"║ Size:     {size}           ║\n"
    receipt += f"║ Price:    ${price:.2f}          ║\n"
    receipt += f"║                                  ║\n"
    receipt += f"║ Thank you for your purchase!  ║\n"
    receipt += f"╚══════════════════════════════════╝"

    return receipt

# Example usage
customer_name = "John Doe"
brand_name = "MyBrand"
model = "Sneaker Model X"
size = "US 10"
price = 99.99

receipt = generate_shoe_receipt(customer_name, brand_name, model, size, price)
print(receipt)
