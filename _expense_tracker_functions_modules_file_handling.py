import math
import random
import datetime
import pandas as pd
import csv

# Function to calculate the tax on an expense, with a default tax rate of 5%
def calculate_tax(expense, tax_rate=0.05):
    """Calculate the tax on an expense."""
    return expense * tax_rate

# Function to format and print an expense report based on the specified order
def print_expense_report(amount, category, description, order='amount'):
    """Format and print an expense report based on the specified order."""
    if order == 'amount':
        print(f"Amount: {amount}, Category: {category}, Description: {description}")
    elif order == 'category':
        print(f"Category: {category}, Amount: {amount}, Description: {description}")

# Function to summarize total expenses for each category
def summarize_expenses(*expenses, **categories):
    """Summarize total expenses for each category."""
    summary = {}
    for expense, category in zip(expenses, categories.keys()):
        summary[category] = summary.get(category, 0) + expense
    for category, total in summary.items():
        print(f"Total for {category}: {total}")

# List of expenses
expenses = [100, 200, 50, 300, 25]

# Lambda function to sort the list of expenses in ascending order
sorted_expenses = sorted(expenses)
print("Sorted expenses:", sorted_expenses)

# Lambda function to filter out expenses below a certain threshold
threshold = 100
filtered_expenses = list(filter(lambda x: x >= threshold, expenses))
print("Filtered expenses (>=100):", filtered_expenses)

# Importing datetime module correctly
from datetime import datetime

# Demonstrate the use of the math module for rounding expenses
PI = math.pi
print(f"PI value: {PI}")
rounded_expense = math.ceil(100.75)
print(f"Rounded expense: {rounded_expense}")

# Demonstrate the use of the random module to generate a random expense amount
random_expense = random.uniform(50, 300)
print(f"Random expense: {random_expense}")

# Demonstrate the use of the datetime module to add a timestamp to transactions
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Timestamp: {current_time}")

# Utility function to calculate the total of a list of expenses
def calculate_total(expenses):
    """Calculate total expenses."""
    return sum(expenses)

# Utility function to apply a discount to an amount
def apply_discount(amount, discount):
    """Apply discount to an amount."""
    return amount - (amount * discount)

# Calculate and print the total of a given list of expenses
expenses_list = [100, 200, 50]
total_expenses = calculate_total(expenses_list)
print("Total Expenses:", total_expenses)

# Create a DataFrame with sample expense data
data = {'Date': ['2024-10-01', '2024-10-02'], 'Category': ['Food', 'Transport'], 'Amount': [100, 50]}
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file and print it
df.to_csv('expenses.csv', index=False)
print(df)

# Read the data from the CSV file and print it
df_read = pd.read_csv('expenses.csv')
print(df_read)

# Function to log a list of expenses to a text file
def log_expenses_to_file(expenses):
    """Log expenses to a file."""
    with open('expenses.txt', 'w') as file:
        for expense in expenses:
            file.write(f"{expense}\n")

# Function to read expenses from a text file and print them
def read_expenses_from_file():
    """Read expenses from a file and print them."""
    with open('expenses.txt', 'r') as file:
        for line in file:
            print(line.strip())  # strip() removes the newline character

# Function to log an expense with a timestamp to a text file
def log_expense_with_timestamp(expense):
    """Log an expense with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('expenses.txt', 'a') as file:
        file.write(f"{timestamp} - Expense: {expense}\n")

# Function to write a list of expenses to a CSV file
def write_expenses_to_csv(expenses):
    """Write expenses to a CSV file."""
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount'])
        for expense in expenses:
            writer.writerow([expense['date'], expense['category'], expense['amount']])

# Function to read expenses from a CSV file and print them
def read_expenses_from_csv():
    """Read expenses from a CSV file and print them."""
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Example usage
if __name__ == "__main__":
    # Calculate tax on an expense of 100
    print(calculate_tax(100))
    
    # Print expense report with category first
    print_expense_report(50, 'Food', 'Lunch', order='category')
    
    # Summarize expenses with different categories
    summarize_expenses(100, 200, 50, 300, 25, Food='Food', Transport='Transport', Entertainment='Entertainment')
    
    # Print sorted expenses
    print(sorted_expenses)
    
    # Print filtered expenses which are >= 100
    print(filtered_expenses)
    
    # Print a random expense amount
    print(f"Random expense: {random_expense}")
    
    # Print the current timestamp
    print(f"Current Time: {current_time}")
    
    # Print the rounded expense amount
    print(f"Rounded Expense: {rounded_expense}")
    
    # Print the total of expenses
    print(f"Total Expenses: {total_expenses}")
    
    # Log expenses to a text file
    log_expenses_to_file(['100 Food Lunch', '50 Transport Uber'])
    
    # Read and print expenses from a text file
    read_expenses_from_file()
    
    # Log an expense with a timestamp to a text file
    log_expense_with_timestamp(150)
    
    # Write expenses to a CSV file
    write_expenses_to_csv([{'date': '2024-10-01', 'category': 'Food', 'amount': 100}, {'date': '2024-10-02', 'category': 'Transport', 'amount': 50}])
    
    # Read and print expenses from a CSV file
    read_expenses_from_csv()