import os
import csv
# Path to file
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
# Open and read CSV file
with open(budget_data_csv, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip header
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    # Set initial values
    total_months = 0
    net_profit = 0
    first_month_profit = None
    final_month_profit = None
    last_month_profit = None
    greatest_increase = None
    greatest_decrease = None
    greatest_increase_date = None
    greatest_decrease_date = None
    
    for date, profit in csv_reader:
        # Total Months
        total_months += 1
        # Net Profit
        profit = int(profit)
        net_profit += profit
        # Average change
        final_month_profit = profit
        if first_month_profit is None:
            first_month_profit = profit

        # Calculate profit change per month
        if last_month_profit is not None:
            current_change = profit - last_month_profit
            # Greatest increase
            if greatest_increase is None or (current_change > greatest_increase):
                greatest_increase = current_change
                greatest_increase_date = date
            # Greatest decrease
            if greatest_decrease is None or (current_change < greatest_decrease):
                greatest_decrease = current_change
                greatest_decrease_date = date

        last_month_profit = profit
        
        # print(f"{date=}, {profit=}, {last_month_profit=}, {current_change=}")

average_change = (final_month_profit - first_month_profit) / (total_months - 1)
average_change = round(average_change, 2)

with open("PyBank/Analysis/output.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_profit}\n")
    f.write(f"Average Change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}")

with open("PyBank/Analysis/output.txt", "r") as f:
    for line in f:
        print(line)