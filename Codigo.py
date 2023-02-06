import csv

file_name= input("Ingrese el nombre del archivo: ")

csvfile = open(file_name, newline='', encoding="utf8")
reader = csv.DictReader(csvfile)
    
for row in reader:
    for element in row:
        print("ass")
