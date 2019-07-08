import shelve

filename="data2.dat"

d=shelve.open(filename)

animales=["perico","pato","perro"]
lenguajes=["python","java","c++"]

archivo=shelve.open(filename)

archivo["animales"]=animales
archivo["lenguajes"]=lenguajes

print(archivo["lenguajes"])
print(archivo["animales"])

archivo.close()


