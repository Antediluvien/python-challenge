from __future__ import division
import csv
import os
path = "D:\election_data_1.csv"
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

Cordin = []
Seth = []
Torres = []
Vestal = []

for i in reader_list:
    if i[2] == 'Cordin':
        Cordin.append(i[2])
    elif i[2] == 'Seth':
        Seth.append(i[2])
    elif i[2] == 'Torres':
        Torres.append(i[2])
    elif i[2] =='Vestal':
        Vestal.append(i[2])


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(identification)))
print("-------------------------")
print("Cordin: " + str(len(Cordin)/(len(identification))*100) + "%  " + "(" + str(len(Cordin)) + ")")
print("Seth: " + str(len(Seth)/(len(identification))*100) + "%  " +  "(" + str(len(Seth)) + ")")
print("Torres: " + str(len(Torres)/(len(identification))*100) + "%  " +  "(" + str(len(Torres)) + ")")
print("Vestal: " + str(len(Vestal)/(len(identification))*100) + "%  " +  "(" + str(len(Vestal)) + ")")
print("-------------------------")

def Result_calculation ():
    if len(Cordin)> len(Seth) and len(Cordin)>len(Torres) and len(Cordin)>len(Vestal):
        return("Cordin is the winner")
    elif len(Seth)> len(Cordin) and len(Seth)>len(Torres) and len(Seth)>len(Vestal):
        return("Seth is the winner")
    elif len(Torres)> len(Seth) and len(Torres)>len(Cordin) and len(Torres)>len(Vestal):
        return("Torres is the winner")
    elif len(Vestal)> len(Seth) and len(Vestal)>len(Torres) and len(Vestal)>len(Cordin):
        return("Vestal is the winner")
    else:
        return("There is no winner")
print(Result_calculation())

election_results = ["Election Results"]
separator = ["-------------------------"]
Total_res= ["Total Votes: " + str(len(identification))]
Cor = ["Cordin: " + str(len(Cordin)/(len(identification))*100) + "%  " + "(" + str(len(Cordin)) + ")"]
Se = ["Torres: " + str(len(Seth)/(len(identification))*100) + "%  " +  "(" + str(len(Seth)) + ")"]
To = ["Torres: " + str(len(Torres)/(len(identification))*100) + "%  " +  "(" + str(len(Torres)) + ")"]
Ve = ["Vestal: " + str(len(Vestal)/(len(identification))*100) + "% " +  "(" + str(len(Vestal)) + ")"]
results = [Result_calculation()]


output_file = os.path.join("C:/Users\Antediluvien\Documents\HaroldsOutputDataPoll1of2.txt")
with open(output_file, 'w', newline= '') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(election_results)
    writer.writerow(separator)
    writer.writerow(Total_res)
    writer.writerow(separator)
    writer.writerow(Cor)
    writer.writerow(Se)
    writer.writerow(To)
    writer.writerow(Ve)
    writer.writerow(separator)
    writer.writerow(results)