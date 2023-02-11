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

def program_start(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list):
    file = open("ExampleCodeLYM.txt", encoding="utf8")
    all_lines = file.readlines()
    long_str = ""
    for line in all_lines:
        long_str = long_str + line.strip()
    string_list = long_str.split(" ")
    long_str = ""
    for line in string_list:
        long_str = long_str + line
    normal_reader(defined_words,defined_basics,defined_funcs,token_lst,long_str)

def dict_check(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str,word:str):
    if word in defined_words:
            token_lst.append(defined_words[word])
            defined_funcs[word]

def variables(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == ";":
            word = word[:-1]
            var_list = word.split(",")
            token_lst.extend(var_list)
            normal_reader(defined_words, defined_basics, defined_funcs,token_lst,long_str)
            break 

def variables_proc(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "|":
            word = word[:-1]
            var_list = word.split(",")
            token_lst.extend(var_list)
    
def procedures(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character 
        if character == "[":
            word = word[:-1]
            if word == "":
                token_lst.append("INSTRUCTION_BLOCK()")
            else:
                token_lst.append("PROCID("+word+")")
            scuareCounter = 1
            inside_proced(defined_words, defined_basics, defined_funcs,token_lst,long_str, scuareCounter, word)
            break 

def inside_proced(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str, scuareCounter:int, kword:str):
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character
        if character == "|":
            pass
            #word = word[:-1]
            #variables_proc(defined_words, defined_basics, defined_funcs,token_lst,long_str)
        if character == "[":
            word = word[:-1]
            scuareCounter += 1
        if character == "]":
            word = word[:-1]
            scuareCounter -= 1 
            if scuareCounter == 0:
                token_lst.append("PROCBDY" + kword + "("+word+")")
                procedures(defined_words, defined_basics, defined_funcs,token_lst,long_str)
                break
        
def rob(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str):
    if len(token_lst) >0:
        if token_lst[0] != "ROB":
            raise Exception("Este no es un codigo ROBOT_R")
    normal_reader(defined_words,defined_basics,defined_funcs,token_lst,long_str)

def normal_reader(defined_words:dict, defined_basics:dict, defined_funcs:dict,token_lst:list,long_str:str): 
    word = ""
    for character in long_str:
        long_str = long_str[1:]
        word = word + character
        if word == "ROBOT_R":
            token_lst.append(defined_words[word])
            rob(defined_words, defined_basics, defined_funcs,token_lst,long_str)
            word = ""
            break
        elif word == "VARS":
            token_lst.append(defined_words[word])
            variables(defined_words, defined_basics, defined_funcs,token_lst,long_str)
            word = ""
            break
        elif word == "PROCS":
            token_lst.append(defined_words[word])
            procedures(defined_words, defined_basics, defined_funcs,token_lst,long_str)
            word = ""
            break


#Definicion de diccionario de funciones 

defined_funcs = {"M:":"M", "R:":"R","C:":"C","B:":"B","c:":"c","b:":"b","P:":"P","J(":"funcJ","G(":"funcG",
"PROCS":"PROCS","ROBOT_R":rob,"VARS":variables,"assignTo:":"procAST","goto:":"procGOT", "move:":"procMOV", 
"turn:":"procTUR", "face:":"procFAC", "put:":"procPUT", "pick:":"procPIC", "moveToThe:":"procMTT","moveInDir:":"procMID",
"jumpToThe:":"procJTT","jumpInDir:":"procJID", "nop":"procNOP", "while":"while", "repeat":"repeat"}

#Start 
program_start(defined_words, defined_basics, defined_funcs,token_lst)

def recursive_experiment(defined_words, defined_basics, defined_funcs,token_lst):
    file = open("ExampleCodeLYM.txt", encoding="utf8")
    all_lines = file.readlines()
    long_str = ""
    for line in all_lines:
        long_str = long_str + line.strip()
    return token_lst
print("Lista de Tokens del Programa: ")
print(token_lst)