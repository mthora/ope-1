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
    if not isinstance(initial_date, str) or initial_date is None or initial_date == "":
        message.append("Data inicial inválida")
    if not isinstance(end_date, str) or end_date is None or end_date == "":
        message.append("Data final inválida")
    if not isinstance(consumed_in, str) or consumed_in is None or consumed_in == "":
        message.append("Data de consumo inválida")
    if not isinstance(table, str) or table is None or table == "":
        message.append("Mesa inválida")
    if not isinstance(payment_method, str) or payment_method is None or payment_method == "":
        message.append("Forma de pagamento inválida")
    if not isinstance(obs, str) or obs is None or obs == "":
        message.append("Observação inválida")
    if not isinstance(confirmed, str) or confirmed is None or confirmed == "":
        message.append("Confirmação inválida")
    return message
