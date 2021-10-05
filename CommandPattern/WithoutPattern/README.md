# This is the example without the usage of the command pattern
There are certain violations of the SOLID principles:
* Violates Single Responsibility Principle
    *   Parsing and executing the commands are separate concerns 
* Violates Open/Closed Principle
    *   In order to add/remove commands you have to modify the implementation
* Violates Dependency Inversion Principle
    *   The main class depends on the concrete implementation of the CommandExecutor

Another hint of bad code:
* Long list of if/elif clauses