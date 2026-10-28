"""
CUT: Bank
The get_account tests isolate Bank from Customer: every Customer.get_account is replaced
by a mock, so a failure there points at Bank and not at Customer.
"""
import pytest

from module03.banking.account import Account
from module03.banking.bank import Bank
from module03.banking.customer import Customer

# region accounts
# the accounts each (mocked) customer owns, keyed by iban
accounts_by_customer = {
    "jack bauer": {"tr1": Account("tr1", 100_000), "tr2": Account("tr2", 200_000)},
    "kate austen": {"tr3": Account("tr3", 300_000), "tr4": Account("tr4", 400_000)},
    "james sawyer": {"tr5": Account("tr5", 500_000), "tr6": Account("tr6", 600_000)},
}
all_accounts = {iban: account
                for accounts in accounts_by_customer.values()
                for iban, account in accounts.items()}
# endregion


@pytest.fixture
def an_empty_bank():
    return Bank("isbankasi")


@pytest.fixture
def a_bank(mocker):
    bank = Bank("isbankasi")
    for identity, (fullname, accounts) in enumerate(accounts_by_customer.items(), start=1):
        customer = bank.create_customer(str(identity), fullname)
        # dict.get returns None for an unknown iban, just like Customer.get_account
        mocker.patch.object(customer, "get_account", side_effect=accounts.get)
    return bank


@pytest.mark.parametrize("iban", ["tr1", "tr4", "tr6"])
def test_get_account_should_success(a_bank, iban):
    # 2. call exercise method
    found_account = a_bank.get_account(iban)
    # 3. verification
    assert found_account is not None
    assert found_account.iban == iban
    assert found_account is all_accounts[iban]


def test_get_account_should_return_none(a_bank):
    # 2. call exercise method
    found_account = a_bank.get_account("tr7")
    # 3. verification
    assert found_account is None


def test_get_account_on_bank_without_customers_should_return_none(an_empty_bank):
    assert an_empty_bank.get_account("tr1") is None


def test_new_bank_should_have_name_and_no_customers(an_empty_bank):
    assert an_empty_bank.name == "isbankasi"
    assert an_empty_bank.customers == ()


def test_create_customer_should_register_customer(an_empty_bank):
    # 2. call exercise method
    customer = an_empty_bank.create_customer("1", "jack bauer")
    # 3. verification
    assert isinstance(customer, Customer)
    assert customer.identity == "1"
    assert customer.fullname == "jack bauer"
    assert an_empty_bank.customers == (customer,)
