import os 
from os import chdir

print('Open Script directory?')

y_input = input('[Y/n] ')

# Условие для input'а
if y_input == "Y" or "y":
  os.chdir('scripts')
  print('\n You opened script directory...')

  list_input = input('Press Enter to list scripts')
