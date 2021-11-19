import decimal

class Transaction:
  def __init__(self, amount, from_account, to_account, description, notes=None):
    """
    decimal: amount
    account: from_account
    account: to_account
    str: description
    str: notes
    """
    
    self.amount = amount
    self.from_account = from_account
    self.to_account = to_account
    
    self.description = description
    self.notes = notes if notes else ""
