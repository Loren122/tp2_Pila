from pila import Pila
# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombres películas estrenadas en el año 2014;

# b. indicar cuántas películas se estrenaron en el año 2018;

# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

class Pelicula:
    
    def __init__(self, name, studio, year):
        
        self.name = name
        self.studio = studio
        self.year = year
        
stack = Pila()

stack.push(Pelicula("Relatos Salvajes","El Deseo S.A",2014))
stack.push(Pelicula("El Sorprendente Hombre Araña 2","Sony Pictures",2014))
stack.push(Pelicula("Los increíbles 2","Walt Disney Pictures",2018))
stack.push(Pelicula("Jurassic World: el reino caído","Perfect World Pictures",2018))
stack.push(Pelicula("Deadpool","Marvel Studios",2016))
stack.push(Pelicula("Doctor Strange: hechicero supremo","Marvel Studios",2016))

def Pelis(stack):

    pelis = 0

    for i in range(stack.size()):
        if stack.on_top().year == 2014:
            print(f"{stack.on_top().name} fue estrenada en {stack.on_top().year}")
        
        if stack.on_top().year == 2018:
            pelis += 1
            
        if stack.on_top().year == 2016 and stack.on_top().studio == "Marvel Studios":
            print(f"{stack.on_top().name} fue una pelicula de {stack.on_top().studio} estrenada en 2016")
            
        stack.pop()
        
    print(f"La pila tiene {pelis} peliculas estrenadas en 2018")
    
Pelis(stack)