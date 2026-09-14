"""
=================================================================
                    LEARN PYTHON — FROM ZERO TO OOP
=================================================================
This file is a single, self-contained Python course.

How to use it:
    1. Read a section's comments top to bottom.
    2. Run the file: `python main.py`
    3. Watch each section print its own demo output to the
       console, in order, with a clear header.
    4. Go back and tweak the code, break things, re-run — that's
       how you actually learn.

Table of contents (search for these headers in your editor):
    1. Python Fundamentals
    2. Data Types
    3. Operators
    4. Conditional Statements
    5. Loops
    6. Functions
    7. Lists, Tuples, Sets & Dictionaries
    8. Exception Handling
    9. File Handling
    10. Object-Oriented Programming
    11. Modules & Packages
    12. Virtual Environments (notes — not runnable code)
    13. Writing Clean & Reusable Code
=================================================================
"""

import math
import random
import os


def section(title: str) -> None:
    """Small helper used everywhere below to print a readable header
    before each demo runs. This is itself an example of writing a
    small reusable function instead of copy-pasting print() calls.
    """
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


# =================================================================
# 1. PYTHON FUNDAMENTALS
# =================================================================
def fundamentals_demo():
    section("1. PYTHON FUNDAMENTALS")

    # Variables: a name bound to a value. Python figures out the
    # type automatically — you don't declare it like int x = 5.
    name = "Jasmanjot"
    age = 21
    print("name:", name, "| age:", age)

    # Naming conventions — pick ONE style and stay consistent.
    pascal_case = "RarelyUsedForVariables"      # PascalCase -> classes
    camelCase = "seen in JS, less common here"  # camelCase
    snake_case = "the Python standard for variables/functions"
    print(pascal_case, "|", camelCase, "|", snake_case)

    # Comments: '#' for single line, triple quotes for multi-line
    # docstrings/notes (like the block at the very top of this file).

    # print() basics
    print("Hello, world!")                       # plain text
    print("a", "b", "c", sep=" -> ")              # custom separator
    print("no newline at the end", end=" | ")
    print("this prints right after")

    # f-strings: the modern, readable way to format text
    print(f"my name is {name} and I am {age} years old")

    # type() tells you what kind of value something is
    print("type of name:", type(name))
    print("type of age:", type(age))


# =================================================================
# 2. DATA TYPES
# =================================================================
def data_types_demo():
    section("2. DATA TYPES")

    # Numbers
    integer_value = -34
    float_value = 56.8
    complex_value = 3 + 4j
    boolean_value = True

    print("int:", integer_value, type(integer_value))
    print("float:", float_value, type(float_value))
    print("complex:", complex_value, type(complex_value))
    print("bool:", boolean_value, type(boolean_value))

    # Strings — sequences of characters, immutable
    text = "SHER CODER"
    print("full string:", text[::])          # slice copy of whole string
    print("reversed:", text[::-1])            # step = -1 reverses it
    print("upper/lower:", text.upper(), "|", text.lower())

    # Type conversion (casting) between types
    age_str = "23"
    age_int = int(age_str)                    # str -> int
    price_int = 12
    price_float = float(price_int)            # int -> float
    print("converted:", age_int, type(age_int), "|", price_float, type(price_float))

    # None represents "no value"
    nothing = None
    print("nothing:", nothing, type(nothing))


# =================================================================
# 3. OPERATORS
# =================================================================
def operators_demo():
    section("3. OPERATORS")

    a, b = 5, 32

    # Arithmetic operators
    print("a + b =", a + b)
    print("b - a =", b - a)
    print("a * b =", a * b)
    print("b / a =", b / a)     # true division -> float
    print("b // a =", b // a)   # floor division -> int result
    print("b % a =", b % a)     # modulus -> remainder
    print("a ** 3 =", a ** 3)   # exponent

    # Assignment / compound assignment operators
    counter = 20
    counter += 20   # same as counter = counter + 20
    counter -= 5
    counter *= 2
    counter //= 3
    print("counter after compound ops:", counter)

    # Comparison operators -> always return a bool
    x, y = 12.1, 12
    print(x == y, x != y, x > y, x < y, x >= y, x <= y)

    # Strings compare character by character using ASCII/unicode values
    print("ord('A') =", ord("A"))
    print("'ABC' > 'ACD' ->", "ABC" > "ACD")

    # Logical operators combine boolean expressions
    print(12 > 20 and 123 > 100)   # False (needs BOTH true)
    print(12 != 12 or 23 == 45 or 10 > 5)   # True (needs ONE true)
    print(not (12 == 12))          # flips True -> False


# =================================================================
# 4. CONDITIONAL STATEMENTS
# =================================================================
def conditionals_demo():
    section("4. CONDITIONAL STATEMENTS")

    # Basic if / else
    marks = 78
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    # if / elif / else chain — checked top to bottom, first match wins
    money = 20
    if money == 10:
        print("I'll have a choco bar")
    elif money == 20:
        print("I'll have a mango dolly")
    elif money == 30:
        print("I'll have a frosty")
    else:
        print("I'll have a plain cone")

    # Nested conditions
    num1, num2 = 15, 15
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are equal")

    # A practical example: leap year check (nested logic)
    year = 2028
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year} is NOT a leap year")
    elif year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")

    # Ternary (conditional) expression — a compact one-line if/else
    n = 7
    parity = "even" if n % 2 == 0 else "odd"
    print(f"{n} is {parity}")


# =================================================================
# 5. LOOPS
# =================================================================
def loops_demo():
    section("5. LOOPS")

    # --- for loop with range() ---
    print("Multiplication table of 5:")
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

    # --- for loop directly over a sequence ---
    word = "PYTHON"
    print("\nLetters in", word, ":")
    for letter in word:
        print(letter, end=" ")
    print()

    # --- while loop ---
    print("\nCounting down from 5:")
    n = 5
    while n > 0:
        print(n)
        n -= 1

    # --- break and continue ---
    print("\nStop at first number divisible by 7:")
    for i in range(1, 50):
        if i % 7 == 0:
            print("Found:", i)
            break

    print("\nSkip even numbers:")
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    # --- for...else: the else runs only if the loop was NOT broken ---
    numbers = [12, 13, 18, 15, 16]
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            print("\nList is not sorted")
            break
    else:
        print("\nList is sorted (loop completed without break)")

    # --- nested loops: classic pattern printing ---
    print("\nStar pyramid:")
    rows = 5
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    # --- accumulating a result: sum, factorial ---
    total = 0
    for i in range(1, 11):
        total += i
    print("\nSum of 1..10:", total)

    factorial = 1
    for i in range(1, 6):
        factorial *= i
    print("5! =", factorial)


# =================================================================
# 6. FUNCTIONS
# =================================================================
def greet(name):
    """A simple function: takes an input, does something, no return."""
    print(f"Hello, {name}!")


def add(a, b=10):
    """Functions can have default parameter values (b=10 if not given)."""
    return a + b


def describe_person(name, age, **extra_info):
    """*args collects extra positional args, **kwargs collects extra
    keyword args into a dictionary — handy for flexible functions."""
    print(f"{name} is {age} years old.")
    for key, value in extra_info.items():
        print(f"  {key}: {value}")


def is_palindrome(text):
    """A function that returns a value instead of printing it —
    generally preferred, since the caller decides what to do with it."""
    return text == text[::-1]


def factorial_recursive(n):
    """Recursion: a function that calls itself with a smaller problem
    until it hits a 'base case' that stops the recursion."""
    if n <= 1:          # base case
        return 1
    return n * factorial_recursive(n - 1)   # recursive case


def make_multiplier(factor):
    """Closures: an inner function 'remembers' variables from its
    enclosing function even after that function has returned."""
    def multiplier(x):
        return x * factor
    return multiplier


def logs_call(func):
    """A decorator: a function that wraps another function to add
    behavior before/after it runs, without changing its code."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@logs_call
def multiply(a, b):
    return a * b


def functions_demo():
    section("6. FUNCTIONS")

    greet("Jasmanjot")
    print("add(5):", add(5))                 # uses default b=10
    print("add(5, 20):", add(5, 20))          # overrides default

    describe_person("Akarsh", 23, designation="AI/ML", city="Jaipur")

    print("is_palindrome('NAMAN'):", is_palindrome("NAMAN"))
    print("is_palindrome('CURSOR'):", is_palindrome("CURSOR"))

    print("5! (recursive):", factorial_recursive(5))

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print("double(9):", double(9), "| triple(9):", triple(9))

    # lambda: a small, anonymous, one-expression function
    square = lambda x: x * x
    print("square(6):", square(6))

    # map/filter often pair with lambdas
    nums = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("doubled:", doubled, "| evens:", evens)

    multiply(6, 7)   # decorated function — prints logs automatically


# =================================================================
# 7. LISTS, TUPLES, SETS & DICTIONARIES
# =================================================================
def collections_demo():
    section("7. LISTS, TUPLES, SETS & DICTIONARIES")

    # ---------------- LISTS: ordered, mutable ----------------
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")          # add to end
    fruits.insert(1, "mango")      # add at index
    fruits.remove("banana")        # remove by value
    print("list:", fruits)
    print("slice fruits[1:3]:", fruits[1:3])

    numbers = [-45, 67, 12, -68, -69, 34]
    positives = [n for n in numbers if n >= 0]   # list comprehension
    print("positives (comprehension):", positives)
    print("average:", sum(numbers) / len(numbers))

    # ---------------- TUPLES: ordered, immutable ----------------
    point = (10, 20)
    single_item_tuple = (5,)       # note the trailing comma!
    print("tuple:", point, "| type:", type(point))
    scores = (90, 85, 90, 70, 90)
    print("count of 90 in tuple:", scores.count(90))

    # ---------------- SETS: unordered, unique items ----------------
    a_set = {1, 2, 3, 4, 5}
    b_set = {4, 5, 6, 7, 8}
    print("union:", a_set | b_set)
    print("intersection:", a_set & b_set)
    print("difference (a - b):", a_set - b_set)

    # ---------------- DICTIONARIES: key -> value pairs ----------------
    student = {"name": "Jasmanjot", "age": 21, "course": "B.Tech CSE"}
    student["year"] = 2027              # add/update a key
    del student["age"]                  # remove a key
    print("dict:", student)
    print("keys:", list(student.keys()))
    print("values:", list(student.values()))

    for key, value in student.items():
        print(f"  {key} -> {value}")

    # Dictionary comprehension
    squares = {i: i ** 2 for i in range(1, 6)}
    print("squares dict:", squares)

    # Common pattern: counting occurrences with a dict
    letters = "mississippi"
    counts = {}
    for ch in letters:
        counts[ch] = counts.get(ch, 0) + 1
    print("letter counts:", counts)


# =================================================================
# 8. EXCEPTION HANDLING
# =================================================================
class InvalidAgeError(Exception):
    """A custom exception. Defining your own exception classes makes
    error handling clearer and more specific than using generic ones."""
    pass


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        print(f"Can't divide by zero: {err}")
        return None
    except TypeError as err:
        print(f"Wrong type used: {err}")
        return None
    else:
        # runs only if the try block did NOT raise an exception
        print("Division succeeded with no errors")
        return result
    finally:
        # always runs, error or not — great for cleanup code
        print("safe_divide() finished running")


def check_age(age):
    if age < 10 or age > 18:
        raise InvalidAgeError("age must be between 10 and 18")
    return "Welcome to the club"


def exceptions_demo():
    section("8. EXCEPTION HANDLING")

    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    try:
        print(check_age(25))
    except InvalidAgeError as err:
        print(f"Custom exception caught: {err}")


# =================================================================
# 9. FILE HANDLING
# =================================================================
def file_handling_demo():
    section("9. FILE HANDLING")

    file_path = "demo_notes.txt"

    # 'with' automatically closes the file for you, even if an error
    # happens inside the block — always prefer it over manual open/close.
    with open(file_path, "w") as f:          # 'w' = write (overwrites)
        f.write("Learning Python step by step.\n")
        f.write("File handling is easy with 'with'.\n")

    with open(file_path, "a") as f:          # 'a' = append (adds to end)
        f.write("This line was appended.\n")

    with open(file_path, "r") as f:          # 'r' = read
        print("Full file content:")
        print(f.read())

    with open(file_path, "r") as f:
        print("Reading line by line:")
        for line in f:
            print(" ", line.strip())

    os.remove(file_path)   # cleanup so re-running this demo stays tidy
    print(f"\n('{file_path}' created, read, and cleaned up successfully)")

    # Common modes: 'r' read, 'w' write/overwrite, 'a' append, 'x' create
    # (fails if exists), and add 'b' for binary (e.g. 'rb', 'wb').


# =================================================================
# 10. OBJECT-ORIENTED PROGRAMMING
# =================================================================
class Animal:
    """A base/parent class showing attributes, __init__, and methods."""

    kingdom = "Animalia"   # class attribute — shared by all instances

    def __init__(self, name, sound):
        self.name = name         # instance attribute — unique per object
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def __str__(self):
        # controls what print(object) shows — a "dunder"/magic method
        return f"Animal(name={self.name})"


class Dog(Animal):
    """Inheritance: Dog reuses everything from Animal and adds/overrides."""

    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")   # call the parent's __init__
        self.breed = breed

    def make_sound(self):
        # Polymorphism: overriding the parent's method with new behavior
        print(f"{self.name} ({self.breed}) barks: {self.sound}!")


class BankAccount:
    """Encapsulation: hide internal state behind a leading double
    underscore, and only expose it through controlled methods/properties."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # "private" attribute (name-mangled)

    @property
    def balance(self):
        """A property lets you read __balance like an attribute:
        account.balance, while still going through this method."""
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @classmethod
    def from_dict(cls, data):
        """A classmethod is an alternate constructor — it receives the
        class itself (cls) instead of an instance (self)."""
        return cls(data["owner"], data["balance"])

    @staticmethod
    def currency_symbol():
        """A staticmethod doesn't need self or cls — it's just a
        function grouped inside the class for organization."""
        return "₹"


def oop_demo():
    section("10. OBJECT-ORIENTED PROGRAMMING")

    generic_animal = Animal("Some Creature", "...")
    generic_animal.make_sound()
    print(generic_animal)             # uses __str__

    my_dog = Dog("Bruno", "Labrador")
    my_dog.make_sound()               # overridden version runs
    print("Dog is also an Animal:", isinstance(my_dog, Animal))

    account = BankAccount("Jasmanjot", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance: {BankAccount.currency_symbol()}{account.balance}")

    account2 = BankAccount.from_dict({"owner": "Friend", "balance": 300})
    print("account2 owner:", account2.owner, "balance:", account2.balance)


# =================================================================
# 11. MODULES & PACKAGES
# =================================================================
def modules_demo():
    section("11. MODULES & PACKAGES")

    # A module is just a .py file; a package is a folder of modules
    # with an __init__.py. You import standard-library modules like this:
    print("math.sqrt(81):", math.sqrt(81))
    print("math.pi:", round(math.pi, 4))
    print("random.randint(1, 6):", random.randint(1, 6))

    # To use your OWN module, e.g. a file called helpers.py with:
    #     def add(a, b): return a + b
    # you would write, from the same folder:
    #     import helpers
    #     from helpers import add
    #
    # For a package (folder), you'd structure it like:
    #     mypackage/
    #         __init__.py
    #         helpers.py
    # and import with: from mypackage import helpers
    #
    # `if __name__ == "__main__":` (used at the bottom of this file)
    # ensures code only runs when the file is executed directly —
    # not when it's imported by another file. That's exactly why all
    # the demo calls below are wrapped in that check.

    # Installing third-party packages (run in your terminal, not here):
    #     pip install requests
    #     pip install pandas numpy


# =================================================================
# 12. VIRTUAL ENVIRONMENTS  (notes — these are terminal commands,
#                             not Python code, so they're comments)
# =================================================================
"""
A virtual environment is an isolated folder with its own Python
interpreter and installed packages, so different projects don't
fight over conflicting package versions.

Create one:
    python -m venv venv

Activate it:
    Windows        : venv\\Scripts\\activate
    macOS / Linux  : source venv/bin/activate

Install packages inside it:
    pip install requests pandas

Save your project's exact dependencies:
    pip freeze > requirements.txt

Recreate the same environment elsewhere:
    pip install -r requirements.txt

Leave the virtual environment:
    deactivate
"""


# =================================================================
# 13. WRITING CLEAN & REUSABLE CODE
# =================================================================
def celsius_to_fahrenheit(celsius: float) -> float:
    """Good practice checklist demonstrated by this one small function:

    - Descriptive name (celsius_to_fahrenheit, not 'convert' or 'f').
    - Type hints (celsius: float, -> float) document intent.
    - A docstring explains WHAT it does and WHY, not just how.
    - Does exactly ONE thing (single responsibility).
    - No hardcoded/magic numbers left unexplained (9/5 and 32 are the
      standard, well-known conversion constants here).
    - Returns a value instead of printing, so callers can reuse it
      for something other than a print statement.
    """
    return (celsius * 9 / 5) + 32


def clean_code_demo():
    section("13. WRITING CLEAN & REUSABLE CODE")

    for temp_c in [0, 20, 37, 100]:
        print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")

    print("""
Quick principles worth internalizing:
  - Follow PEP 8 (Python's style guide): snake_case for variables and
    functions, PascalCase for classes, 4 spaces per indent level.
  - DRY: Don't Repeat Yourself — if you copy-paste code, consider a
    function or loop instead.
  - Small functions, one job each, are easier to test and reuse.
  - Meaningful names beat comments explaining bad names.
  - Handle errors explicitly (see section 8) instead of letting a
    program crash silently or unpredictably.
  - Keep related code together in modules; keep unrelated code apart.
""")


# =================================================================
# RUN ALL DEMOS IN ORDER
# =================================================================
if __name__ == "__main__":
    fundamentals_demo()
    data_types_demo()
    operators_demo()
    conditionals_demo()
    loops_demo()
    functions_demo()
    collections_demo()
    exceptions_demo()
    file_handling_demo()
    oop_demo()
    modules_demo()
    clean_code_demo()

    section("DONE")
    print("You just ran a full tour of Python fundamentals through OOP.")
    print("Re-read each section, then try changing values and re-running.")
