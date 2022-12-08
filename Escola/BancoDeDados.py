
class DataBase():
    def __int__(self,tabela,ComandoSQL = False):
        self.tabela = tabela
        self.ComandoSQL = ComandoSQL

    def SelecionarTabela(self):
        sala = int(input("Existem duas salas registradas no sistema: \n"
                         "Escolha:\n[1]Sala A\n[2]Sala B\n"))
        while True:
            if sala > 0 and sala <=2:
                self.tabela = sala
                break
            else:
                sala = int(input("Por favor escolha uma opção registrada no sistema: \n"
                                 "Escolha:\n[1]Sala A\n[2]Sala B\n"))

        return self.tabela

    def MostrarDados(self,cursor):
        if self.tabela == 0:
            print("nenhuma tabela selecionada")
            return
        elif self.tabela == 1:
            comando = "SELECT * FROM salaa;"
            cursor.execute(comando)
            self.ComandoSQL = cursor.fetchall()
            return self.ComandoSQL

        elif self.tabela == 2:
            comando = "SELECT * FROM salab;"
            cursor.execute(comando)
            self.ComandoSQL = cursor.fetchall()
            return self.ComandoSQL

    def CopularTabela(self,cursor,banco,nome,nota1,nota2,nota3):

        if self.tabela == 0:
            print("nenhuma tabela selecionada")
            return

        elif self.tabela == 1:
            media = (nota1 + nota2 + nota3)/3
            comando = "INSERT INTO salaa (nome,nota1,nota2,nota3,media) VALUES " \
                      "('{}','{}','{}','{}','{}')".format(nome,nota1,nota2,nota3,media)

            self.ComandoSQL = cursor.execute(comando), banco.commit()
            return self.ComandoSQL

        elif self.tabela == 2:
            media = (nota1 + nota2 + nota3) / 3
            comando = "INSERT INTO salab (nome,nota1,nota2,nota3,media) VALUES" \
                      " ('{}','{}','{}','{}','{}')".format(nome,nota1,nota2,nota3,media)

            self.ComandoSQL = cursor.execute(comando), banco.commit()
            return self.ComandoSQL
