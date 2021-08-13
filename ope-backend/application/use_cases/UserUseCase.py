class UserUseCase:
    def __init__(self):
        self.repository = UserRepository
        self.message = ""

    async def create_user_async(self, input):
        #checar se usuario já existe
        user = await self.repository.get_by_email_async(input.email)
        if not isinstance(user, None):
            #configurar erro 400
            self.message = "Usuário já existe"
            return False
        self.repository.create_user_async(input)
        return True
