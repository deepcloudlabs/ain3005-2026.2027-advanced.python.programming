"""Encapsulation: hide an object's state behind properties and guard it with business rules."""
from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class Account:
    def __init__(self, iban: str, balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE) -> None:
        # double underscore -> name mangling: the attributes are "private" to the class
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    @property
    def iban(self) -> str:
        return self.__iban

    @iban.setter
    def iban(self, new_iban: str) -> None:
        self.__iban = new_iban

    @property
    def balance(self) -> float:
        # read-only: there is no setter, so `account.balance -= 1_000_000` raises AttributeError
        return self.__balance

    @property
    def status(self) -> AccountStatus:
        return self.__status

    def deposit(self, amount: float) -> None:
        self._validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        self._validate_amount(amount)
        # business rule
        if amount > self.__balance:
            raise ValueError("amount cannot be greater than balance")
        self.__balance -= amount

    @staticmethod
    def _validate_amount(amount: float) -> None:
        # validation rule
        if amount <= 0:
            raise ValueError("amount must be positive")

    def __str__(self) -> str:
        return f"Account [iban: {self.__iban}, balance: {self.__balance}, status: {self.__status.name}]"


def main() -> None:
    acc1 = Account(iban="tr1", balance=1_000)
    acc2 = Account(iban="tr2", status=AccountStatus.BLOCKED)
    acc1.withdraw(700)  # same as Account.withdraw(acc1, 700)
    acc1.iban = "tr3"  # goes through the iban setter
    print(acc1.balance)
    print(acc1)  # print() calls str(acc1), which calls acc1.__str__()
    print(acc2)


if __name__ == "__main__":
    main()
