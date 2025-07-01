# 🧩 Task 2: Stock Portfolio Tracker

A simple Python-based stock tracker that calculates your total investment using hardcoded stock prices.

---
## 🚀 Features
- Manually enter stock symbols and quantities.
- Uses a predefined dictionary of stock prices (e.g., AAPL, TSLA).
- Calculates total portfolio investment.
- Optionally saves the result to a `.txt` or `.csv` file.

---
## 🧠 Key Concepts Used
- Dictionaries
- User Input & Output
- Loops & Conditions
- Arithmetic Operations
- File Handling (Text and CSV)

---
## 🖥️ How It Works
1. The program displays a list of available stocks with predefined prices.
2. The user inputs stock symbols (like `AAPL`, `TSLA`) and corresponding quantities.
3. The script calculates the value of each holding and the total investment.
4. User is prompted to save the result in `.txt` or `.csv` format.

---
## 💻 Example

**Console Input:**
Enter stock symbol (or type 'done' to finish): AAPL
Enter quantity for AAPL: 5
Enter stock symbol (or type 'done' to finish): TSLA
Enter quantity for TSLA: 3
Enter stock symbol (or type 'done' to finish): done

**Console Output:**
Your Portfolio Summary:
Stock Qty Value
AAPL 5 $900.00
TSLA 3 $750.00

Total Investment Value: $1650.00

---
## 📄 Sample Output Files

### portfolio_summary.txt
Stock Portfolio Summary
AAPL: Qty=5, Value=$900.00
TSLA: Qty=3, Value=$750.00
Total Investment Value: $1650.00

### portfolio_summary.csv
Stock,Quantity,Value
AAPL,5,900
TSLA,3,750
Total,,1650

---
## 🛠 Requirements
- Python 3.x  
- No external libraries required (except `csv`, which is part of Python standard library)

---
## 📂 How to Run
1. Save the script as `Task_2_stock_portfolio_tracker.py`.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python Task_2_stock_portfolio_tracker.py
