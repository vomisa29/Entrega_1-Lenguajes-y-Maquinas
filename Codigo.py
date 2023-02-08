expected_char = {}
defined_words = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":"ROB","VARS":"VARS","assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}
token_lst = []
var_lst = []
procs_lst = []
procsBody_lst = []
file_name= input("Ingrese el nombre del archivo: ")
file = open("ExampleCodeLYM.txt", encoding="utf8")
all_lines = file.readlines()
long_str = ""
for line in all_lines:
    long_str = long_str + line.strip()
word = ""
var_centinela = True
scuareCounter = 0
betweenScuare = 0

def defined_keep(word:str):
    token_lst.append(defined_words[word])
    word = ""
    return word 

for character in long_str:

    if character != " ":
        #print(word)
        #print(betweenScuare)

        if character == "[" and scuareCounter == 0:
            betweenScuare += 1
            if word[0] == "]":
                word = word[1:]
            defined_words[word] = "PROC_ID(" + word + ")"
            procs_lst.append(word)
            word = defined_keep(word)
            
            
        elif character == "]":
            betweenScuare -= 1
            scuareCounter = 1
            word = word + character
            defined_words[word] = "PROC_Body(" + word + ")" 
            procsBody_lst.append(word)
            print(word)
            word = defined_keep(word)
            print("1")

        if (character == "," or character == ";") and var_centinela:
            if var_centinela and character != ";":
                defined_words[word] = "VAR_ID(" + word + ")"
                var_lst.append(word)
                word = defined_keep(word)

            elif character == ";" and var_centinela:
                defined_words[word] = "VARID(" + word + ")"
                var_lst.append(word)
                word= defined_keep(word)
                var_centinela = False
                
        else:
            word = word + character
            
            scuareCounter = 0
            if word in defined_words:
                token_lst.append(defined_words[word])
                word = ""
print("\n")
print("Lista de Tokens")
print(token_lst)
print("\n")
print("Lista de Variables")
print(var_lst)
print("\n")
print("Lista de Procedimientos")
print(procs_lst)
print("\n")
print("Lista de Contenido de Procedimientos")
print(procsBody_lst)
print("\n")
print("So, el programa falla con los parentesis anidados (algo del estilo de [ [a] ]).\nFalta corregir eso y agregar un par de procedimientos que no estan en el ejemplo.\nAlso la variable betweenScuare es para contar el estado de los parentesis(+1 para [ , y -1 para ] ). Srry por la falta de creatividad del nombre.\n")



