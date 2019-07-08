try:

	import cPickle as pickle

except ImportError:

	print("importe pickle en vez de cpickle")
	import pickle


animales= ["piton","mono","camello"]
lenguajes=["python","java","perl"]

with open("data.pickle","wb") as fichero:
	pickle.dump(animales,fichero,2)
	pickle.dump(lenguajes,fichero,2)
	fichero.close()


with open("data.pickle","rb") as fichero:
	animales2=pickle.load(fichero)
	lenguajes2=pickle.load(fichero)
	

print(animales2)
print(lenguajes2)

