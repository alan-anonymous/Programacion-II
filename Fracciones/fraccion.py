#Inicio
class Fraccion:

     def __init__ (self, numerador, denominador):
          self.numerador = numerador
          self.denominador = denominador

     def mostrar (self):
          print (self.numerador, "/", self.denominador)
          
     def sumar (self, fraccion2):
          resultado = Fraccion(1,1)

          #Metodo mariposa para sumar fracciones
          resultado.numerador = self.numerador * fraccion2.denominador + fraccion2.numerador * self.denominador
          resultado.denominador = self.denominador * fraccion2.denominador
          return resultado

     def restar (self, fraccion2):
          resultado = Fraccion(1,1)

          #Metodo mariposa para restar fracciones
          resultado.numerador = self.numerador * fraccion2.denominador - fraccion2.numerador * self.denominador
          resultado.denominador = self.denominador * fraccion2.denominador
          return resultado

     def multiplicar (self, fraccion2):
          resultado = Fraccion(1,1)

          resultado.numerador = self.numerador * fraccion2.numerador 
          resultado.denominador = self.denominador * fraccion2.denominador
          return resultado     

     def dividir (self, fraccion2):
          resultado = Fraccion(1,1)

          resultado.numerador = self.numerador * fraccion2.denominador 
          resultado.denominador = self.denominador * fraccion2.numerador
          return resultado     
     
