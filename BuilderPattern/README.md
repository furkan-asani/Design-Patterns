# Builder Pattern

The builder pattern is a creational pattern(it's used to create an object)<br>
It separates construction from it's representation, assembly order, etc.<br>
->
The builder pattern separates the "How" from the "What".
## When to use the builder pattern?
- Too many parameters when constructing an object
- When an assembly order is needed which could potentially differ

## Example
We are creating a computer builder which could potentially <br>
assemble any product configuration we want. Which means it has <br>
to be extensible for new computer configurations without having <br>
to touch already existing code.