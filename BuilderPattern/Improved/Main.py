from Director import Director
from MyComputerBuilder import MyComputerBuilder

computerBuilder = Director(MyComputerBuilder())
computerBuilder.buildComputer()
computer = computerBuilder.getComputer()
computer.display()
