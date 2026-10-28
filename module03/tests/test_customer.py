"""
CUT: Customer
"""
import pytest

from module03.banking.account import Account
from module03.banking.customer import Customer


@pytest.fixture
def two_accounts():
    return Account("tr1", 100_000), Account("tr2", 200_000)


@pytest.fixture
def a_customer(two_accounts):
    customer = Customer("1", "jack bauer")
    for account in two_accounts:
        customer.add_account(account)
    return customer


def test_new_customer_should_have_identity_fullname_and_no_accounts():
    customer = Customer("2", "kate austen")
    assert customer.identity == "2"
    assert customer.fullname == "kate austen"
    assert customer.accounts == ()


def test_fullname_should_be_updatable(a_customer):
    a_customer.fullname = "jack shephard"
    assert a_customer.fullname == "jack shephard"


def test_add_account_should_keep_insertion_order(a_customer, two_accounts):
    assert a_customer.accounts == two_accounts


@pytest.mark.parametrize("iban", ["tr1", "tr2"])
def test_get_account_should_find_account_by_iban(a_customer, iban):
    # 2. call exercise method
    found_account = a_customer.get_account(iban)
    # 3. verification
    assert found_account is not None
    assert found_account.iban == iban


def test_get_account_with_unknown_iban_should_return_none(a_customer):
    assert a_customer.get_account("tr3") is None


def test_remove_account_should_forget_account(a_customer, two_accounts):
    first, second = two_accounts
    a_customer.remove_account(first)
    assert a_customer.accounts == (second,)
    assert a_customer.get_account("tr1") is None


def test_remove_unknown_account_should_fail(a_customer):
    with pytest.raises(ValueError):
        a_customer.remove_account(Account("tr3"))


def test_accounts_should_be_a_read_only_snapshot(a_customer, two_accounts):
    snapshot = a_customer.accounts
    a_customer.add_account(Account("tr3"))
    assert snapshot == two_accounts
    assert len(a_customer.accounts) == 3
