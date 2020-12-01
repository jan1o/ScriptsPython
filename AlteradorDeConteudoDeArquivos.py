

class Main:
    def __init__(self):
        while True:
            escolha = int(input("Digite: \n 0 - Sair \n 1 - Continuar \n"))
            if escolha == 0:
                break;
            else:
                diretorio = input("Digite o Diretorio: \n OBS: digite no seguinte modelo - C:usu\\\pasta\\\\arquivo.extensao OU C:usu/pasta/arquivo.extensao \n")
                Converter(diretorio)
                          
                        
                                
                                
        

class Converter:
    def __init__(self, path):
        self.path = path

        arquivo = open(self.path, "r")
        print("Conteudo antigo: ",arquivo.readlines())
        arquivo.close()

        arquivo = open(self.path, "w")
        arquivo.write("texto alterado")
        arquivo.close()

        arquivo = open(self.path, "r")
        print("Conteudo novo: ",arquivo.readlines())
        arquivo.close()
        
        
  

#Converter(r"C:\Users\Usuário\Desktop\jogos\World of Warcraft - 3.3.5a (12340) - enUS (No Install)\Data\enUS\realmlist.wtf")
Main()
