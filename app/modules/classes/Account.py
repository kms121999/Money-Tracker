from decimal import Decimal

def test_decimal(x):
  if type(x) != Decimal:
      raise TypeError("Expected Decimal type.")

class Account:
  def __init__(self, account_name, account_properties):
    """ Account
    str account_name - display name of the account
    ??? account_properties - ###!!! what data type is account properties?
    """
    
    self.name = account_name
    self.properties = account_properties ###!!!
    
    self.balance = Decimal("0.00")
    
    self.transactions = set()

    
  def __add__(self, amount):
    test_decimal(amount)
    self.balance += amount
    return True
    
  def __sub__(self, amount):
    test_decimal(amount)
    self.balance -= amount
    return True
