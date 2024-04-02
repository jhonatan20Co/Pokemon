import random
import time 
import numpy as np
import sys 


#imprimir con retraso 

def imprimir_retraso(s):
    #imprime una letra a la vez
    for c in s: #pasa por cada letra para que se vea lento 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_salud='=========='):
        #guardar variables como atributos 
        self.nombre = nombre
        self.tipos = tipos 
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_salud = puntos_salud
        self.barras = 20 


    def impresa(self,Pokemon2):
        #imprime informacion de lucha
        print("-Batalla Pokemon-")
        print(f"\n{self.nombre}")
        print("tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque, self.defensa])))
        print("\nVS")

        print(f"\n{Pokemon2.nombre}")
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("defensa/", Pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([Pokemon2.ataque, Pokemon2.defensa])))
        time.sleep(2)

    def ventaja(self,Pokemon2):
        version = ['fuego','agua','planta']
        for i,k in enumerate(version):

            if self.tipos == k:
                #misma clase
                if Pokemon2.tipos == k:
                    cadena_1ata = '\n...'
                    cadena_2ata = '\n...'
                

                # pokemon2 es Fuerte
                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1ata = '\n...'
                    cadena_2ata = '\n...'

                # Pokemon2 es debil 
                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    cadena_1ata = '\n...'
                    cadena_2ata = '\n...'

            return cadena_1ata, cadena_2ata
        
    def turn (self, Pokemon2, cadena_1ata, cadena_2ata):
        #actualizacion de los datos pokemon1 1 2
        while (self.barras>0) and (Pokemon2.barras>0):

            #imprime puntos de salud
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_salud}\n")


            #Pokemon 1
            print(f"Adelante {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.",x)
            index = int(input('Elige un movimineto: '))
            imprimir_retraso(f"\n{self.nombre} uso {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_retraso(cadena_1ata)

            #determinar el daño
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_salud = ""

            # agregar barras adicionales mas defensa
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_salud +="="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_salud}\n")
            time.sleep(.5)
            

            #saber si esta debilitado
            if Pokemon2.barras <= 0:
                imprimir_retraso("\n..." + Pokemon2.nombre + "se debilito...")


            #Pokemon 2
            print(f"Adelante {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.",x)
            index = int(input('Elige un movimineto: '))
            imprimir_retraso(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_retraso(cadena_2ata)

            #determinar el daño
            self.barras -= Pokemon2.ataque
            self.puntos_salud = ""

            # agregar barras adicionales mas defensa
            for j in range(int(self.barras+.1*self.defensa)):
                self.puntos_salud +="="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_salud}\n")
            time.sleep(.5)
            

            #saber si esta debilitado
            if self.barras <= 0:
                imprimir_retraso("\n..." + self.nombre + "se debilito...")



    def lucha(self, Pokemon2):
        self.impresa(Pokemon2)
        cadena_1ata, cadena_2ata = self.ventaja(Pokemon2)
        self.turn(Pokemon2, cadena_1ata, cadena_2ata)
        
        imprimir_retraso(f"\nEl oponente perdio y ganaste .\n")


if __name__ == '__main__':

 Pikachu = Pokemon('Pikachu', 'fuego',['Impactrueno','Rayo','Ataque Rápido','Placaje'], {'ataque':10, 'defensa':9})
 Bulbasaur = Pokemon('Bulbasaur', 'planta',['Látigo Cepa','Drenadoras','Placaje','Somnífero'], {'ataque':7, 'defensa':15})
 Charmander = Pokemon('charmander', 'fuego',['Lanzallamas','Gruñido','Arañazo','Ascuas'], {'ataque':12, 'defensa':8})
 Caterpie = Pokemon('carterpie', 'agua',['placaje','tacleada','drenadoras','supersonico'], {'ataque':13, 'defensa':5})
 pidgeotto = Pokemon('pidgeotto', 'agua',['picotazo','remolino','Tornado','Ataque rapido'], {'ataque':11, 'defensa':11})
 Squirtle = Pokemon('Squirtle', 'agua',['pistola agua','burbuja','placaje','Ataque rapido'], {'ataque':8, 'defensa':13})
 Raticate = Pokemon('Raticate', 'fuego',['hipercolmillo','golpe cabeza','placaje','Ataque rapido'], {'ataque':15, 'defensa':7})
 muk = Pokemon('muk', 'agua',['lodo','bomba lodo','infortunio','Ataque acido'], {'ataque':8, 'defensa':12})
 


 if __name__ == '__main__':
    pokemones_disponibles = {
        'Pikachu': Pikachu,
        'Bulbasaur': Bulbasaur,
        'Charmander': Charmander,
        'carterpie': Caterpie,
        'pidgeotto': pidgeotto,
        'Squirtle': Squirtle,
        'Raticate': Raticate,

    }

    while True:
        print("Pokémon disponibles:")
        for nombre in pokemones_disponibles.keys():
            print(f"- {nombre}")

        nombre_pokemon_elegido = input("\nElige un Pokémon para luchar (o 'salir' para terminar): ")
        if nombre_pokemon_elegido.lower() == 'salir':
            break

        pokemon_elegido = pokemones_disponibles.get(nombre_pokemon_elegido)
        if pokemon_elegido:
            # Seleccionar un oponente aleatorio
            oponente = random.choice(list(pokemones_disponibles.values()))
            while oponente == pokemon_elegido:
                oponente = random.choice(list(pokemones_disponibles.values()))

            # Iniciar la batalla
            pokemon_elegido.lucha(oponente)
        else:
            print("Pokémon no encontrado. Por favor, elige uno de los Pokémon disponibles.")

            