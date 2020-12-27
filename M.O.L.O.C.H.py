import string
import random
import time
import os
import sys
import codecs

ascii_table = string.ascii_letters
debug = False

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def matrixify(n):
    if not debug:
        for i in range(n*2):
            print(random.choice(string.ascii_letters), end='')
            sys.stdout.flush()
            time.sleep(0.001)
        print('')

cls()
matrixify(2000)
time.sleep(1)
input("\nPress Enter to continue...")
cls()
time.sleep(1)

print('\nProperty of [RETHINK ROBOTICS], do not execute without permission.\n')
time.sleep(1)

input("Press Enter to continue...")

login = None
true_login = 'rudy102'
login_list = [true_login.lower(), true_login.upper(), ''.join(true_login.split(' ')), true_login]

login = input('\nLogin: ')
while ''.join(login.lower().split(' ')) not in login_list:
    print('\nWrong login. Please try again.')
    login = input('\nLogin: ')

cls()

login = None
true_login = None
with open('cipher', 'r') as f:
    true_login = codecs.encode(f.read(), 'rot13') 
login_list = [true_login.lower(), true_login.upper(), ''.join(true_login.split(' ')), true_login]

login = input('\nWelcome Konrad, please enter your password: ')
while ''.join(login.lower().split(' ')) not in login_list:
    print('\nWrong password. Please try again.')
    login = input('\nPassword: ')

cls()
matrixify(1000)
time.sleep(1)
input("\nPress Enter to continue...")
cls()

print('\n\t\\RETHINK\\')
print('\t\t\\ROBOTICS\\\n')
time.sleep(1)
print('\tWe are fighing for a brighter future!\n\n')

time.sleep(1)
print('\nWelcome to MOLOCH project mainframe.') 
print('Before progressing further, please verify that the computer is connected to the Large Antenna System.\n')
print('Please ask systems admin (Game Master) for permission before proceeding.\n')

time.sleep(20)
input("If the computer is plugged, press Enter to continue...")
cls()

time.sleep(1)

print('\n\t\\RETHINK\\')
print('\t\t\\ROBOTICS\\\n')
print('\tWe are fighing for a brighter future!\n\n')

time.sleep(1)
print('\nWelcome to MOLOCH project mainframe. Do you want to disable the machines?\n')

login = None
true_login = 'yes'
login_list = [true_login.lower(), true_login.upper(), ''.join(true_login.split(' ')), true_login]

login = input('\nyes/no: ')
while login.lower() not in login_list:
    login = input('yes/no: ')

time.sleep(1)
cls()
time.sleep(3)
matrixify(7000)
cls()
time.sleep(3)

while True:
    time.sleep(0.5)
    print('\n\n\tALL\n')
    time.sleep(0.2)
    print('\tSYSTEMS\n')
    time.sleep(0.2)
    print('\tDEACTIVATED')
    time.sleep(2)
    cls()