from myBank import Account, total_balance, show_all, find_account_by_num

def test_total_balance():
    # Create some test accounts
    account1 = Account("John", 1000.0, "Savings")
    account2 = Account("Alice", 500.0, "Checking")

    # Calculate the expected total balance
    expected_total = account1.balance + account2.balance

    # Check if the calculated total matches the expected total
    assert total_balance() == expected_total

def test_show_all(capfd):
    # Create some test accounts
    account1 = Account("John", 1000.0, "Savings")
    account2 = Account("Alice", 500.0, "Checking")

    # Call show_all to display the accounts
    show_all()

    # Capture the printed output
    out, _ = capfd.readouterr()

    # Check if the printed output contains the account information
    assert "John" in out
    assert "Alice" in out
    assert "Savings" in out
    assert "Checking" in out

def test_find_account_by_num():
    # Create some test accounts
    account1 = Account("John", 1000.0, "Savings")
    account2 = Account("Alice", 500.0, "Checking")

    # Find an account by its account number
    found_account = find_account_by_num(account1.account_number)

    # Check if the found account matches the expected account
    assert found_account == account1

    # Try to find an account with an invalid account number
    invalid_account = find_account_by_num(999)

    # Check if the invalid account is None
    assert invalid_account is None


