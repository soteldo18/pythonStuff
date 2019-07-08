try:
    number=12/0
    print(number)

except ZeroDivisionError:
    print("operacion erronea")

else:
    print("todo esta bien")

finally:
    print("esto siempre se imprime")

