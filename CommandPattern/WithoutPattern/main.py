import sys
from commandExecutor import CommandExecutor

print("Please enter your command!")
command = input()

if len(command) < 2:
    print ('Usage:')
    print('Commands:')
    print('\t CreateOrder')
    print('\t UpdateQuantity number')
    print('\t ShipOrder')
    exit()

executor = CommandExecutor()
executor.executeCommand(command.split())