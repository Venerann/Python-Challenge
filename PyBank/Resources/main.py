import os
import csv

csv_path = 'budget_data.csv'
output_folder = '../Analysis'
output_file = os.path.join(output_folder, 'financial_analysis.txt')

total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:

        total_months += 1

        current_profit = int(row[1])
        net_total += current_profit

        if total_months > 1:
            profit_change = current_profit - previous_profit
            profit_changes.append(profit_change)

            if profit_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_change]
            elif profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_change]

        previous_profit = current_profit

average_change = sum(profit_changes) / len(profit_changes)

analysis_results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
]

for result in analysis_results:
    print(result)

os.makedirs(output_folder, exist_ok=True)
with open(output_file, 'w') as file:
    file.writelines('\n'.join(analysis_results))

print(f"\nAnalysis results have been exported to '{output_file}'.")
