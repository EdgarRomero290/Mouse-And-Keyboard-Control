from pynput.keyboard import Controller

#Funcion para escribir en pantalla
def controlKeyboard():
    keyboard= Controller()
    keyboard.type("Hello World")

controlKeyboard()



