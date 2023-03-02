color: str = input("Type a traffic light color. We will tell you what to do: ").lower()

if color == "green" or color == "verde":
    print(f"Color is: {color}, moving forward!")
elif color == "yellow" or color == "amarillo":
    print(f"Color is: {color}, stoping!")
elif color == "red" or color == "rojo":
    print(f"Color is: {color}, we have stopped!")
else:
    print("Error!")
