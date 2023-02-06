expected_char = {}
defined_words = {}
file_name= input("Ingrese el nombre del archivo: ")
file = open("ExampleCodeLYM.txt", encoding="utf8")
all_lines = file.readlines()
long_str = ""
for line in all_lines:
    long_str = long_str + line.strip()
word = ""
for character in long_str:
    if character != " ":
        word = word + character 
        if word in defined_words:
            print(word)
            word == ""




