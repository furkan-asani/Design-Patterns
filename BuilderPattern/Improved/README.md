# What are the advantages using the command pattern?
* No duplicate code which would make it hard to maintain
* It is open for extensibility
* It depends on an interface instead of an actual implementation
* The concerns are separated -> building, representing, order of assembly
# How does the builder pattern work in this scenario?
Separate the building from the orchestration 
-> 
* Separate classes for building the computer <br>
* Separate class for the orchestration of the build process <br>

In order to build different computers without having to replicate code we have to create an AbstractBuilder Class.