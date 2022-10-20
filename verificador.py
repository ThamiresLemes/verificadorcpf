


cpf = 15969985719
cpflista = list(str(cpf))
cpflistaint = list(map(int,cpflista))
listamultiplicar = [10,9,8,7,6,5,4,3,2]
resultadomultiplicar = list(map(lambda x,y:x*y, cpflistaint,listamultiplicar))
somadamultiplicacao = sum(resultadomultiplicar)
calculoresto = somadamultiplicacao % 11
primeirodigitoverificador = 11 - calculoresto

listamultiplicar2 = [11,10,9,8,7,6,5,4,3,2]
resultadomultiplicar2 = list(map(lambda x,y:x*y, cpflistaint,listamultiplicar2))
somadamultiplicacao2 = sum(resultadomultiplicar2)
calculoresto2 = somadamultiplicacao2 % 11
segundodigitoverificador = 11 - calculoresto2

print(primeirodigitoverificador)
print(segundodigitoverificador)

if calculoresto == 0 or calculoresto == 1:
    if cpflistaint[9] == 0:
        print("Primeiro digito igual a 0")
    
    else:
        print("CPF invalido, digito nao e 0")



elif primeirodigitoverificador == 0 or primeirodigitoverificador >0 and primeirodigitoverificador < 10:
    if cpflistaint[9] == primeirodigitoverificador:
        print ("Primeiro digito igual a ele mesmo")
    
    else:
        print ("cpf invalido, digito nao e ele mesmo.")
        
        
elif primeirodigitoverificador ==10 or primeirodigitoverificador>10 :
        if cpflistaint[9] ==0:
            print ("Primeiro digito igual a 0")
            
        else:
            print("cpf invalido, digito nao e 00")

else:
    print("testando")
    
    
if calculoresto2 == 0 or calculoresto2 == 1:
    if cpflistaint[10] == 0:
        print("Segundo digito igual a 0")
    
    else:
        print("CPF invalido, segundo digito nao e 0")



elif segundodigitoverificador == 0 or segundodigitoverificador > 0 and segundodigitoverificador < 10:
    if cpflistaint[10] == segundodigitoverificador:
        print ("Segundo digito igual a ele mesmo ")
    
    else:
        print ("cpf invalido, segundo digito nao e ele mesmo.")
        
        
elif segundodigitoverificador ==10 or segundodigitoverificador >10 :
        if cpflistaint[10] ==0:
            print ("Segundo digito igual a 0")
            
        else:
            print("cpf invalido, segundo digito nao e 00")

else:
    print("testando")