class Cafe_espresso:
    def otima_escolha(self):
        print("Ótima escolha!")
            
    def moer_cafe(self):
        print("Moendo os grãos do café...")
        
    def tamping(self):
        print("Adicionando o pó de café no portafiltro...")

    def insercao(self):
        print("Inserindo o portafiltro na máquina de café expresso...")

    def extraindo(self):
        print("Extraindo o café...")

    def crema(self):
        print("Finalizando o processamento do seu café...")

    def listo(self):
        print("A extração foi concluída, o café expresso está pronto para ser servido.")

    def espresso(self):
        print("\n")
        self.otima_escolha()
        self.moer_cafe()
        self.tamping()
        self.insercao()
        self.extraindo()
        self.crema()
        print("\n")
        self.listo()
        print("\n")

class Cafe_capsula(Cafe_espresso): #CAPSULAS OP-2
        def __init__(self):
            self.capsulas = ["Nespresso Ristretto", "Nespresso Arpeggio", "Nespresso Lungo", "Nespresso Volluto", "Lavazza A Modo Mio Intenso", "Lavazza A Modo Mio Cremoso", "Illy Espresso", "Dolce Gusto Espresso", "Tchibo Cafissimo Espresso", "Caffè Vergnano 1882 Espresso"]

        def escolha_cap(self):
            print()
            for capsula in enumerate(self.capsulas, start=1):
                print(*capsula, sep=': ')

        def inserir_cap(self):
            print("Inserindo a cápsula escolhida na máquina...")

        def aquecendo(self):
            print("A água está sendo aquecida até uma temperatura ideal (normalmente entre 85°C a 95°C) através de um sistema de aquecimento rápido.")

        def extrai(self):
            print("Extraindo os compostos solúveis que formam a bebida. Esse processo dura de 20 a 30 segundos...")

        def listoo(self):
            print("Seu café foi extraido e está pronto para consumo. ")
            print("A cápsula usada é ejetada automaticamente pela máquina para um recipiente de descarte de cápsulas.")

        def capsula(self):
            print("\n")
            super().otima_escolha()
            self.inserir_cap()
            self.aquecendo()
            self.extrai()
            self.listoo()
            print("\n")
            
class Cafe_filtro(Cafe_espresso):
    #0func vou importar OTIMA ESCOLHA
    #1func vou importar da classe pai / moer cafe

    def preparo(self):
        print("Colocando o filtro de papel no funil...")

    def adicao_cafe(self):
        print("Colocando o café moído de maneira uniforme no filtro... ")

    def aquecimento(self):
        print("Aquecendo a água com uma média entre 90°C a 96°C...")

    def filtragem(self):
        print("Despejando a água de forma lenta e circular, começando de fora para dentro, para garantir que toda a camada de café moído seja saturada uniformemente.")

    def coleta(self):
        print("Seu café está pronto para ser apreciado! Agora, basta servir em sua xícara favorita e, se desejar, adicionar açúcar conforme o seu gosto.")
        print("Aproveite o aroma e o sabor do seu café fresquinho! ☕")

    def conclusao(self):
        print("\n")
        super().otima_escolha()
        super().moer_cafe()
        self.preparo()
        self.adicao_cafe()
        self.aquecimento()
        self.filtragem()
        print("\n")
        self.coleta()
        print("\n")

class Cafe_leite(Cafe_filtro, Cafe_espresso):
    def tipos(self):
        self.cafes = ["Café Expresso", "Café Filtrado"]
        for cafe in enumerate(self.cafes, start=1):
            print(*cafe, sep=". ")

        self.escolhaa = int(input("\nEscolha entre as opções para o seu tipo de café ideal: "))
            
    def escolha_do_cafe(self):
        if self.escolhaa == 1: #cafe_expresso
            print("\n")
            super().otima_escolha() #chamar funcao por funcao
            super().moer_cafe()
            super().tamping()
            super().insercao()
            super().extraindo()
            super().crema()

            
        elif self.escolhaa == 2: #cafe_filtrado
            print("\n")
            super().otima_escolha()
            super().preparo()
            super().adicao_cafe()
            super().aquecimento()
            super().filtragem()
            print("O café está preparado...")

        else:
            print("Selecione uma opção válida. 1 para Café Expresso e 2 para Café Filtrado.")

    #1func OTIMA ESCOLHA IMPORTADA

    def aquecimento_leite(self):
        print("Aquecendo o leite até aproximadamente 70°C a 80°C...")
        print("Vaporizado o leite até que fique espesso para criar uma espuma adicional...")

    def misturando(self):
        if self.escolhaa == 1: #Cafe_expresso
            print("Despejando o café expresso em uma xícara. Em seguida, adicionando o leite quente e espumado...")

        elif self.escolhaa == 2: #Cafe_filtrado
            print("Despejando o café preparado na xícara e depois adicionando o leite, mexendo suavemente para misturar...")

    def finalizacao(self):
        print("Se necessário, adicione açúcar, adoçante ou até mesmo um pouco de essência de baunilha para dar um toque especial à sua bebida.")
        print("Aproveite o aroma e o sabor do seu café fresquinho! ☕")
        
    def pronto(self):
        print("\n")
        self.tipos()
        self.escolha_do_cafe()
        self.aquecimento_leite()
        self.misturando()
        print("\n")
        self.finalizacao()
        print("\n")

class Informacoes:
    def Infos(self):
        self.machines = ["Máquina de Café Expresso", "Máquina de Café de Cápsulas", "Máquina de Café de Filtro", "Máquina de Café com Leite"]
        print("\n")
        for machine in enumerate(self.machines, start=1):
            print(*machine, sep='. ')

        print("\n")
        self.qualmaquina = int(input("Insira qual máquina deseja obter mais informações: "))
    
        if self.qualmaquina == 1: #cafe expresso
           print("Uma máquina de café espresso é um equipamento projetado para preparar café espresso, que é um tipo de café concentrado e forte, feito através da passagem de água quente sob alta pressão por grãos finamente moídos. O processo de preparo é rápido, geralmente levando de 25 a 30 segundos, e resulta em uma bebida espessa, rica e com uma camada de creme (uma espuma dourada e aveludada formada pela emulsificação dos óleos do café).")
           print("\n")
        elif self.qualmaquina == 2: #cafe capulas
           print("A máquina de café de cápsulas é um tipo de equipamento de preparo de café que utiliza cápsulas ou pods (pequenos recipientes de café pré-dosado) para fazer bebidas de forma rápida e prática. Essas máquinas são conhecidas pela conveniência, pois oferecem um processo de preparo simples, sem a necessidade de moer o café ou medir a quantidade exata de pó.")
           print("\n")    
        elif self.qualmaquina == 3: #cafe filtro
           print("O café de filtro é um dos métodos de preparação mais tradicionais e populares, especialmente em casa e em escritórios. O processo é relativamente simples, mas exige algum cuidado em relação à proporção de café e água, temperatura e tempo de extração.")
           print("\n")
        elif self.qualmaquina == 4: #cafe leite
           print("A máquina de café com leite é um tipo de equipamento projetado para preparar café e, ao mesmo tempo, integrar leite na bebida, criando opções como cappuccinos, lattes, ou outros cafés com leite. Existem diferentes tipos de máquinas, mas todas têm em comum a capacidade de misturar café e leite, seja de forma manual ou automática.")
           print("\n")
        else:
           print("Número inválido. Selecione apenas as opções cima.")
           print("\n")
           
cafe_espresso = Cafe_espresso()
cafe_capsula = Cafe_capsula()
cafe_filtro = Cafe_filtro()
cafe_leite = Cafe_leite()
infos = Informacoes()

def main():
    while True:
        print("======      COFFEE SHOP      ======")
        print("'Through coffee, I express myself.'")
        
        opcao1 = str(input("\nDeseja ver nosso cardápio? [S/N]: "))
        
        if opcao1.lower() == 's':
            print("\n[1] Café Expresso: \n[2] Café de Cápsulas: \n[3] Café de Filtro: \n[4] Café com Leite: \n[5] Ver descrição de cada máquina: \n[6] Sair: \n")
            opcao2 = int(input("Insira qual opção deseja seguir: ")) #opcao para escolher a máquina!
            
            if opcao2 == 1:
                cafe_espresso.espresso()

            elif opcao2 == 2:
                cafe_capsula.escolha_cap()
                opcao_cap = int(input("\nEscolha o número da qual deseja saborear: "))
                cafe_capsula.capsula()

            elif opcao2 == 3:
                cafe_filtro.conclusao()

            elif opcao2 == 4:
                cafe_leite.pronto()

            elif opcao2 == 5:
                infos.Infos()

            elif opcao2 == 6:
                print("Encerrando...")
                break
        else:
            print("Encerrando...")
            break

main()

