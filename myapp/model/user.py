class User(object): 
  
  firstName: str
  lastName: str

  def __init__(self, firstName: str, lastName: str):
    self.firstName = firstName
    self.lastName = lastName

  def fullName(self) -> str:
    return self.firstName + ' ' + self.lastName
  
  def toString(self) -> str:
    return self.fullName()