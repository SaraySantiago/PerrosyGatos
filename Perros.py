#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class perro:

    __name = None 
    __hambre = True
    __sleepy = False
    
    def __init__(self, aname = "dog") -> None:
       self. __name = aname 
       self.PedirComida()
        
    def __str__(self) -> str:
        answ = f"me llamo {self.__name}"
        return answ 
    
    def comer (self):
      self.__hambre = False
      self.__sleepy = True
       
    def dormir (self):
        print(f"{self.__name}: zzzzzzzzz")
        self.__sleepy = False 
        self.__hambre = True
    
    def PedirComida (self):
        if self.__hambre:
            print(f"{self.__name}: dame comida porfi")
        else:
            print(f"{self.__name}: No tengo hambre")

    def jugar(self):
        if not self.__sleepy:
            print(f"{self}: Genial, vamos a jugar")
        else: 
            self.dog()
            self.PedirComida()
    def dog(self):
        print("woof woof")

   
    
    
    
    
    

if __name__ == "__main__":
      
    # p0 = perro()
    # # print(p0)
    # p0.pedirComida()
    # p0.comer()
    # p0.pedirComida()
        
    p1 = perro("Lady")
    # print(p1)
    p1.PedirComida()
    p1.comer()    
    p1.PedirComida()    
    p1.jugar()
    p1.dormir()
    p1.jugar()