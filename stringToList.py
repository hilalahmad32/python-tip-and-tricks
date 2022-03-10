import ast

def changeString(string):
    return ast.literal_eval(string)


string="[[1,2,3,4] ,[4,5,6]]"

list=changeString(string)
print(list) 