class Personaje:
    def __init__(self, Vida, Ataque, Defensa):
        self.__Vida = 0
        self.__Ataque = Ataque
        self.__Defensa = Defensa
        self.Set_Vida(Vida)
    # Getter de Vida
    def Get_Vida(self):
        return self.__Vida
    # Setter de Vida (Validacion para el 0-100)
    def Set_Vida(self, Nueva_Vida):
        if 0 <= Nueva_Vida <= 100:
            self.__Vida = Nueva_Vida
        else:
            print("La Vida debe estar entre 0 y 100")
    def Get_Ataque(self):
        return self.__Ataque
    def Get_Defensa(self):
        return self.__Defensa
    # Metodo de Ataque
    def Atacar(self, Objetivo):
        Daño = self.__Ataque - Objetivo.Get_Defensa()
        if Daño < 0:
            Daño = 0
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        Objetivo.Set_Vida(max(Nueva_Vida, 0))
        print(f"{self.__class__.__name__} ataca causando {Daño} de daño.")
# Guerrero
class Guerrero(Personaje):
    def Atacar(self, Objetivo):
        Daño = self.Get_Ataque() * 1.2 - Objetivo.Get_Defensa()
        if Daño < 0:
            Daño = 0
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        Objetivo.Set_Vida(max(int(Nueva_Vida), 0))
        print(f"Guerrero usa fuerza bruta!, hace {int(Daño)} de daño.")
# Mago
class Mago(Personaje):
    def Atacar(self, Objetivo):
        Daño = self.Get_Ataque()  # Calculo para Ignorar Def
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        Objetivo.Set_Vida(max(int(Nueva_Vida), 0))
        print(f"Mago lanza hechizo!, Hace {int(Daño)} de daño.")
# Arquero
class Arquero(Personaje):
    def Atacar(self, Objetivo):
        if self.Get_Ataque() > Objetivo.Get_Defensa():
            Daño = self.Get_Ataque() * 2
            Critico = True
        else:
            Daño = self.Get_Ataque() - Objetivo.Get_Defensa()
            Critico = False
        if Daño < 0:
            Daño = 0
        Nueva_Vida = Objetivo.Get_Vida() - Daño
        Objetivo.Set_Vida(max(int(Nueva_Vida), 0))
        print(f"Arquero dispara flecha e inflige {int(Daño)} de daño.")
        if Critico:
            print("¡Ataque crítico del Arquero!")



# Simulación de batalla
def Batalla(Personaje1, Personaje2):
    Turno = 1
    while Personaje1.Get_Vida() > 0 and Personaje2.Get_Vida() > 0:
        print(f"\n- - - Turno {Turno} - - -")
        Personaje1.Atacar(Personaje2)
        print(f"Vida restante de {Personaje2.__class__.__name__}: {Personaje2.Get_Vida()}")
        if Personaje2.Get_Vida() <= 0:
            print(f"\n{Personaje1.__class__.__name__} ha ganado!")
            break
        Personaje2.Atacar(Personaje1)
        print(f"Vida restante de {Personaje1.__class__.__name__}: {Personaje1.Get_Vida()}")
        if Personaje1.Get_Vida() <= 0:
            print(f"\n{Personaje2.__class__.__name__} ha ganado!")
            break
        Turno += 1
# Ejemplo de ejecución
Guerrero1 = Guerrero(100, 30, 20)
Mago1 = Mago(80, 40, 10)
Batalla(Guerrero1, Mago1)