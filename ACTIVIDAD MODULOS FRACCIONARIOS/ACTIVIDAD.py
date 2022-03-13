def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a

def fracc(a, b):
    num= int(a/mcd(a,b))
    den= int(b/mcd(a,b))
    
    if a==1:
        return b
    
    
    return str(num)+"/"+str(den)
    fracc()

def suma():
    n1=int(input("Ingrese numerador a: "))
    n2=int(input("Ingrese numerador c: ")) 
    d1=int(input("Ingrese denominador b: ")) 
    d2=int(input("Ingrese denominador d: ")) 
    mult = n1*d2
    mult2 = n2*d1
    mult3 = d1*d2
    print(mult + mult2,'/',mult3)    
    suma()



    
                                                                
def resta():
    n1=int(input("Ingrese numerador a: "))
    n2=int(input("Ingrese numerador c: ")) 
    d1=int(input("Ingrese denominador b: ")) 
    d2=int(input("Ingrese denominador d: ")) 
    
    mult = n1*d2
    mult2 = n2*d1
    mult3 = d1*d2
    
    print(mult - mult2,'/',mult3)
    resta()




    
                                                                
def multiplicacion():
    
    n1=int(input("Ingrese numerador a: "))
    n2=int(input("Ingrese numerador c: ")) 
    d1=int(input("Ingrese denominador b: ")) 
    d2=int(input("Ingrese denominador d: ")) 
    
    mult = n1*n2
    mult2 = d1*d2
    
    print(mult ,'/',mult2)
    multiplicacion()




     
                                                                
def division():   
    n1=int(input("Ingrese numerador a: "))
    n2=int(input("Ingrese numerador c: ")) 
    d1=int(input("Ingrese denominador b: ")) 
    d2=int(input("Ingrese denominador d: ")) 
    
    mult = n1*d2
    mult3 = d1*d2
    print(mult,'/',mult3)
    
    if d1==0:
        return "No se puede dividir por 0"
    if d2==0:
        return "No se puede dividir por 0"

    division()



