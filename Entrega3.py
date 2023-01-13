
def PrintOpcoes():
      print("1- Fazer Login")
      print("2- Criar Projeto")
      print("3- Remover Projeto")
      print("4- Criar Consultor")
      print("5- Remover Consultor")
      print("6- Criar Gerente")
      print("7- Remover Gerente")
      print("8- Listar Gerentes / Consultores / Projetos")
      print("9- Sair")
      
      
class Sistema:
      def __init__(self, status):
            self.status = status
           
            

class Consultor:
      pass

class Gerente:
      pass

class Projeto:
      def __init__(self, status):
            self.status = status
            
      def CriarProjeto(self, nome, area, cliente):
            self.nome = nome
            self.area = area
            self.cliente = cliente
      
      
      
      
sistema1 = Sistema("Logado")
print(sistema1.status)