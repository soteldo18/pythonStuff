##EJEMPLO DE PROGRAMACION FUNCIONAL Y EJECUTAR UNA FUNCION DENTRO DE OTRA
def hola_multilang(entrada):

    def lang_frances():
        print("Salut")
    
    def lang_ingles():
        print("Hello")
    
    def lang_español():
        print("hola")

    tipo_lenguaje={
        "es":lang_español,
        "en":lang_ingles,
        "fr":lang_frances
    }
    return tipo_lenguaje[entrada]

hola_multilang("es")()

f=hola_multilang("fr")
f()

##USO DE LA FUNCION FILTER

def es_par(n):
    return (n%2.0==0)


l=[1,2,3,4,5,6,7,89,12,33,45,67]
l2=list(filter(es_par,l))

#####USO DE LA FUNCION REDUCE
from functools import reduce

def sumar(x,y):
    return x+y

l=[1,2,3,4,5,6,7,8,9]
l2=reduce(sumar,l)

print(l2)

######comprension de listas

m=["a","b"]
n=[s*v for s in m
       for v in l
       if v>0]

print(n)

###########DECORADORES funcion que pasa otra funcion
def imp(saludo):
    print("hola")

def decorador(funcion):
    def nueva(*args):
        print("el nombre de la funcion pasada es:",funcion.__name__)
        entrada=funcion(*args)
        return entrada
    return nueva

decorador(imp)("hola")













