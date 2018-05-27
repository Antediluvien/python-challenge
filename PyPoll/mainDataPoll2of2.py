from __future__ import division
import csv
import os
path = "D:\election_data_2.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader) # the first line is the header
reader_list = list(reader)
identification = []
county = []
candidate = []
for i in reader_list:
    id = i[0]
    cnty = str(i[1])
    cand = str(i[2])
    identification.append([id])
    county.append([cnty])
    candidate.append((cand))

Correy = []
Khan = []
Li = []
OTooley = []

for i in reader_list:
    if i[2] == 'Correy':
        Correy.append(i[2])
    elif i[2] == 'Khan':
        Khan.append(i[2])
    elif i[2] == 'Li':
        Li.append(i[2])
    elif i[2] =='O\'Tooley':
        OTooley.append(i[2])


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(identification)))
print("-------------------------")
print("Correy: " + str(round((len(Correy)/(len(identification))*100),2)) + "%  " + "(" + str(len(Correy)) + ")")
print("Khan: " + str(round((len(Khan)/(len(identification))*100),2)) + "%  " +  "(" + str(len(Khan)) + ")")
print("Li: " + str(round((len(Li)/(len(identification))*100),2)) + "%  " +  "(" + str(len(Li)) + ")")
print("O'Tooley: " + str(round((len(OTooley)/(len(identification))*100),2)) + "%  " +  "(" + str(len(OTooley)) + ")")
print("-------------------------")

def Result_calculation ():
    if len(Correy)> len(Khan) and len(Correy)>len(Li) and len(Correy)>len(OTooley):
        return("Correy is the winner")
    elif len(Khan)> len(Correy) and len(Khan)>len(Li) and len(Khan)>len(OTooley):
        return("Khan is the winner")
    elif len(Li)> len(Khan) and len(Li)>len(Correy) and len(Li)>len(OTooley):
        return("Li is the winner")
    elif len(OTooley)> len(Khan) and len(OTooley)>len(Li) and len(OTooley)>len(Correy):
        return("O'Tooley is the winner")
    else:
        return("There is no winner")
print(Result_calculation())

election_results = ["Election Results"]
separator = ["-------------------------"]
Total_res= ["Total Votes: " + str(len(identification))]
Corr = ["Correy: " + str(round((len(Correy)/(len(identification))*100),2)) + "%  " + "(" + str(len(Correy)) + ")"]
Kh = ["Khan: " + str(round((len(Khan)/(len(identification))*100),2)) + "%  " +  "(" + str(len(Khan)) + ")"]
Li = ["Li: " + str(round((len(Li)/(len(identification))*100),2)) + "%  " +  "(" + str(len(Li)) + ")"]
OT = ["O'Tooley: " + str(round((len(OTooley)/(len(identification))*100),2)) + "%  " +  "(" + str(len(OTooley)) + ")"]
results = [Result_calculation()]


output_file = os.path.join("C:/Users\Antediluvien\Documents\HaroldsOutputDataPoll2of2.txt")
with open(output_file, 'w', newline= '') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(election_results)
    writer.writerow(separator)
    writer.writerow(Total_res)
    writer.writerow(separator)
    writer.writerow(Corr)
    writer.writerow(Kh)
    writer.writerow(Li)
    writer.writerow(OT)
    writer.writerow(separator)
    writer.writerow(results)