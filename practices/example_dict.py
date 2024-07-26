persona1={
    "name":"sebastian",
    "age":17
}
persona2={
    "name":"mama",
    "age":41
}
persona3={
    "name":"papa",
    "age":43
}
persona4={
    "name":"hermano",
    "age":11,
    
}
persona5={
    "name":"hermano",
    "age":13
}
myFamily={
    "mama":persona2,
    "papa":persona3,
    "hermano_mediano":persona5,
    "hermano_menor":persona4,
    "yo":persona1
}
for x, obj in myFamily.items():
    print(x)
    for y in obj:
        print(y+":",obj[y])
