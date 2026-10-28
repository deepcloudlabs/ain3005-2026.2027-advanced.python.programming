from .account import Account


class Customer:
    def __init__(self, identity: str, fullname: str) -> None:
        self._identity = identity
        self._fullname = fullname
        self._accounts: list[Account] = []

    @property
    def identity(self) -> str:
        return self._identity

    @property
    def fullname(self) -> str:
        return self._fullname

    @fullname.setter
    def fullname(self, fullname: str) -> None:
        self._fullname = fullname

    @property
    def accounts(self) -> tuple[Account, ...]:
        # a tuple copy, so callers cannot add or remove accounts behind the customer's back
        return tuple(self._accounts)

    def add_account(self, account: Account) -> None:
        self._accounts.append(account)

    def remove_account(self, account: Account) -> None:
        self._accounts.remove(account)

    def get_account(self, iban: str) -> Account | None:
        return next((account for account in self._accounts if account.iban == iban), None)
