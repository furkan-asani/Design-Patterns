from UpdateOrder import UpdateOrder
from CreateOrder import CreateOrder
from ShipOrder import ShipOrder
from NoCommand import NoCommand

def getCommands():
    commands = (UpdateOrder, CreateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)

def printUsage(commands):
    print('Usage: python -m Command CommandName [arguments]')
    print('Commands:')
    for command in commands.values:
        print ('    %s' % command.description)

def parseCommand(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)

print('Please enter your desired command!\n')
inputCommand = input()
commands = getCommands()
if len(inputCommand) < 2:
    printUsage(commands)
    exit()

command = parseCommand(commands, inputCommand.split(' '))
command.execute()