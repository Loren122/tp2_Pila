from pila import Pila

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot,
# tomando como posición uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga,
# además indicar la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G


class character:
    
    def __init__(self,name,movies):
        
        self.name = name
        self.movies = movies

def Pila_charger():
    
    stack.push(character("Iron Man", 3))
    stack.push(character("Capitán América", 4))
    stack.push(character("Thor", 4))
    stack.push(character("Hulk", 3))
    stack.push(character("Black Widow", 7))
    stack.push(character("Hawkeye", 4))
    stack.push(character("Spider-Man", 2))
    stack.push(character("Doctor Strange", 2))
    stack.push(character("Black Panther", 2))
    stack.push(character("Ant-Man", 2))
    stack.push(character("Vision", 2))
    stack.push(character("Scarlet Witch", 3))
    stack.push(character("Falcon", 3))
    stack.push(character("War Machine", 4))
    stack.push(character("Winter Soldier", 3))
    stack.push(character("Rocket Raccoon", 5))
    stack.push(character("Groot", 5))
    stack.push(character("Thanos", 3))
    stack.push(character("Loki", 6))
    
stack = Pila()    
aux_5_pelis = Pila()
aux_b_w = Pila()
aux_c_d_g = Pila()

Pila_charger()


def Encontrar(stack):
    
    for i in range(stack.size()):
        if stack.on_top().name == "Rocket Raccoon":
            posrocket = f'{stack.on_top().name}: posición {i + 1}'
        
        elif stack.on_top().name == "Groot":
            posgroot = f'{stack.on_top().name}: posición {i + 1}'
            
        stack.pop()    
          
    return posrocket, posgroot

print(Encontrar(stack))

Pila_charger()

def Mas_5_pelis(stack):    
    
    for i in range(stack.size()):
        per_y_pelis = (f'{stack.on_top().name} en {stack.on_top().movies} películas', )
        if stack.on_top().movies > 5:
            aux_5_pelis.push(per_y_pelis)
        
        stack.pop()  
         
    return aux_5_pelis
    
print(Mas_5_pelis(stack))

Pila_charger()

def Black_w_pelis(stack):
    
    for i in range(stack.size()):
        black_w_pelis = (f'{stack.on_top().name} participó en {stack.on_top().movies} películas', )
        if stack.on_top().name == 'Black Widow':
            aux_b_w.push(black_w_pelis)
          
        stack.pop() 
        
    return aux_b_w

print(Black_w_pelis(stack))

Pila_charger()

def Ini_c_d_g(stack):
    
    
    
    for i in range(stack.size()):
        if stack.on_top().name[0] in ['C','D','G']:
            aux_c_d_g.push(stack.on_top().name)
            
        stack.pop()
        
    return aux_c_d_g

print(Ini_c_d_g(stack))