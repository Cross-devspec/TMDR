import os
import random

from time import sleep


input_staff = input("Вы хотите использовать УСТАНОВЩИК службы? [Y/n]: ")
file_path = input(r"Введите путь к скриптам: ")

script_staff = 0
for i in range(1, 11):

  var = script_staff + 1
  sleep(random.uniform(0.01, 1))
  print(var + os.listdir(file_path))
  
