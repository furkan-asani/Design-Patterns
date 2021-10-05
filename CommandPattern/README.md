# Command Pattern

It's a behavioral pattern which allows you to elegantly add new commands or option to your programm without having to touch already existing implementation

# Example for the Command Pattern

We are creating a command line interface for creating, updating or shipping orders.
</br>
We want to ensure extensibility in case there is a new functionality we want to implement
</br>
The arguments typed into the console shall be parsed.
</br>
If the typed command is supported it should also be executed and notify the user.
