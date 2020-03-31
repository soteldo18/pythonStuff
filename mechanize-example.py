import mechanize
# la url de la pagina a visitar
url='http://paytechcorp.com/'

def main():
    #crea una instacia del broswer
    b= mechanize.Browser()
    #carga la pagina
    b.open(url)
    #selecciona el formulario
    b.select_form(nr=0)
    
    
    