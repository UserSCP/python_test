import re 
txt= "sentado de bajo de un arbol de mango , "
x=re.sub("\s","()",txt)
print(x)