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

from module03.banking.account import Account, AccountStatus, CheckingAccount, InsufficientBalanceException

non_positive_amounts = [0, -1, -1.10, -0.10, -10]
inactive_statuses = [AccountStatus.CLOSED, AccountStatus.BLOCKED]


@pytest.fixture
def an_active_account():
    return Account("TR1", 1_000, AccountStatus.ACTIVE)


@pytest.fixture
def an_active_checking_account():
    return CheckingAccount("TR2", 1_000, AccountStatus.ACTIVE, overdraft_amount=500)


def test_new_account_should_expose_its_state(an_active_account):
    assert an_active_account.iban == "TR1"
    assert an_active_account.balance == 1_000
    assert an_active_account.status == AccountStatus.ACTIVE


def test_new_account_should_use_default_balance_and_status():
    account = Account("TR3")
    assert account.balance == 5_000
    assert account.status == AccountStatus.ACTIVE


def test_str_should_describe_account(an_active_account):
    assert str(an_active_account) == "Account: iban: TR1, balance: 1000, status: AccountStatus.ACTIVE"


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


def test_insufficient_balance_exception_should_carry_its_message(an_active_account):
    # match= checks str(exception), so the message must reach Exception.__init__
    with pytest.raises(InsufficientBalanceException, match="does not cover your expenses") as exc_info:
        an_active_account.withdraw(1_200)
    assert exc_info.value.message == "Your balance does not cover your expenses"


@pytest.mark.parametrize("status", list(AccountStatus))
def test_setting_valid_status_should_succeed(an_active_account, status):
    an_active_account.status = status
    assert an_active_account.status == status


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


def test_new_checking_account_should_use_default_overdraft():
    assert CheckingAccount("TR4").overdraft_amount == 1_000


def test_str_should_describe_checking_account(an_active_checking_account):
    assert str(an_active_checking_account) == (
        "CheckingAccount: iban: TR2, balance: 1000, status: AccountStatus.ACTIVE, overdraft_amount: 500"
    )


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


def test_setting_positive_overdraft_should_extend_available_funds(an_active_checking_account):
    an_active_checking_account.overdraft_amount = 2_000
    assert an_active_checking_account.overdraft_amount == 2_000
    assert an_active_checking_account.withdraw(3_000) == -2_000
