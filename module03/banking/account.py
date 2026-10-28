from enum import Enum


class InsufficientBalanceException(Exception):
    def __init__(self, message: str, deficit: float) -> None:
        super().__init__(message)
        self.message = message
        self.deficit = deficit


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class Account:
    def __init__(self, iban: str, balance: float = 5_000, status: AccountStatus = AccountStatus.ACTIVE) -> None:
        # attributes/state/data; single underscore so subclasses can reach them
        self._iban = iban
        # constraint: the balance never drops below what _available_funds() allows
        self._balance = balance
        self._status = status

    @property
    def iban(self) -> str:
        return self._iban

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def status(self) -> AccountStatus:
        return self._status

    @status.setter
    def status(self, status: AccountStatus) -> None:
        if not isinstance(status, AccountStatus):
            raise ValueError("Status must be one of AccountStatus.ACTIVE, CLOSED or BLOCKED")
        self._status = status

    def deposit(self, amount: float) -> float:
        self._validate_transaction(amount)
        self._balance += amount
        return self._balance

    # business method
    def withdraw(self, amount: float) -> float:
        self._validate_transaction(amount)
        available = self._available_funds()
        # business rule
        if amount > available:
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", amount - available)
        self._balance -= amount
        return self._balance

    def _validate_transaction(self, amount: float) -> None:
        # business rule
        if self._status != AccountStatus.ACTIVE:
            raise ValueError("Account is not active")
        # validation rule
        if amount <= 0.0:
            raise ValueError("Amount must be positive")

    def _available_funds(self) -> float:
        """The most that can be withdrawn right now; subclasses override this to change the rule."""
        return self._balance

    def __str__(self) -> str:
        return f"{type(self).__name__}: iban: {self.iban}, balance: {self.balance}, status: {self.status}"


class CheckingAccount(Account):
    """
    CheckingAccount: sub class, derived class
    Account        : super class, base class

    The overdraft lets the balance go negative, down to -overdraft_amount.
    """

    def __init__(self, iban: str, balance: float = 5_000, status: AccountStatus = AccountStatus.ACTIVE,
                 overdraft_amount: float = 1_000) -> None:
        super().__init__(iban, balance, status)
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self) -> float:
        return self._overdraft_amount

    @overdraft_amount.setter
    def overdraft_amount(self, overdraft_amount: float) -> None:
        if overdraft_amount <= 0.0:
            raise ValueError("Overdraft amount must be positive")
        self._overdraft_amount = overdraft_amount

    # overriding: the overdraft extends the funds available to withdraw()
    def _available_funds(self) -> float:
        return self._balance + self._overdraft_amount

    def __str__(self) -> str:
        return f"{super().__str__()}, overdraft_amount: {self.overdraft_amount}"
