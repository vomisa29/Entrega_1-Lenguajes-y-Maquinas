
file_name= input("Ingrese el nombre del archivo: ")
file = open("ExampleCodeLYM.txt", encoding="utf8")
all_lines = file.readlines()
for line in all_lines:
    line_string = line.strip()
    

