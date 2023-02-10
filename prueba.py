expected_char = {}
defined_words = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":"ROB","VARS":"VARS"}
defined_basics = {"assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}
global long_str
global token_lst
global defined_funcs
token_lst = []
file_name= input("Ingrese el nombre del archivo: ")
file = open("ExampleCodeLYM.txt", encoding="utf8")
all_lines = file.readlines()
long_str = ""
for line in all_lines:
    long_str = long_str + line.strip()

def dict_check(word:str):
    if word in defined_words:
            token_lst.append(defined_words[word])
            defined_funcs[word]

def variables(long_str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == ";":
            var_list = word.split(",")
            token_lst.extend(var_list)
            normal_reader(long_str)
            break

def variables_proc(long_str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "|":
            var_list = word.split(",")
            token_lst.extend(var_list)
            break
    

def procedures(long_str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "[":
            token_lst.append("PROCID("+word+")")
            inside_proced(long_str)
            break



def inside_proced(long_str):
    word = ""
    scuareCounter =0
    for character in long_str:
        word = word + character
        if character == "|" and len(word) > 1:
            raise Exception("Hay un procedimiento mal definido pero no se cual jijijiji")
        elif character == "|" and len(word) == 1:
            variables_proc(long_str)
        if character == "[":
            scuareCounter += 1
        if character == "]":
            scuareCounter -= 1 
            if scuareCounter == 0:
                procedures(long_str)
                break
        
def rob():
    word = ""
    if len(token_lst) >0:
        if token_lst[0] != "ROB":
            raise Exception("Este no es un codigo ROBOT_R")

def normal_reader(long_str): 
    word = ""
    for character in long_str:
        long_str = long_str[1:] 
        word = word + character
        if word in defined_words:
            token_lst.append(defined_words[word])
            defined_funcs[word](";")
            break 
defined_funcs = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":rob(),"VARS":variables(long_str),"assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}

normal_reader(long_str)





