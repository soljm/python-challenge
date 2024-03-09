import os
import csv

# open and read CSV file
with open("PyBank/Resources/budget_data.csv", encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    csv_header = next(csvfile)

    # set initial values
    total_months = 0
    net_profit = 0
    first_month_profit = None
    final_month_profit = None
    last_month_profit = None
    greatest_increase = None
    greatest_decrease = None
    greatest_increase_date = None
    greatest_decrease_date = None

    # loop through the rows, assigning date and profit to their respective columns
    for date, profit in csv_reader:
        # counting total months
        total_months += 1

        # calculating net profit
        profit = int(profit)
        net_profit += profit

        # finding the profit for the first month and the last month
        final_month_profit = profit
        if first_month_profit is None:
            first_month_profit = profit

        # calculate profit change per month
        if last_month_profit is not None:
            current_change = profit - last_month_profit

            # greatest increase
            if greatest_increase is None or (current_change > greatest_increase):
                greatest_increase = current_change
                greatest_increase_date = date

            # greatest decrease
            if greatest_decrease is None or (current_change < greatest_decrease):
                greatest_decrease = current_change
                greatest_decrease_date = date

        # set current profit 
        last_month_profit = profit

# calculating average change and rounding to 2 decimal places
average_change = (final_month_profit - first_month_profit) / (total_months - 1)
average_change = round(average_change, 2)

# creating a new text file and writing the analysis
with open("PyBank/Analysis/output.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_profit}\n")
    f.write(f"Average Change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}")

# reading the text file to print in terminal
with open("PyBank/Analysis/output.txt", "r") as f:
    for line in f:
        print(line)