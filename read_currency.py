import csv

with open("currencyrates.csv","r") as file:
      lines =csv.reader(file)
      for line in lines:
            if (line[1]=="BDT"):
                  curr =float(line[3])
                  print(curr*50)