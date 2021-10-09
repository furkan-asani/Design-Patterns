# What is the singleton pattern?
* Creational pattern
* Ensures that a class has only ine instance
* Controls access to a limited resource
    +   Device access like a printer
    +   Buffer pools
    +   Web/DB connection pools
* Global point of access
* Lazy instantiation

# Why are Singletons dangerous? Some implementations more than others...
* Violates Single Responsibility Principle
* Non standard class access
* Harder to test

# Advantages
* Provides controlled access to a single instance
* Reduces the global namespace
* More flexibility than with a static class