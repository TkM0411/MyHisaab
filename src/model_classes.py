import datetime


class DailyTransaction:
    """
    Data Model for Daily Transactions
    """
    
    def __init__(self, transaction_date: str, description: str, amount: float, payment_mode: int, expense_type: int):
        """
        Init Method for Daily Transactions
        Attributes:
            transaction_date (str): Date of the transaction
            description (str): Description of the transaction
            amount (float): Amount of the transaction
            payment_mode (int): Payment mode of the transaction
            expense_type (int): Expense type of the transaction
        """
        self.__transaction_id = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        self.__transaction_date = int(transaction_date.replace("-", ""))
        self.__description = description
        self.__amount = amount
        self.__payment_mode = payment_mode
        self.__expense_type = expense_type
