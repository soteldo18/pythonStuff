try:

	import cPickle as pickle

except ImportError:

	print("importe pickle en vez de cpickle")
	import pickle


animales= ["piton","mono","camello"]

with open("data.pickle","wb") as fichero:
	pickle.dump(animales,fichero,2)
	
	fichero.close()


with open("data.pickle","rb") as fichero:
	animales2=pickle.load(fichero)

print(animales2)

