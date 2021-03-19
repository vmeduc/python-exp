from . import user

class Developer(user.User):

  progrLang: str

  def __init__(self, firstName: str, lastName: str, progrLang: str):
    self.progrLang = progrLang
    super().__init__(firstName, lastName)

  def toString(self) -> str:
    return self.firstName + ' ' \
      + self.lastName + ' (lang: ' \
      + self.progrLang + ')'