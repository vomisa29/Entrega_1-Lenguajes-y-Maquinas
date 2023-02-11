"""
***********************************************************************************************************************************************************
DEFINICIONES DE DICCIONARIOS
***********************************************************************************************************************************************************
"""

defined_words = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":"ROB","VARS":"VARS"}
defined_basics = {"assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}
token_lst = []

"""
***********************************************************************************************************************************************************
DEFINICIONES DE FUNCIONES
***********************************************************************************************************************************************************
"""

def program_start(defined_words:dict, defined_basics:dict, defined_funcs:dict):
    file = open("ExampleCodeLYM.txt", encoding="utf8")
    all_lines = file.readlines()
    global long_str
    long_str = ""
    for line in all_lines:
        long_str = long_str + line.strip()
    normal_reader(defined_words,defined_basics,defined_funcs,token_lst)

def dict_check(word:str):
    if word in defined_words:
            token_lst.append(defined_words[word])
            defined_funcs[word]

def variables():
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == ";":
            var_list = word.split(",")
            token_lst.extend(var_list)
            normal_reader()
            break

def variables_proc():
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "|":
            var_list = word.split(",")
            token_lst.extend(var_list)
            break
    
def procedures():
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "[":
            token_lst.append("PROCID("+word+")")
            inside_proced(long_str)
            break

def inside_proced(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list):
    word = ""
    scuareCounter =0
    for character in long_str:
        word = word + character
        if character == "|" and len(word) > 1:
            raise Exception("Hay un procedimiento mal definido pero no se cual jijijiji")
        elif character == "|" and len(word) == 1:
            variables_proc(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list)
        if character == "[":
            scuareCounter += 1
        if character == "]":
            scuareCounter -= 1 
            if scuareCounter == 0:
                procedures(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list)
                break
        
def rob(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list):
    word = ""
    if len(token_lst) >0:
        if token_lst[0] != "ROB":
            raise Exception("Este no es un codigo ROBOT_R")

def normal_reader(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list): 
    word = ""
    for character in long_str:
        long_str = long_str[1:] 
        word = word + character
        if word in defined_words:
            token_lst.append(defined_words[word])
            defined_funcs[word](defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list)
            break 

#Definicion de diccionario de funciones 

defined_funcs = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":rob,"VARS":variables,"assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}

#Start 
params = [defined_basics,defined_funcs,defined_basics, token_lst]
program_start(params)




