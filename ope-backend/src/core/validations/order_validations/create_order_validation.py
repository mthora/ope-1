def create_order_validation(
        done: bool,
        initial_date: str,
        end_date: str,
        consumed_in: str,
        table: int,
        payment_method: str,
        obs: str,
        confirmed: bool):
    message: list[str] = []
    if not isinstance(done, bool) or done is None or done == "":
        message.append("status inválido")
    if initial_date is None:
        message.append("Ocorreu um erro na requisição")
    if end_date is not None:
        message.append("Ocorreu um erro na requisição")
    if not isinstance(consumed_in, int) or consumed_in is None:
        message.append("Data de consumo inválida")
    if not (isinstance(table, int)):
        message.append("Mesa inválida")
    if consumed_in == 1 and (table is None or table == 0):
        message.append("Mesa inválida")
    if not isinstance(payment_method, int) or payment_method is None or payment_method == "":
        message.append("Forma de pagamento inválida")
    if not isinstance(obs, str) and obs != "":
        message.append("Observação inválida")
    if not isinstance(confirmed, bool) or confirmed is None:
        message.append("Ocorreu um erro na requisição")
    return message
