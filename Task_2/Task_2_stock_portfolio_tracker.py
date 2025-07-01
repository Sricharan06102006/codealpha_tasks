# stock_portfolio_tracker.py

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135,
    "MSFT": 330
}

# Dictionary to hold user's portfolio
portfolio = {}

print("🧩 Task 2: Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from available stocks.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("❌ Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n📊 Your Portfolio Summary:")
print("{:<10} {:<10} {:<10}".format("Stock", "Qty", "Value"))
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print("{:<10} {:<10} ${:<10.2f}".format(stock, qty, value))

print("\n💰 Total Investment Value: ${:.2f}".format(total_value))

# Option to save to file
save = input("Do you want to save the summary to a file? (yes/no): ").lower()

if save == 'yes':
    file_type = input("Choose file type (txt/csv): ").lower()
    if file_type == 'txt':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock}: Qty={qty}, Value=${value:.2f}\n")
            f.write(f"Total Investment Value: ${total_value:.2f}\n")
        print("📁 Summary saved as 'portfolio_summary.txt'")
    elif file_type == 'csv':
        import csv
        with open("portfolio_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock] * qty])
            writer.writerow(["Total", "", total_value])
        print("📁 Summary saved as 'portfolio_summary.csv'")
    else:
        print("❌ Invalid file type. No file was saved.")
else:
    print("📝 Summary not saved.")
