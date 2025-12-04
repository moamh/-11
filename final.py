def calculate_price_with_tax():
    # Product List: [Name, Price]
    products = [
        ["Product 1", 10],
        ["Product 2", 20],
        ["Product 3", 30],
        ["Product 4", 40],
        ["Product 5", 50]
    ]

    tax_rate = 0.15 

    print("--- Price Calculator with Tax ---")

    # Display products
    print("\nAvailable Products:")
    for i, item in enumerate(products):
        print(f" {i + 1}. {item[0]} - Price: {item[1]} SAR")

    while True:
        try:
            user_input = input("\nEnter product number: ")
            
            if not user_input.isdigit():
                print("Please enter numbers only.")
                continue
            
            index = int(user_input) - 1
            
            if 0 <= index < len(products):
                selected = products[index]
                price = selected[1]
                
                final_price = price + (price * tax_rate)
                
                print("------------------------------------")
                print(f"OK Item: {selected[0]}")
                print(f"Total Price (with Tax): {final_price:.2f} SAR")
                print("------------------------------------")
                break
            else:
                print("Invalid number. Choose from 1 to 5.")

        except Exception:
            print("Error occurred.")

if __name__ == "__main__":
    calculate_price_with_tax()
