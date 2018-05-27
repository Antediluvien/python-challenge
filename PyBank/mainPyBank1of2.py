import csv
import os
path = "D:\pybank data 1 of 2.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # the first line is the header
data = []
revenue = []
for row in reader:
    date = row[0]
    rev = float(row[1])
    data.append([date])
    revenue.append([rev])


total_months = len(data)

def total_rev(revenue):
  total = 0
  for x in revenue:
    total +=sum(x)
  return total


rev_change= []
for i in range(1,len(revenue)):
    rev_change.append(sum(revenue[i]) - sum(revenue[i - 1]))


avg_rev_change = sum(rev_change)/len(rev_change)
max_rev_change = (float(max(rev_change)))
min_rev_change = (float(min(rev_change)))
max_rev_change_date = data[rev_change.index(max(rev_change))]
min_rev_change_date = data[rev_change.index(min(rev_change))]

print("Financial Analysis")
print("------------------------------------------")
print("Total Months:  " + str(total_months))
print("The total revenue: " + '${:,.2f}'.format(total_rev(revenue)))
print("Greatest Increase in Revenue: " + str(max_rev_change_date[0]) + "  (" + '${:,.2f}'.format(max_rev_change) + ")")
print("Greatest Decrease in Revenue: " + str(min_rev_change_date[0]) + "  (" + '${:,.2f}'.format(min_rev_change) + ")")




Financial_results = ["Financial Results"]
separator = ["-------------------------"]
Total_months= ["Total Months:  " + str(total_months)]
Total_rev = ["The total revenue: " + '${:,.2f}'.format(total_rev(revenue))]
max_rev = ["Greatest Increase in Revenue: " + str(max_rev_change_date[0]) + "  (" + '${:,.2f}'.format(max_rev_change) + ")"]
min_rev = ["Greatest Decrease in Revenue: " + str(min_rev_change_date[0]) + "  (" + '${:,.2f}'.format(min_rev_change) + ")"]


output_file = os.path.join("C:/Users\Antediluvien\Documents\HaroldsOutputPyBankl1of2.txt")
with open(output_file, 'w', newline= '') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(Financial_results)
    writer.writerow(separator)
    writer.writerow(Total_months)
    writer.writerow(Total_rev)
    writer.writerow(max_rev)
    writer.writerow(min_rev)








