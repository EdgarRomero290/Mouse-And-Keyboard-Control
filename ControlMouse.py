from pynput.mouse import Controller

#Funcion para mover el mouse a coordenadas especificas
def controlMouse():
    mouse= Controller()
    mouse.position=[10,20]  #[derecha a izquierda, arriba a abajo]
    
controlMouse()


