x= "Hola putos"
insultos=["puto","mierda","triple hioputa", "carajo", "perro", "idiota"]
table=str.maketrans("aeiou", "#####")
for insulto in insultos:
    censurado=insulto.translate(table)
    x=x.replace(insulto, censurado)
print(x)