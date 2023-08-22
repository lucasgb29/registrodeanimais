import time
import os
from abc import ABC, abstractmethod

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Animal(ABC):
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    
    @abstractmethod
    def __str__(self):
        pass

class Menu():
    
    @staticmethod
    def menu_fichas(cachorros, gatos, peixes, cavalos, passaros):
        clear_screen()
        print("menu das fichas:")
        print("\n1 - Cachorro")
        print("2 - Gato")
        print("3 - Peixe")
        print("4 - Cavalo")
        print("5 - Pássaro")
        print("Q - Encerrar o programa")
            
            
        opcao= input("\nEscolha uma opção:").strip().upper()

        if opcao== "Q":
            clear_screen()
            print("Encerrando o programa...")

        elif opcao== "1":
            Fichas.ficha("cachorro",cachorros,"cachorro",Adicionar.add_cachorro)    
        elif opcao== "2":
            Fichas.ficha("gato",gatos,"gato",Adicionar.add_gato)    
        elif opcao== "3":
            Fichas.ficha("peixe",peixes,"peixe",Adicionar.add_peixe)    
        elif opcao== "4":
            Fichas.ficha("cavalo",cavalos,"cavalo",Adicionar.add_cavalo)        
        elif opcao== "5":
            Fichas.ficha("passaro",passaros,"passaro",Adicionar.add_passaro)    

        else:
                clear_screen()
                print("Opção inválida. Por favor, escolha uma opção válida.")
                time.sleep(1)
                Menu.menu_fichas(cachorros, gatos, peixes, cavalos, passaros)


class Fichas(Menu):
    @staticmethod
    def ficha(animal, animais,especie, adicionar):
        clear_screen()
        print(f"ficha de cada {especie}:\n")
        for animal in animais:
            print(animal)
            print()
        
        print("\nA - Adicionar")
        print("D - Deletar")
        print("R - Retornar")
        print("Q - Encerrar o programa\n")
                
        opcao = input("\nEscolha uma opção:").strip().upper()

        if opcao== ("R"):
            Menu.menu_fichas(cachorros, gatos, peixes, cavalos, passaros)
                        
        elif opcao== "Q":
            clear_screen()
            print("Encerrando o programa...")
                                          
        elif opcao ==  "D":
            Deletar.deletar_animal(animais,especie)
            Fichas.ficha(animal, animais,especie, adicionar)  
        
        elif opcao == "A":
            adicionar()
            Fichas.ficha(animal, animais,especie, adicionar)
        else:
            clear_screen()
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(1)
            Fichas.ficha(animal, animais,especie, adicionar)
        
          
    

class Adicionar:    
    @staticmethod
    def add_cachorro():
        clear_screen()

        nome = input("Digite o nome do cachorro: ")
        idade = int(input("Digite a idade do cachorro: "))
        genero = input("Digite o gênero do cachorro(M/F): ").upper()
        raca = input("Digite a raça do cachorro: ")
        porte = input("Digite o porte do cachorro: ")
        cor = input("Digite a cor do cachorro: ")

        novo_cachorro = Cachorro(nome, idade, genero, raca, porte, cor)
        cachorros.append(novo_cachorro)   

    @staticmethod
    def add_gato():
        clear_screen()

        nome = input("Digite o nome do gato: ")
        idade = int(input("Digite a idade do gato: "))
        genero = input("Digite o gênero do gato(M/F): ").upper()
        tipo = input("Digite o tipo do gato: ")

        novo_gato = Gato(nome, idade, genero, tipo)
        gatos.append(novo_gato) 

    @staticmethod
    def add_peixe():
        clear_screen()

        nome = input("Digite o nome do peixe: ")
        idade = int(input("Digite a idade do peixe: "))
        genero = input("Digite o gênero do peixe(M/F): ").upper()
        tipo = input("Digite o tipo do peixe: ")

        novo_peixe = Peixe(nome, idade, genero, tipo)
        peixes.append(novo_peixe)  

    @staticmethod
    def add_cavalo():
        clear_screen()

        nome = input("Digite o nome do cavalo: ")
        idade = int(input("Digite a idade do cavalo: "))
        genero = input("Digite o gênero do cavalo(M/F): ").upper()
        raca = input("Digite a raça do cavalo: ")
        categoria = input("Digite a categoria do cavalo: ")
        cor = input("Digite a cor do cavalo: ")

        novo_cavalo = Cavalo(nome, idade, genero, raca, categoria, cor)
        cavalos.append(novo_cavalo)   

    @staticmethod
    def add_passaro():
        clear_screen()

        nome = input("Digite o nome do pássaro: ")
        idade = int(input("Digite a idade do pássaro: "))
        genero = input("Digite o gênero do pássaro(M/F): ").upper()
        raca = input("Digite a raça do pássaro: ")
        cor = input("Digite a cor do pássaro: ")

        novo_passaro = Passaro(nome, idade, genero, raca, cor)
        passaros.append(novo_passaro)

class Deletar:
     @staticmethod
     def deletar_animal(animais,especie):
        opcao= input(f"\nEscolha qual {especie} remover:").strip().upper()
        selecionado = animais[int(opcao)-1]
        animais.remove(selecionado)
      

class Cachorro(Animal):
    def __init__(self, nome, idade, genero, raca, porte, cor):
        super().__init__(nome, idade, genero)
        self.raca = raca
        self.porte = porte
        self.cor = cor
    
    
    def __str__(self):
        return f"NOME: {self.nome}, {self.idade} anos\nGÊNERO: {self.genero}\nRAÇA: {self.raca}\nPORTE: {self.porte}\nCOR: {self.cor}"

class Gato(Animal):
    def __init__(self, nome, idade, genero, tipo):
        super().__init__(nome, idade, genero)
        self.tipo = tipo

    def __str__(self):
        return f"NOME: {self.nome}, {self.idade} anos\nGÊNERO: {self.genero}\nTIPO: {self.tipo}"

class Peixe(Animal):
    def __init__(self, nome, idade, genero, tipo):
        super().__init__(nome, idade, genero)
        self.tipo = tipo

    def __str__(self):
        return f"NOME: {self.nome}, {self.idade} anos\nGÊNERO: {self.genero}\nTIPO: {self.tipo}"

class Cavalo(Animal):
    def __init__(self, nome, idade, genero, raca, categoria, cor):
        super().__init__(nome, idade, genero)
        self.raca = raca
        self.categoria = categoria
        self.cor = cor

    def __str__(self):
        return f"NOME: {self.nome}, {self.idade} anos\nGÊNERO: {self.genero}\nRAÇA: {self.raca}\nCATEGORIA: {self.categoria}\nCOR: {self.cor}"

class Passaro(Animal):
    def __init__(self, nome, idade, genero, raca, cor):
        super().__init__(nome, idade, genero)
        self.raca = raca
        self.cor = cor

    def __str__(self):
        return f"NOME: {self.nome}, {self.idade} anos\nGÊNERO: {self.genero}\nRAÇA: {self.raca}\nCOR: {self.cor}"


cachorros = [
    Cachorro("Tody", 8, "M", "Labrador", "Médio", "Caramelo"),
    Cachorro("Collie", 4, "F", "Labrador", "Médio", "Preto"),
    Cachorro("Hunter", 11, "M", "Husk Siberiano", "Médio", "Cinza-Branco"),
    Cachorro("Bob", 7, "M", "Beagle", "Pequeno", "Marrom-Preto-Branco"),
    Cachorro("Laika", 6, "F", "Border-collie", "Pequeno", "Preto-Branco"),
    Cachorro("Poket", 3, "F", "Chihuahua", "Mini", "Branco"),
    Cachorro("Clifford", 10, "F", "Dogue Alemão", "Grande", "Marrom")
]

gatos = [
    Gato("Gio", 3, "F", "Laranja"),
    Gato("Morgana", 12, "F", "Frajola"),
    Gato("Tom", 13, "M", "Siames"),
    Gato("Selina", 4, "F", "Preto"),
    Gato("Garfield", 13, "M", "Laranja"),
    Gato("Lion", 7, "F", "Ashera"),
]

peixes = [
    Peixe("Darwin", 3, "F", "Dourado"),
    Peixe("Arthur", 2, "M", "Dourado"),
    Peixe("Nemo", 3, "M", "Dourado"),
    Peixe("Ariel", 1, "F", "Arco-íris"),
]

cavalos = [
    Cavalo("Pegazos", 11, "M", "Puro Sangue Inglês", "Corrida", "Castanha"),
    Cavalo("Liza", 12, "F", "Appaloosa", "Lazer", "Tordilha"),
    Cavalo("Carpeado", 13, "M", "Pônei Shetland", "Lazer", "Alazão"),
    Cavalo("Perceus", 6, "M", "Clydesdale", "Carga", "Marrom Avermelhado"),
    Cavalo("Agro", 12, "F", "Cavalo de Sela Francês", "Lazer", "Castanha"),
    Cavalo("Solidus", 17, "M", "Quarto de Milha", "Corrida", "Tordilha"),
]

passaros = [
    Passaro("Louro", 3, "M", "Calopsita", "Cinza"),
    Passaro("Kiwi", 5, "F", "Agapornis", "Verde"),
    Passaro("Piu", 1, "M", "Canário", "Amarelo"),
    Passaro("Chico", 51, "M", "Papagaio", "Verde-Amarelo"),
]

Menu.menu_fichas(cachorros, gatos, peixes, cavalos, passaros)
