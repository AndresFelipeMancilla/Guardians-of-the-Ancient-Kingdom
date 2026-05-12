from abc import ABC, abstractmethod
# Clase Abstracta
class Personaje(ABC):
    # Constructor
    def __init__(self, Vida, Ataque, Defensa):
        # Atributos Privados
        self.__Vida = 0
        self.__Ataque = Ataque
        self.__Defensa = Defensa
        # Uso del setter para validar la vida
        self.Set_Vida(Vida)
    # Getter de Vida
    def Get_Vida(self):
        return self.__Vida
    # Setter de Vida
    def Set_Vida(self, Nueva_Vida):
        # Validacion de vida entre 0 y 100
        if 0 <= Nueva_Vida <= 100:
            self.__Vida = Nueva_Vida
        else:
            print("La Vida debe estar entre 0 y 100")
    # Getter de Ataque
    def Get_Ataque(self):
        return self.__Ataque
    # Getter de Defensa
    def Get_Defensa(self):
        return self.__Defensa
    # Metodo Abstracto
    @abstractmethod
    def Atacar(self, Objetivo):
        pass
# Clase Guerrero
class Guerrero(Personaje):
    # Metodo de Ataque del Guerrero
    def Atacar(self, Objetivo):
        # Hace 20% Daño Extra
        Daño = int(self.Get_Ataque() * 1.2) - Objetivo.Get_Defensa()
        # Evita Daño Negativo
        if Daño < 0:
            Daño = 0
        # Calcular Nueva Vida
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        # Actualiza Vida
        Objetivo.Set_Vida(max(Nueva_Vida, 0))
        # Mensaje de Ataque
        print(f"\nGuerrero usa fuerza bruta e inflige {Daño} de daño.")
# Clase Mago
class Mago(Personaje):
    # Metodo de Ataque del Mago
    def Atacar(self, Objetivo):
        # Ignora Defensa
        Daño = self.Get_Ataque()
        # Calcular Nueva Vida
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        # Actualiza Vida
        Objetivo.Set_Vida(max(Nueva_Vida, 0))
        # Mensaje de Ataque
        print(f"\nMago lanza hechizo e inflige {Daño} de daño.")
# Clase Arquero
class Arquero(Personaje):
    # Metodo de Ataque del Arquero
    def Atacar(self, Objetivo):
        # Verifica Ataque critico
        if self.Get_Ataque() > Objetivo.Get_Defensa():
            # Doble Daño
            Daño = self.Get_Ataque() * 2
            Critico = True
        else:
            Daño = self.Get_Ataque() - Objetivo.Get_Defensa()
            Critico = False
        # Evita Daño Negativo
        if Daño < 0:
            Daño = 0
        # Calcular Nueva Vida
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        # Actualiza Vida
        Objetivo.Set_Vida(max(Nueva_Vida, 0))
        # Mensaje de Ataque
        print(f"\nArquero dispara flecha e inflige {Daño} de daño.")
        # Mensaje Critico
        if Critico:
            print("¡Ataque critico del Arquero!")
# Menu de Seleccion de Personaje
def Crear_Personaje(Jugador):

    print(f"\nSeleccione el personaje del Jugador {Jugador}")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    Opcion = input("Ingrese una opcion: ")
    # Crear Guerrero
    if Opcion == "1":
        return Guerrero(100, 30, 20)
    # Crear Mago
    elif Opcion == "2":
        return Mago(80, 40, 10)
    # Crear Arquero
    elif Opcion == "3":
        return Arquero(90, 35, 15)
    # Opcion Invalida
    else:
        print("Opcion invalida. Se seleccionara Guerrero por defecto.")
        return Guerrero(100, 30, 20)
# Funcion Para los Enfrentamientos
def Batalla(Personaje1, Personaje2):
    # Contador de Turnos
    Turno = 1
    # Bucle Principal de Batalla
    while Personaje1.Get_Vida() > 0 and Personaje2.Get_Vida() > 0:
        print(f"\n========== TURNO {Turno} ==========")
        # Mostrar Vidas
        print(f"Vida de {Personaje1.__class__.__name__}: {Personaje1.Get_Vida()}")
        print(f"Vida de {Personaje2.__class__.__name__}: {Personaje2.Get_Vida()}")
        # Menu de Acciones
        print("\n1. Atacar")
        print("2. Salir")
        Accion = input("Seleccione una opcion: ")
        # Opcion Atacar
        if Accion == "1":
            # Ataca Jugador 1
            Personaje1.Atacar(Personaje2)
            # Mostrar Vidas Despues del Ataque
            print(f"Vida restante de Jugador 2: {Personaje2.Get_Vida()}")
            # Verificador de Derrota
            if Personaje2.Get_Vida() <= 0:
                print("¡Jugador 1 ha ganado la batalla!")
                break
            # Ataca Jugador 2
            Personaje2.Atacar(Personaje1)
            # Mostrar Vidas Despues del Ataque
            print(f"Vida restante de Jugador 1: {Personaje1.Get_Vida()}")
            # Verificador de Derrota
            if Personaje1.Get_Vida() <= 0:
                print("¡Jugador 2 ha ganado la batalla!")
                break
            # Siguiente Turno
            Turno += 1
        # Opcion Salir
        elif Accion == "2":
            print("\nJuego finalizado.")
            break
        # Opcion Invalida
        else:
            print("\nOpcion invalida.")
# Programa Principal
print("= = = Guardians of the Ancient Kingdom = = =")
# Creador de Personajes
Personaje1 = Crear_Personaje(1)
Personaje2 = Crear_Personaje(2)
# Iniciar Batalla
Batalla(Personaje1, Personaje2)