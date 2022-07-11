import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
output_data = os.path.join("analysis", "budget_analysis.txt")

#set up the variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
total_net = 0

#Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip header row in analysis
    csv_header = next (csv_file)


    #start a beginning calculations
    firstrow = next(csv_reader)
    total_months += 1
    total_net += int(firstrow[1])
    previous_net = int(firstrow[1])


    for row in csv_reader:
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #calculate greatest increase
        if net_change > greatest_increase [1]:
            greatest_increase [0] = row[0]
            greatest_increase [1] = net_change

        if net_change < greatest_decrease [1]:
            greatest_decrease [0] = row[0]
            greatest_decrease [1] = net_change



net_monthly_average = sum(net_change_list) / len(net_change_list)



output=(f'''
  Financial Analysis
  ----------------------------
  Total Months: {total_months}
  Total: ${total_net}
  Average Change: ${net_monthly_average:.2f}
  Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
  Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
  ''')

print (output)

with open (output_data, "w") as txt_file:
    txt_file.write(output)


#total number of months


#for row in csv_reader:
#Total_Months=Str
#How to separate month from day "-"
# If = pd.read_csv(mystr, sep= '-'), header=next, names=['MonthDay']

#Total_Months=sum(Date)
#print ("Total Months: ")





#net total amount of "Profit/Losses"
#for row in csvreader:
    #profit = int(row[1])
    #if profit > 0
       #sum_profit = sum_profit + sum_profit
        #elif profit < 0
            #sum_loss = sum_loss + sum_profit
#TotalPL = sum_profit - sum_loss
#print (f"Total: {totalPL}")






#changes in "Profit/Losses", then average those changes


#print ("Average Change: ")





#greatest increase in profits (date/amount) 

#print ("Greatest Increase in Profits: ")





#greatest decrease in profits (date/amount)

#print ("Greatest Decrease in Profits: ")