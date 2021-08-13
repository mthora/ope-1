class UserRepository:
    #configurar conexão com o banco
    #db = await getconnection bla bla bla
    #cursor blabla
    def CreateUserAsync(self, input):
        script = open('scripts/CreateUserAsync.sql').read()
        #retorno = cursor.execute(script) etc
        #terminar conexão
        retorno = True
        return retorno

