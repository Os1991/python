from sys import argv

script_params_test, hours, rate, bonus = argv
print((int(hours)*int(rate))+int(bonus))