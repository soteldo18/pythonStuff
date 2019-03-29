"""x=[2,3,34,12,543,123,12341,123]
for y in x: pass
   # print(y)

d = {"a": 1, "b": 2, "c": 3}

for key,value in d.items():

    print(key," : ",value)"""
"""diccionario={}
entrada=""
while True:
    llave=input("Introduzca llave:\n")
    if llave!="exit":
        valor=input("Introduzca valor:\n")
        if valor!="exit":
            diccionario[llave]=valor
        else:
            break
    else:
        break
print(diccionario)"""


"""#Ejemplo de como desempaquetar variables de un diccionario
from operator import itemgetter,attrgetter
people = [{'name':'chandan','age':20,'salary':2000},
{'name':'chetan','age':18,'salary':5000},
{'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)
print(people)

list_of_tuples = [(1,2), (3,4), (5,0)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples)
list_of_tuples.sort(key=itemgetter(0))
print(list_of_tuples)
"""
a = list(range(10))
print(a)
del a[::1]
# a = [1, 3, 5, 7, 9]
#del a[-1]
# a = [1, 3, 5, 7]
#del a[:]
# a = []

print(a)
