"""
CUT: Class Under Test -> Account
MUT: Method Under Test
Unit test should follow four test phases:
1. Test Fixture/Setup
2. Call exercise method
3. Verification
4. Cleanup/Teardown

"""
import pytest

from banking.account import Account, AccountStatus, CheckingAccount, InsufficientBalanceException

non_positive_amounts = [0, -1, -1.10, -0.10, -10]
inactive_statuses = [AccountStatus.CLOSED, AccountStatus.BLOCKED]


@pytest.fixture
def an_active_account():
    return Account("TR1", 1_000, AccountStatus.ACTIVE)


@pytest.fixture
def an_active_checking_account():
    return CheckingAccount("TR2", 1_000, AccountStatus.ACTIVE, overdraft_amount=500)


@pytest.mark.parametrize("amount", non_positive_amounts)
def test_deposit_with_non_positive_amount_should_fail(an_active_account, amount):
    # 1. test fixture
    # 3. verification
    with pytest.raises(ValueError):
        # 2. call exercise method
        an_active_account.deposit(amount)


def test_deposit_should_increase_balance(an_active_account):
    new_balance = an_active_account.deposit(250)
    assert new_balance == 1_250
    assert an_active_account.balance == 1_250


@pytest.mark.parametrize("amount", non_positive_amounts)
def test_withdraw_with_non_positive_amount_should_fail(an_active_account, amount):
    with pytest.raises(ValueError):
        an_active_account.withdraw(amount)


def test_withdraw_should_decrease_balance(an_active_account):
    assert an_active_account.withdraw(1_000) == 0
    assert an_active_account.balance == 0


def test_withdraw_over_balance_should_fail_with_deficit(an_active_account):
    with pytest.raises(InsufficientBalanceException) as exc_info:
        an_active_account.withdraw(1_200)
    assert exc_info.value.deficit == 200
    assert an_active_account.balance == 1_000


@pytest.mark.parametrize("status", inactive_statuses)
def test_transactions_on_inactive_account_should_fail(an_active_account, status):
    an_active_account.status = status
    with pytest.raises(ValueError):
        an_active_account.deposit(100)
    with pytest.raises(ValueError):
        an_active_account.withdraw(100)


@pytest.mark.parametrize("status", [None, "ACTIVE", 100])
def test_setting_invalid_status_should_fail(an_active_account, status):
    with pytest.raises(ValueError):
        an_active_account.status = status


def test_checking_account_withdraw_within_overdraft_should_succeed(an_active_checking_account):
    assert an_active_checking_account.withdraw(1_500) == -500


def test_checking_account_withdraw_over_overdraft_should_fail_with_deficit(an_active_checking_account):
    with pytest.raises(InsufficientBalanceException) as exc_info:
        an_active_checking_account.withdraw(1_600)
    assert exc_info.value.deficit == 100
    assert an_active_checking_account.balance == 1_000


@pytest.mark.parametrize("status", inactive_statuses)
def test_checking_account_withdraw_on_inactive_account_should_fail(an_active_checking_account, status):
    an_active_checking_account.status = status
    with pytest.raises(ValueError):
        an_active_checking_account.withdraw(100)


@pytest.mark.parametrize("overdraft_amount", non_positive_amounts)
def test_setting_non_positive_overdraft_should_fail(an_active_checking_account, overdraft_amount):
    with pytest.raises(ValueError):
        an_active_checking_account.overdraft_amount = overdraft_amount
