import re
mo=re.match("http://(.+)\.net","http://mundogeek.net")
try:
    print(mo.group(1))
except (IndexError,IndentationError):
    print("Error de indice")
