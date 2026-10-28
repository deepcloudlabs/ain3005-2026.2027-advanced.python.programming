from .account import Account
from .customer import Customer


class Bank:
    def __init__(self, name: str) -> None:
        self._name = name
        self._customers: list[Customer] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def customers(self) -> tuple[Customer, ...]:
        return tuple(self._customers)

    def create_customer(self, identity: str, fullname: str) -> Customer:
        customer = Customer(identity, fullname)
        self._customers.append(customer)
        return customer

    def get_account(self, iban: str) -> Account | None:
        accounts = (customer.get_account(iban) for customer in self._customers)
        return next((account for account in accounts if account is not None), None)
