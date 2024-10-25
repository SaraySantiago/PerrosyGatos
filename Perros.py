#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class perro:

    __name = None 
    __hambre = True
    __sleppy = True
    __fear = False
    __happy = True

    def __init__(self, aname = "firulais") -> None:
     self.__name = aname
     self.ladra()
    
    def ladra(self):
     print (f"{self.__name}: wof wof")
     
    def pegar(self):
        self.__fear = True 
     
    def ataca(self):
        if self.__fear:
            print (f"{self.__name}: mieditoo")
        else:
            print (f"{self.__name}: GRRR")  
    
    def traePelota(self, color=" rojo"):
         return "pelota" + color
   
    def comer (self):
        self.__hambre = False
        
    def dormir(self):
        self.__sleppy = False
    
    def pedirComida (self):
       if self.__hambre:
        self.ladra()
        
    def tocar(self):
        if self.__fear:
            self.ladra()
            self.__fear = False
        else:
            self.__happy = True
            self.pedirComida()   
        
        
        
if __name__ == "__main__":
    
    p0 = perro("sultan")   
    meTrae = p0.traePelota()
    print(meTrae)
    
    meTrae = p0.traePelota (" verde")
    print(meTrae)
    p0.dormir()
    p0.pedirComida()
    p0.comer()
    p0.ataca()
    p0.dormir()