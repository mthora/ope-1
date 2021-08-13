class CreateUserHandler:

    def __init__(self, use_case, query):
        self.useCase = use_case
        self.query = query

    async def handle(self):
        if self.query.is_valid():
            output = await self.useCase.CreateUserAsync(self.query.input)
            return output
        return self.query.errors
