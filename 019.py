
try :
    Pol = int(input("enter llinder de Pol·lucio "))
    Med = int(input("enter la mediana en 30 dias "))

    def Seq (Pol: int , Med : int) -> int :
        n = 0 
        while Pol != 0 :
        
            if Pol > Med :
                n += 1
        
            Pol = int(input("enter llinder de Pol·lucio"))

        return n 



    print (Seq(Pol,Med) , " Esta sobre del media")
except TypeError and ValueError :
    print("you can enter just numbers without decimal")