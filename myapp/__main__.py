from model.user import *
from model.developer import *

if __name__ == '__main__':
  x = User('Vlad', 'Melekhin')
  print(x.toString())

  dev1 = Developer('Vlad', 'Melekhin', 'TypeScript')
  print(dev1.toString())