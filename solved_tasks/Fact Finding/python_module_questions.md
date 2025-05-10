1. **What are a list and tuple in Python, and what are some examples?**

A **list** in Python is an ordered, changeable (mutable) collection that allows duplicate elements. Lists are created using square brackets `[]`. Example:

```python
my_list = ["apple", "banana", "cherry"]
```

You can modify, add, or remove items from a list after it is created.

A **tuple** is also an ordered collection, but it is unchangeable (immutable) after creation. Tuples are created using parentheses `()`. Example:

```python
my_tuple = ("apple", "banana", "cherry")
```

Tuples also allow duplicate values, but you cannot add, remove, or change items after creation.

---

2. **What is a namespace in Python?**

A **namespace** is a container that maps names (identifiers) to objects. It works like a dictionary, where each key is a name and the value is the object itself. Namespaces help organize variables, functions, and classes, preventing naming conflicts by allowing the same name to exist in different namespaces (e.g., local, global, built-in).

---

3. **What is the difference between a local variable and a global variable?**

- **Local Variable**: Declared inside a function and accessible only within that function. Its lifetime is limited to the function's execution.
- **Global Variable**: Declared outside any function and accessible throughout the entire program. Its lifetime spans the execution of the whole program.

| Basis | Local Variable | Global Variable |
| :-- | :-- | :-- |
| Declaration | Inside a function | Outside all functions |
| Scope | Only within the function | Entire program |
| Lifetime | Created/destroyed with function call | Exists as long as the program runs |
| Data Sharing | Not shared between functions | Shared across functions |


---

4. **What is an IDE, and what are some common IDEs that could be used with Python?**

An **IDE** (Integrated Development Environment) is an application that combines tools for writing, editing, debugging, and running code in one place. It typically includes features like syntax highlighting, code completion, debugging tools, and project management.

**Common Python IDEs:**

- PyCharm
- Visual Studio Code (VS Code)
- Spyder
- Thonny
- IDLE

---

5. **What are modules in Python, and what are some examples?**

A **module** is a file containing Python code (functions, variables, classes) that can be imported and reused in other programs. Modules help organize code into separate files for better structure and reusability.

**Examples:**

- Built-in modules: `math`, `random`, `os`, `sys`
- User-defined module: A file named `mymodule.py` with custom functions and variables.

Usage example:

```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```


---

6. **What is the difference between an array and a list?**

- **List**: Built-in Python data type, can hold items of different types (e.g., integers, strings, objects), and can be resized dynamically.
- **Array**: Typically refers to the `array` module's array, which is more efficient for large collections of numeric data but can only store elements of the same type. Lists are more flexible, while arrays are more memory-efficient for homogeneous data.

---

7. **What are operators, and what are some examples?**

**Operators** are special symbols or keywords that perform operations on one or more operands (values or variables).

**Examples:**


| Operator | Name | Example | Description |
| :-- | :-- | :-- | :-- |
| + | Addition | `a + b` | Adds two values |
| - | Subtraction | `a - b` | Subtracts right from left |
| * | Multiplication | `a * b` | Multiplies two values |
| / | Division | `a / b` | Divides left by right |
| % | Modulus | `a % b` | Remainder of division |
| == | Equal to | `a == b` | Checks if values are equal |
| and | Logical AND | `a and b` | True if both are True |

Other operator categories include assignment, comparison, logical, identity, membership, and bitwise operators.

