expected_char = {}
defined_words = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG","PROCS":"PROCS","ROBOT_R":"ROB","VARS":"VARS","assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", "turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID","jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP"}
token_lst = []
file_name= input("Ingrese el nombre del archivo: ")
file = open("ExampleCodeLYM.txt", encoding="utf8")
all_lines = file.readlines()
long_str = ""
for line in all_lines:
    long_str = long_str + line.strip()
word = ""
for character in long_str:
    if character != " ":
        if character == "[":
            defined_words[word] = "PROCID(" + word + ")" 
            token_lst.append(defined_words[word])
            long_str = long_str[:1]
            word = ""
        if character == ",":
            defined_words[word] = "VARID(" + word + ")"
            token_lst.append(defined_words[word])
            long_str = long_str[:1]
            word = ""
        else:
            word = word + character
            long_str = long_str[:1]
            if word in defined_words:
                token_lst.append(defined_words[word])
                word = ""
print(token_lst)

def defined_keep(word:str):
    token_lst.append(defined_words[word])
    long_str = long_str[:1]
    word = ""
    return word 




