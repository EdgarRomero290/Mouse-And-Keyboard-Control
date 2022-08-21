from pynput.mouse import Listener

#Funcion para identificar la posicion del mouse
def writetoFile(x,y):
    print('Posicion del mouse {0}'.format((x,y)))

with Listener(on_move=writetoFile) as l:
    l.join()