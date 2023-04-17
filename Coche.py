import time
from Gasolinera import Surtidor

class Coche():

    def __init__(self):
        self.repostado = False

    def repostar(self, surtidor:Surtidor):
        if surtidor.getEnUso() == False:
            inicio=time.time()
            tiempo_a_esperar = surtidor.getTiempo()
            surtidor.setEnUso(True)
            print("Repostando...")
            while time.time()-inicio < tiempo_a_esperar:
                time.sleep(0.5)
            self.repostado = True

    def getRepostado(self):
        return self.repostado
    
if __name__=="__main__":
    coche = Coche()
    surtidor = Surtidor()
    coche.repostar(surtidor)
    print(surtidor.getTiempo())
    print(coche.getRepostado())