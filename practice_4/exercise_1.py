# Pedimos un color, este es el inicio de todo el programa. Hacemos el texto a
# letras que solo sean minúsculas para no tener que condicionar de manera diferente
# ya que "Verde" sería distinto a "verde" y así sucesivamente. Con esto, no importa
# lo que el usuario escriba: verdE, Verde, VERDE, veRDE; al final todo ese texto por
# el comando ".lower()" se convertirá a un: "verde"
color: str = input("Type a traffic light color. We will tell you what to do: ").lower()

# Condicionamos lo que vamos a imprimir a cada tipo de color que nos pasen. En base
# a las instrucciones dadas, lo que deberíamos hacer es imprimir un mensaje diferente
# por cada color del semáforo

# Si el color que escribió el usuario ya convertido a .lower() es igual a 
# "green" o igual a "verde", se le dirá un mensaje, este puede ser lo qye
# queramos, no está especificado por la profe. De misma manera colocamos una
# condición para cuando no sea así con la palabra elif.
if color == "green" or color == "verde":
    print(f"Color is: {color}, moving forward!")
elif color == "yellow" or color == "amarillo":
    print(f"Color is: {color}, stoping!")
elif color == "red" or color == "rojo":
    print(f"Color is: {color}, we have stopped!")
# La palabra else se ejecuta cuando ninguno de los casos anteriores de if o elif
# se cumpla. En este caso si el texto no fue ninguno de los colores básicos,
# diremos que hubo un error, o daremos el mensaje que queramos
else:
    print("Error!")
