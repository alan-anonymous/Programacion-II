from fraccion import Fraccion
import os

cicloMayor = True
while (cicloMayor==True):
     print ("First fraction:")
     num = int(input("Enter the numerator:  "))
     den = int(input("Enter the denominator:  "))
     ciclo = True
     while (ciclo==True):
          if (den==0):
                    print ("The denominator admitted is invalid")
                    den = int(input("Enter again the denominator:  "))
          else:
               ciclo = False     
     fraccion1 = Fraccion(num,den)
     print("\nSecond fraction:")
     num = int(input("Enter the numerator:  "))
     den = int(input("Enter the denominator:  "))
     ciclo = True
     while (ciclo==True):
          if (den==0):
                    print ("The denominator admitted is invalid.")
                    den = int(input("Enter again the denominator:  "))
          else:
               ciclo = False    
     fraccion2 = Fraccion(num,den)
     print("-----------")
     fraccion1.mostrar()
     fraccion2.mostrar()
     print("-----------")
     ciclo = True
     while (ciclo == True):
          print (" 1. Add the fractions\n 2. Subtract the fractions\n 3. Multiply the fractions\n 4. Divide the fractions")
          option = str(input()) 
          if (option == "1"):
               resultadoSuma  =  fraccion1.sumar (fraccion2)
               print ("The addition is: ")
               resultadoSuma.mostrar ()
               ciclo = False
          elif (option == "2"):
               resultadoResta  =  fraccion1.restar (fraccion2)
               print ("The subtraction is: ")
               resultadoResta.mostrar ()
               ciclo = False
          elif (option == "3"):
               resultadoMult  =  fraccion1.multiplicar(fraccion2)
               print ("The multiplication is: ")
               resultadoMult.mostrar ()
               ciclo = False
          elif (option == "4"):
               resultadoDiv  =  fraccion1.dividir (fraccion2)
               print ("The division is: ")
               resultadoDiv.mostrar ()
               ciclo = False
          else:
               print("The option admitted isn't in the main.\nPlease enter again it.")
               ciclo = True
               
     continuar = str(input("\nDo you wish to continue operating? yes/no\n"))
     if (continuar == "yes"):
          os.system ("cls")
          cicloMayor = True
     else:
          cicloMayor = False
          
