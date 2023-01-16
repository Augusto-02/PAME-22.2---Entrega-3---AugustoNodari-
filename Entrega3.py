
def PrintMenu():
      print("1- Fazer Login")
      print("2- Criar Projeto")
      print("3- Remover Projeto")
      print("4- Criar Consultor")
      print("5- Remover Consultor")
      print("6- Criar Gerente")
      print("7- Remover Gerente")
      print("8- Listar Gerentes / Consultores / Projetos")
      print("9- Sair")
      
def PrintMenuConsultor():
      print("1 - Ver meus dados")
      print("2 - Modificar meus dados")
      print("3 - Verificar Projetos onde estou alocado")
      print("4 - Avançar com um projeto")
      print("5 - Pedir retirada de um projeto")
      print("6 - Sair")
      
def PrintMenuGerente():
      print("1 - Ver meus dados")
      print("2 - Modificar meus dados")
      print("3 - Verificar Projetos onde estou alocado")
      print("4 - Avançar com um projeto")
      print("5 - Dar aval sobre a retirada de um consultor")
      print("6 - Passar o projeto a outro gerente")
      print("7 - Entregar um projeto")
      print("8 - Sair")      
      
            
def ProcuraId(id, lista):
      for el in range(0, len(lista)):
            if lista[el][0] == id:
                  return 0
      return -1
          
      
class Projeto:
      def __init__(self, listaproj):
            self.listaproj = listaproj
            
      def CriarProjeto(self, listaconsultor, listagerentes):
            nomeproj = input("Digite o nome do projeto: ")
            for el in self.listaproj:
                  if nomeproj == el[0]:
                        print("Nome de projeto ja utilizado")
                        input("Digite enter para continuar")
                        return
                  
            areaproj = input("Digite a area do projeto: ")
            idconsultores = input("Digite os id dos consultores do projeto: ")
            listconsultor = idconsultores.split()
            for el in listaconsultor:
                  if el[0] not in listconsultor:
                        print("Consultor nao encontrado")
                        return self.listaproj
            idgerente = input("Digite o id do gerente do projeto: ")
            num = ProcuraId(idgerente, listagerentes)
            if num == -1:
                  print("Gerente nao encontrado")
                  input("Digite enter para continuar")
                  return self.listaproj
            if areaproj == "Desenvolvimento":
                  etapas = 4
            elif areaproj =="Concepcao":
                  etapas = 5
            elif areaproj == "Identidade Visual":
                  etapas = 6
            else:
                  print("Area invalida")
                  return self.listaproj

            self.listaproj += [[nomeproj , areaproj, listconsultor, idgerente, etapas]]
            
      def RemoverProjeto(self):
            nome = input("Digite o nome do projeto que quer deletar: ")
            area = input("Digite a area do projeto: ")
            for el in self.listaproj:
                  if (el[0]== nome) and (el[1]== area):
                        self.listaproj.remove(el)
            return self.listaproj
      
      
class Gerente():
      def __init__(self, status, id, usuario, senha, listgerentes):
             self.status = status
             self.id = id
             self.usuario = usuario
             self.senha = senha
             self.listgerentes = listgerentes
             
      def  VerDados(self, id, nome, area, senha):
            if self.status == "Logado consultor" or self.status == "Logado Gerente":
                  print(f'ID: {id}, Nome: {nome}, area: {area}, senha: {senha}')
            input("Digite enter para continuar")
      
      def ModificarDados(self):
        
        resposta=input("Deseja mudar o usuário(sim/nao): ")
        if resposta == 'sim':
            novo_usuario=input("Novo nome: ")
            self.usuario = novo_usuario

        resposta=input("Deseja mudar a senha(sim/nao): ")
        if resposta == 'sim':
            nova_senha=input("Nova senha: ")
            self.senha = nova_senha

        resposta=input("Deseja mudar a area(sim/nao): ")
        if resposta == 'sim':
            nova_area=input("Nova area: ")
            self.area = nova_area
            
        if self.status == "Logado consultor":  
            return  self.usuario, self.senha, self.area, "1"
            
        elif self.status == "Logado gerente":
            return  self.usuario, self.senha, self.area, "2"
            
      def VerificarProjetos(self, listaprojs):
            if self.status == "Logado gerente":
                  for el in listaprojs:
                        if self.id == el[3]:
                              print(f'Nome: {el[0]}, area: {el[1]},etapas faltando: {el[4]}')
                              
            if self.status == "Logado consultor":
                  for el in listaprojs:
                        if self.id in el[2]:
                              print(f'Nome: {el[0]}, area: {el[1]}, id do gerente: {el[3]}, etapas faltando: {el[4]}')      
            input("Digite enter para continuar")                 
                  
      
class Consultor(Gerente):
       def __init__(self, status, id, usuario, senha, listconsultores):
             super().__init__(status,id,usuario,senha)
             self.listconsultores = listconsultores
                
      
           
                  
class Sistema(Projeto, Consultor, Gerente):
      def __init__(self, status, listconsultores, listgerentes, listaproj):
            self.status = status
            self.listconsultores = listconsultores
            self.listgerentes = listgerentes
            self.listaproj = listaproj
            self.listapendencias = []
            self.listaretiradas = []
      
      def main(self):
            while True:
                  input("Digite enter para continuar")
                  PrintMenu()
                  opcao = input("Digite uma opcao: ")
                  if opcao == "1":
                        self.id, self.usuario, self.senha, self.area = self.Login()
                        
                        if self.status == "Logado consultor":
                              self.MenuConsultor()
                              
                        elif self.status == "Logado gerente":
                              self.MenuGerente()
                             
                  if opcao == "2":
                        self.CriarProjeto(self.listconsultores, self.listgerentes)
                  elif opcao == "3":
                        self.RemoverProjeto()
                  elif opcao == "4":
                        self.AdicionarConsultor()
                  elif opcao == "5":
                        self.RemoverConsultor()
                  elif opcao == "6":
                        self.AdicionarGerente()
                  elif opcao == "7":
                        self.RemoverGerente()
                  elif opcao == "8":
                        self.Listagem()
                  elif opcao == "9":
                        break
                  else:
                        print("Digite uma opcao Valida")
                        print()
                  
      def MenuConsultor(self):
            while True:
                  PrintMenuConsultor()
                  opcao = input("Digite uma opcao: ")
                  if opcao == "1":
                        self.VerDados(self.id, self.usuario, self.area, self.senha)
                  if opcao == "2":
                        self.usuario, self.senha, self.area, numero = self.ModificarDados()
                        if numero == "1":
                              num = ProcuraId(self.id, self.listconsultores)
                              self.listconsultores[num][1] = self.usuario
                              self.listconsultores[num][2] = self.senha
                              self.listconsultores[num][3] = self.area
                              
                  if opcao == "3":
                        self.VerificarProjetos(self.listaproj)
                  if opcao == "4":
                        self.AvancarProjetos()
                  if opcao == "5":
                        self.PedirRetiradaDoProjeto()
                  if opcao == "6":
                        break
                  
      def MenuGerente(self):
            while True:
                  PrintMenuGerente()
                  opcao = input("Digite uma opcao: ")
                  if opcao == "1":
                        self.VerDados(self.id, self.usuario, self.area, self.senha)
                  if opcao == "2":
                        self.usuario, self.senha, self.area, numero = self.ModificarDados()
                        if numero == "1":
                              num = ProcuraId(self.id, self.listgerentes)
                              self.listgerentes[num][1] = self.usuario
                              self.listgerentes[num][2] = self.senha
                              self.listgerentes[num][3] = self.area
                              
                  if opcao == "3":
                        self.VerificarProjetos(self.listaproj)
                  if opcao == "4":
                        self.PermitirAvancarProjetos()  
                  if opcao == "5":
                        self.listaproj = self.PermitirRetirada()
                  if opcao == "6":
                        self.listaproj = self.PassarProjeto()
                  if opcao == "7":
                        self.listaproj = self.EntregarProjeto()
                  if opcao == "8":
                        break            
      
      def Listagem(self):
            print("1 - Projetos")
            print("2 - Gerentes")
            print("3 - Consultores")
            op = input("Digite o que vc quer listar: ")
            if op =="1":
                  for el in self.listaproj:
                        print(f'Nome: {el[0]}, area: {el[1]}, id dos consultores: {el[2]}, id do gerente: {el[3]}, etapas faltando: {el[4]}')
                  input("Digite enter para continuar")
                  print()
            elif op =="2":
                  for el in self.listgerentes:
                        print(f'ID: {el[0]}, Nome: {el[1]}') 
                  input("Digite enter para continuar")     
                  print()
            elif op =="3":
                  for el in self.listconsultores:
                        print(f'ID: {el[0]}, Nome: {el[1]}')
                  input("Digite enter para continuar")
                  print()
            else:
                  print("Opcao invalida")
                  input("Digite enter para continuar")
                  print()
      
      def AdicionarConsultor(self):
            usuario = input("Digite o nome do consultor: ")
            senha = input("Digite a senha desse usuario: ")
            id = input("Digite o ID do usuario: ")
            area = input("Digite a sua area: ")
            for el in self.listconsultores:
                  if el[0] == id:
                        print("ID invalido")
                        return 
            for el in self.listgerentes:
                  if el[0] == id:
                        print("ID invalido")
                        return 
            self.listconsultores += [[id, usuario, senha, area]]
            print("Consultor adicionado com sucesso")
            input("Digite enter para continuar")      
            
      def RemoverConsultor(self):
            usuario = input("Digite o nome do consultor: ")
            id = input("Digite o ID do usuario: ")
            for el in self.listconsultores:
                  if (usuario== el[1]) and (id == el[0]):
                        self.listconsultores.remove(el)
                        print("Consultor retirado com sucesso")
                        input("Digite enter para continuar")
            else:
                  print("Consultor nao encontrado")
           
           
      def AdicionarGerente(self):
            usuario = input("Digite o nome do gerente: ")
            senha = input("Digite a senha desse usuario: ")
            id = input("Digite o ID do usuario: ")
            area = input("Digite a sua area: ")
            for el in self.listconsultores:
                  if el[0] == id:
                        print("ID invalido")
                        input("Digite enter para continuar")
                        return 
            for el in self.listgerentes:
                  if el[0] == id:
                        print("ID invalido")
                        input("Digite enter para continuar")
                        return 
            self.listgerentes += [[id, usuario, senha, area]]
            print("Gerente adicionado com sucesso")
            input("Digite enter para continuar")    
            
            
      def RemoverGerente(self):
            usuario = input("Digite o nome do gerente: ")
            id = input("Digite o ID do usuario: ")
            for el in self.listaproj:
                  if el[3] == id:
                        print("Nao e possivel remover o gerente pois ele esta alocado em um projeto")
                        input("Digite enter para continuar")
                        return 
            for el in self.listgerentes:
                  if (usuario== el[1]) and (id == el[0]):
                        self.listgerentes.remove(el)
                        print("Gerente removido com sucesso")
                        input("Digite enter para continuar")
                        return
            else:
                  print("Gerente nao encontrado")
            
      
      def Login(self):
            id = input("Digite o ID do usuario: ")
            senha = input("Digite a senha: ")
            for el in self.listconsultores:
                  if el[0]==id and el[2]==senha:
                        self.status = "Logado consultor"
                        print("Logado como consultor com sucesso")
                        print()
                        return el[0], el[1], el[2], el[3]
            for el in self.listgerentes:
                  if el[0]==id and el[2]==senha:
                        self.status = "Logado gerente"
                        print("Logado como gerente com sucesso")
                        print()
                        return el[0], el[1], el[2], el[3]
            else: 
                  print("Login invalido")
                  self.status == "Deslogado"
                  return "", "", "", ""   
                    
      def AvancarProjetos(self):
            if self.status == "Logado consultor":
                  self.VerificarProjetos(self.listaproj)
                  nomeproj = input("Digite o nome do projeto que deseja avancar: ")
                  id = input("Digite o ID do gerente desse projeto: ")
                  num = ProcuraId(id, self.listgerentes)
                  if num == -1:
                        print("Gerente nao encontrado")
                        input("Digite enter para continuar")
                        return
                        
                  for el in self.listaproj:
                              if el[0] == nomeproj:
                                    if el[4] == 0:
                                          print("O projeto ja está concluido")
                                          input("Digite enter para continuar")
                                          return self.listaproj
                  
                  print("Projeto esta na lista de pendencias para o avanco")
                  self.listapendencias += [[id, nomeproj]]
                  input("Digite enter para continuar")
      
      def PermitirRetirada(self):
            if self.status == "Logado gerente":
                  for el in self.listaretiradas:
                        if self.id == el[0]:
                              print(f'Nome do Projeto: {el[1]}, Nome do consultor: {el[2]}')
                  nomeproj = input("Digite o nome do projeto que deseja analisar dar o aval da retirada do consultor: ")
                  nomeconsultor = input("Digite o nome do consultor que deseja retirar do projeto: ")
                  for el in self.listaretiradas:
                        if el[1] == nomeproj:
                              self.listaretiradas.remove(el)
                     
                  for el in self.listaproj:
                        if el[0] == nomeproj:
                              el[2].remove(nomeconsultor)
                              print("Consultor retirado com sucesso")
                              return self.listaproj
            
            print("Nao foi possivel retirar o consultor do projeto")
            input("Digite enter para continuar")
            return self.listaproj
                  
      def PassarProjeto(self):
            if self.status == "Logado gerente":
                  self.VerificarProjetos(self.listaproj)
                  nomeproj = input("Digite o nome do projeto que deseja passar para outro gerente: ")
                  idnovo = input("Digite o id do novo gerente: ")
                  num = ProcuraId(idnovo, self.listgerentes)
                  if num == -1:
                        print("Gerente nao encontrado")
                        input("Digite enter para continuar")
                        return self.listaproj
                  for el in self.listaproj:
                              if el[0] == nomeproj:
                                    if el[4] == 0:
                                          print("O projeto ja está concluido")
                                          input("Digite enter para continuar")
                                          return self.listaproj
                  for el in self.listaproj:
                        if el[0] == nomeproj:
                              el[3] = idnovo
                              print("Troca de gerentes realizada com sucesso")
                              return self.listaproj
                        
            print("Nao foi possivel mudar o gerente do projeto")
            input("Digite enter para continuar")
            return self.listaproj
      
      def EntregarProjeto(self):
            if self.status == "Logado gerente":
                  for el in self.listaproj:
                        if el[3] == self.id:
                              if el[4] == 0:
                                    print("Projeto entregue")
                                    self.listaproj.remove(el)
                                    input("Digite enter para continuar")
                                    return self.listaproj
                              else:
                                    print("Nao e possivel entregar o projeto")
                                    input("Digite enter para continuar")
                                    return self.listaproj
            else:
                  print("Nao e possivel entregar o projeto")
                  input("Digite enter para continuar")
            return self.listaproj
                              
      
      def PermitirAvancarProjetos(self):
            lista = []
            if self.status == "Logado gerente":
                  for el in self.listapendencias:
                        if self.id == el[0]:
                              print(f'Nome do Projeto: {el[1]}')
                              lista += [el[1]]
                  if len(lista) == 0:
                        print("Nao tem projetos para avancar no momento")
                        return self.listaproj
                  nomeproj = input("Digite o nome do projeto que deseja avancar: ")
                  
                  for el in self.listapendencias:
                        if el[1] == nomeproj:
                              self.listapendencias.remove(el)
                     
                  for el in self.listaproj:
                        if el[0] == nomeproj:
                              el[4] = el[4]-1
                              print("Sucesso")
                              return self.listaproj
            
            print("Nao foi possivel avancar o projeto")
            input("Digite enter para continuar")
            return self.listaproj            
      
      def PedirRetiradaDoProjeto(self):
            if self.status == "Logado consultor":
                  self.VerificarProjetos(self.listaproj)
                  nomeproj = input("Digite o nome do projeto que deseja se retirar: ")
                  id = input("Digite o ID do gerente desse projeto: ")
                  num = ProcuraId(id, self.listgerentes)
                  if num == -1:
                        print("Gerente nao encontrado")
                        input("Digite enter para continuar")
                        return
                  for el in self.listaproj:
                              if el[0] == nomeproj:
                                    if el[4] == 0:
                                          print("O projeto ja está concluido")
                                          input("Digite enter para continuar")
                                          return self.listaproj
                  
                  print("Sua solicitacao esta na lista de pendencias")
                  self.listaretiradas += [[id, nomeproj, self.id]]
                  input("Digite enter para continuar")
      
     


            
      
      
      
sistema1 = Sistema("Deslogado",[["GUGU","GU","BABA","Desenvolvimento"]],[["AUG","Augusto","BABA","Desenvolvimento"]],[["Flemis", "Desenvolimento", ["GUGU", "UG"],"AUG", 0],["FLU", "Identidade Visual", ["GUGU", "UG"], "AUG", 6]])
sistema1.main()


