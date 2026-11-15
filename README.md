# Python Learning Journey 🐍

A structured, chapter-wise collection of Python notes, examples and practice programs, written while learning Python from scratch. Each chapter lives in its own folder with numbered `.py` files — the number reflects the order topics were covered.

The journey starts with variables, operators and strings, moves through data structures, loops, functions and file handling, and then into object-oriented programming, error handling and iterators. Course notes and beginner mini projects sit alongside the chapters.

> 📌 Click any chapter or file link below to jump straight to that folder/file in this repo.

---

## Table of Contents

| # | Chapter | Topics Covered |
|---|---------|-----------------|
| 01 | [Basics of Python](<Chapter%20-%2001>) | Print statements, arithmetic, variables, data types, operators, type conversion, inputs, unary & membership operators |
| 02 | [Strings & Conditionals](<Chapter%20-%2002>) | Strings, indexing, slicing, string functions, conditional statements, f-strings & `.format()` |
| 03 | [Lists & Tuples](<Chapter%20-%2003>) | Lists, nested lists, list slicing, list methods, tuples, tuple slicing, tuple methods |
| 04 | [Dictionaries & Sets](<Chapter%20-%2004>) | Dictionaries, nested dictionaries, dictionary methods, sets, set methods |
| 05 | [Loops](<Chapter%20-%2005>) | while loop, break & continue, for loop, `range()`, `pass` statement |
| 06 | [Functions](<Chapter%20-%2006>) | Functions, function types, default parameters, recursion |
| 07 | [File Handling](<Chapter%20-%2007>) | Open/read/close files, write & append modes, `with` statement, deleting files |
| 08 | [OOP Basics](<Chapter%20-%2008>) | OOP intro, constructors & `self`, class vs instance attributes, methods, static methods, abstraction, encapsulation |
| 09 | [OOP - Inheritance & Polymorphism](<Chapter%20-%2009>) | `del` keyword, public/private members, inheritance (single, multi-level, multiple), `super()`, class methods, `@property`, polymorphism & operator overloading |
| 10 | [Modern Python & Error Handling](<Chapter%20-%2010>) | Walrus operator, type hints, match-case, dict merge & update operators, exception handling (try/except/else/finally, raise), `if __name__ == "__main__"`, `global`, `enumerate()`, list comprehensions |
| 11 | [Misc / Advanced Topics](<Chapter%20-%2011>) | Virtual environments (placeholder), lambda functions, `join()`, `.format()`, map/filter/reduce |
| 12 | [Iterators & Iterables](<Chapter%20-%2012>) | Iteration, iterables vs iterators, iterator protocol, how the `for` loop works, custom iterators, `itertools.islice` |
| 13 | [Course Notes](<Course_Notes>) | Modules & imports, `random` module, variable scope, debugging techniques |
| 14 | [Fundamentals (Mini Projects)](<Fundamentals>) | Beginner projects: band name generator, tip calculator, conditionals (pizza, rollercoaster, treasure island), rock paper scissors, password generator, hangman, Caesar cipher, secret auction, calculator, blackjack, number guessing game, higher/lower |

---

## Chapter Details

### [Chapter - 01: Basics of Python](<Chapter%20-%2001>)

- [01_first_program.py](<Chapter%20-%2001/01_first_program.py>) — First program: `print()`, arithmetic operations, variables and strings, data types, comments
- [02_operators.py](<Chapter%20-%2001/02_operators.py>) — Arithmetic operators (`+ - * / // % **`), common uses of modulo, operator precedence, comparison and assignment operators
- [03_type_conversion.py](<Chapter%20-%2001/03_type_conversion.py>) — Implicit conversion and manual type casting
- [04_inputs.py](<Chapter%20-%2001/04_inputs.py>) — Taking user input (`input()` returns a string by default) and casting it
- [05_Practice.py](<Chapter%20-%2001/05_Practice.py>) — Practice questions: sum of two numbers, area of a square, average of two floats, comparing two integers
- [06_unary_operators.py](<Chapter%20-%2001/06_unary_operators.py>) — Unary operators (`+x`, `-x`, `not x`, `~x`)
- [08_membership_operators.py](<Chapter%20-%2001/08_membership_operators.py>) — Membership operators (`in`, `not in`), in conditions and in `for` loops
- [bin.py](<Chapter%20-%2001/bin.py>) — Empty scratch file

### [Chapter - 02: Strings & Conditionals](<Chapter%20-%2002>)

- [01_strings.py](<Chapter%20-%2002/01_strings.py>) — String creation (single, double and triple quotes), escape sequences, concatenation, `len()`
- [02_indexing.py](<Chapter%20-%2002/02_indexing.py>) — String indexing
- [03_slicing.py](<Chapter%20-%2002/03_slicing.py>) — String slicing, including negative indexing
- [04_functions.py](<Chapter%20-%2002/04_functions.py>) — String functions: `endswith()`, `capitalize()`, `replace()`, `find()`, `count()`
- [05_Practice_1.py](<Chapter%20-%2002/05_Practice_1.py>) — Practice questions: length of a name, counting `$` in a string
- [06_conditional_stat.py](<Chapter%20-%2002/06_conditional_stat.py>) — `if` / `elif` / `else`, grading examples, logical operators in conditions, nesting
- [07_Practice_2.py](<Chapter%20-%2002/07_Practice_2.py>) — Practice questions: odd or even, greatest of three numbers, multiple of 7
- [08_f_string.py](<Chapter%20-%2002/08_f_string.py>) — String formatting: concatenation, `.format()` (positional and named), number formatting, f-strings
- [conditional_statement.png](<Chapter%20-%2002/conditional_statement.png>) — Flowchart of a simple if/else decision (height check)
- [nested.png](<Chapter%20-%2002/nested.png>) — Flowchart of nested conditions (height check, then age-based ticket price)
- [bin.py](<Chapter%20-%2002/bin.py>) — Empty scratch file

### [Chapter - 03: Lists & Tuples](<Chapter%20-%2003>)

- [01_list_basics.py](<Chapter%20-%2003/01_list_basics.py>) — Creating lists, indexing, mutability, dynamic size
- [02_list_types_and_nested_lists.py](<Chapter%20-%2003/02_list_types_and_nested_lists.py>) — Homogeneous, heterogeneous, empty and nested lists
- [03_list_slicing.py](<Chapter%20-%2003/03_list_slicing.py>) — List slicing, including negative indexes
- [04_list_methods.py](<Chapter%20-%2003/04_list_methods.py>) — `append()`, `extend()`, `sort()`, `reverse()`, `insert()`, `remove()`, `pop()`, `copy()`, plus `random.choice()`, `choices()` and `randint()` with lists
- [05_tuples.py](<Chapter%20-%2003/05_tuples.py>) — Tuples: indexing, immutability, empty and single-element tuples
- [06_tuples_slicing.py](<Chapter%20-%2003/06_tuples_slicing.py>) — Tuple slicing
- [07_tuples_method.py](<Chapter%20-%2003/07_tuples_method.py>) — Tuple methods: `index()`, `count()`
- [08_Practice.py](<Chapter%20-%2003/08_Practice.py>) — Practice questions: favourite movies list, palindrome check using `copy()`, counting "A" grades in a tuple, sorting grades
- [bin.py](<Chapter%20-%2003/bin.py>) — Empty scratch file

### [Chapter - 04: Dictionaries & Sets](<Chapter%20-%2004>)

- [01_dictionary.py](<Chapter%20-%2004/01_dictionary.py>) — Key–value pairs, accessing, adding and updating items, empty dictionaries, looping through a dictionary
- [02_nested_dict.py](<Chapter%20-%2004/02_nested_dict.py>) — Nested dictionaries (lists and dictionaries as values)
- [03_dict_methods.py](<Chapter%20-%2004/03_dict_methods.py>) — `keys()`, `values()`, `items()`, `get()`, `update()`
- [04_set.py](<Chapter%20-%2004/04_set.py>) — Sets: unordered and unique elements, empty set vs empty dictionary
- [05_set_methods.py](<Chapter%20-%2004/05_set_methods.py>) — `add()`, `remove()`, `pop()`, `clear()`, `union()`, `intersection()`
- [06_Practice.py](<Chapter%20-%2004/06_Practice.py>) — Practice questions: word-meanings dictionary, counting unique subjects, marks dictionary, storing `9` and `9.0` in one set
- [bin.py](<Chapter%20-%2004/bin.py>) — Empty scratch file

### [Chapter - 05: Loops](<Chapter%20-%2005>)

- [01_while_loop.py](<Chapter%20-%2005/01_while_loop.py>) — `while` loop, iteration, avoiding infinite loops
- [02_Practice_1.py](<Chapter%20-%2005/02_Practice_1.py>) — Practice questions: print 1–100 and 100–1, multiplication table, traversing a list
- [03_break_n_continue.py](<Chapter%20-%2005/03_break_n_continue.py>) — `break` and `continue`
- [04_for.py](<Chapter%20-%2005/04_for.py>) — `for` loop over sequences, `for … else`
- [05_Practice_2.py](<Chapter%20-%2005/05_Practice_2.py>) — Practice questions: printing list elements, linear search in a tuple
- [06_range.py](<Chapter%20-%2005/06_range.py>) — `range(start, stop, step)`
- [07_Practice_3.py](<Chapter%20-%2005/07_Practice_3.py>) — Practice questions: 1–100, 100–1 and a multiplication table using `for` and `range()`
- [08_pass.py](<Chapter%20-%2005/08_pass.py>) — `pass` statement
- [09_Practice_4.py](<Chapter%20-%2005/09_Practice_4.py>) — Practice questions: sum of first n natural numbers (`while`), factorial (`for`)
- [bin.py](<Chapter%20-%2005/bin.py>) — Empty scratch file

### [Chapter - 06: Functions](<Chapter%20-%2006>)

- [01_functions.py](<Chapter%20-%2006/01_functions.py>) — Defining and calling functions, parameters and arguments, `print()` vs `return`
- [02_fun_type.py](<Chapter%20-%2006/02_fun_type.py>) — Built-in vs user-defined functions
- [03_default_parameters.py](<Chapter%20-%2006/03_default_parameters.py>) — Return values (`None` when nothing is returned) and default parameters
- [04_Practice_1.py](<Chapter%20-%2006/04_Practice_1.py>) — Practice questions: list length, printing list elements, factorial, USD to INR, odd/even, leap year
- [05_recursion.py](<Chapter%20-%2006/05_recursion.py>) — Recursion: base case and recursive case
- [06_Practice_2.py](<Chapter%20-%2006/06_Practice_2.py>) — Practice questions: recursive sum of first n numbers, recursive list printing, call-stack push/pop order
- [bin.py](<Chapter%20-%2006/bin.py>) — Empty scratch file

### [Chapter - 07: File Handling](<Chapter%20-%2007>)

- [01_open,read.py](<Chapter%20-%2007/01_open%2Cread.py>) — Opening files, file modes, `read()`, `readline()`, `close()`
- [02_write&append.py](<Chapter%20-%2007/02_write%26append.py>) — Write mode (`"w"`) and the read/write and append modes (`"r+"`, `"w+"`, `"a+"`)
- [03_with.py](<Chapter%20-%2007/03_with.py>) — The `with` statement for safe file handling
- [04_deleting.py](<Chapter%20-%2007/04_deleting.py>) — Deleting files with `os.remove()`
- Sample data files used by the programs above:
  - [1_demo1.txt](<Chapter%20-%2007/1_demo1.txt>) — Used by `01_open,read.py`
  - [2_demo1.txt](<Chapter%20-%2007/2_demo1.txt>) — Used by `02_write&append.py`
  - [2_demo2.txt](<Chapter%20-%2007/2_demo2.txt>) — Used by `02_write&append.py`
  - [2_demo3.txt](<Chapter%20-%2007/2_demo3.txt>) — Used by `02_write&append.py`
  - [2_demo4.txt](<Chapter%20-%2007/2_demo4.txt>) — Used by `02_write&append.py`
  - [3_demo1.txt](<Chapter%20-%2007/3_demo1.txt>) — Used by `03_with.py`
  - [4_Delete.txt](<Chapter%20-%2007/4_Delete.txt>) — Used by `04_deleting.py`
- [Learning](<Chapter%20-%2007/Learning>) — Saved reference link on file open modes (Stack Overflow)
- [Practice/](<Chapter%20-%2007/Practice>) — Practice questions on file handling
  - [Question1.py](<Chapter%20-%2007/Practice/Question1.py>) — Create a file, replace a word and search for a word
  - [Question2.py](<Chapter%20-%2007/Practice/Question2.py>) — Find the line number where a word first occurs
  - [Question3.py](<Chapter%20-%2007/Practice/Question3.py>) — Count the even numbers in a comma-separated file
  - [Practice.py](<Chapter%20-%2007/Practice/Practice.py>) — Empty scratch file
  - [practice1.txt](<Chapter%20-%2007/Practice/practice1.txt>) — Sample data for Questions 1 and 2
  - [practice2.txt](<Chapter%20-%2007/Practice/practice2.txt>) — Sample data for Question 3
- [bin.py](<Chapter%20-%2007/bin.py>) — Empty scratch file

### [Chapter - 08: OOP Basics](<Chapter%20-%2008>)

- [01_OOP.py](<Chapter%20-%2008/01_OOP.py>) — Procedural vs object-oriented programming, classes and objects
- [02_constructor.py](<Chapter%20-%2008/02_constructor.py>) — Constructor (`__init__`) and `self`
- [03_class_&_instance_attributes.py](<Chapter%20-%2008/03_class_%26_instance_attributes.py>) — Class vs instance attributes and attribute priority
- [04_methods.py](<Chapter%20-%2008/04_methods.py>) — Instance methods
- [05_Practice_1.py](<Chapter%20-%2008/05_Practice_1.py>) — Practice question: `Student` class that prints the average of three marks
- [06_static_methods.py](<Chapter%20-%2008/06_static_methods.py>) — Static methods and decorators
- [07_abstraction.py](<Chapter%20-%2008/07_abstraction.py>) — Abstraction
- [08_encapsulation.py](<Chapter%20-%2008/08_encapsulation.py>) — Encapsulation and private attributes
- [09_Practice_2.py](<Chapter%20-%2008/09_Practice_2.py>) — Practice question: `Account` class with debit, credit and balance
- [bin.py](<Chapter%20-%2008/bin.py>) — Empty scratch file

### [Chapter - 09: OOP - Inheritance & Polymorphism](<Chapter%20-%2009>)

- [01_del_key.py](<Chapter%20-%2009/01_del_key.py>) — `del` keyword for attributes and objects
- [02_private.py](<Chapter%20-%2009/02_private.py>) — Public and private attributes, private methods
- [03_inheritance.py](<Chapter%20-%2009/03_inheritance.py>) — Inheritance basics and types
- [04_multi_level_inheritance.py](<Chapter%20-%2009/04_multi_level_inheritance.py>) — Multi-level inheritance
- [05_multiple_Inheritance.py](<Chapter%20-%2009/05_multiple_Inheritance.py>) — Multiple inheritance
- [06_super_method.py](<Chapter%20-%2009/06_super_method.py>) — `super()` for calling parent constructors and methods
- [07_class_method.py](<Chapter%20-%2009/07_class_method.py>) — Class methods (`@classmethod`, `cls`) compared with instance and static methods
- [08_property.py](<Chapter%20-%2009/08_property.py>) — `@property` decorator
- [09_polymorhpism.py](<Chapter%20-%2009/09_polymorhpism.py>) — Polymorphism and operator overloading
- [10_polymorhpism_2.py](<Chapter%20-%2009/10_polymorhpism_2.py>) — Implementing operator overloading with dunder methods (`__add__`, `__sub__`)
- [11_Practice.py](<Chapter%20-%2009/11_Practice.py>) — Practice questions: `Circle`, `Employee` and `Order` classes
- [bin.py](<Chapter%20-%2009/bin.py>) — Empty scratch file

### [Chapter - 10: Modern Python & Error Handling](<Chapter%20-%2010>)

- [01_walrus_operator.py](<Chapter%20-%2010/01_walrus_operator.py>) — Walrus operator (`:=`)
- [02_types.py](<Chapter%20-%2010/02_types.py>) — Type hints for variables, parameters and return values
- [03_match_case.py](<Chapter%20-%2010/03_match_case.py>) — `match`-`case` with constants, OR patterns, `if` guards and sequences
- [04_dict_merge_update.py](<Chapter%20-%2010/04_dict_merge_update.py>) — Dictionary merge (`|`) and update (`|=`) operators
- [05_exception_handling.py](<Chapter%20-%2010/05_exception_handling.py>) — `try` / `except` exception handling
- [06_raising_exception.py](<Chapter%20-%2010/06_raising_exception.py>) — Raising exceptions with `raise`
- [07_try_except_else.py](<Chapter%20-%2010/07_try_except_else.py>) — `try` / `except` / `else`
- [08_try_finally.py](<Chapter%20-%2010/08_try_finally.py>) — `try` / `finally`
- [09_if_name_main/](<Chapter%20-%2010/09_if_name_main>) — `if __name__ == "__main__"` and importing a module
  - [main.py](<Chapter%20-%2010/09_if_name_main/main.py>) — Imports from `module.py` and uses the `__name__` check
  - [module.py](<Chapter%20-%2010/09_if_name_main/module.py>) — Module that is imported by `main.py`
  - [pycahce.txt](<Chapter%20-%2010/09_if_name_main/pycahce.txt>) — Short note on the `__pycache__` folder
- [10_global.py](<Chapter%20-%2010/10_global.py>) — `global` keyword
- [11_enumerate.py](<Chapter%20-%2010/11_enumerate.py>) — `enumerate()`
- [12_list_comprehensions.py](<Chapter%20-%2010/12_list_comprehensions.py>) — List comprehensions: expression, filtering and conditions
- [Practice/](<Chapter%20-%2010/Practice>) — Practice questions on exceptions, `enumerate()` and list comprehensions
  - [Practice.py](<Chapter%20-%2010/Practice/Practice.py>) — Solutions to the practice questions
  - [2.txt](<Chapter%20-%2010/Practice/2.txt>) — Sample file read by the practice program
  - [Tablex.txt](<Chapter%20-%2010/Practice/Tablex.txt>) — Output file written by the practice program (multiplication table)
- [bin.py](<Chapter%20-%2010/bin.py>) — Empty scratch file

### [Chapter - 11: Misc / Advanced Topics](<Chapter%20-%2011>)

- [01_venv.py](<Chapter%20-%2011/01_venv.py>) — Virtual environments (file is currently empty)
- [02_lambda_func.py](<Chapter%20-%2011/02_lambda_func.py>) — Lambda (anonymous) functions
- [03_joint_method.py](<Chapter%20-%2011/03_joint_method.py>) — `join()` method for strings
- [04_format.py](<Chapter%20-%2011/04_format.py>) — `.format()` method
- [05_map_filter_reduce.py](<Chapter%20-%2011/05_map_filter_reduce.py>) — `map()`, `filter()`, `reduce()`
- [Practice/](<Chapter%20-%2011/Practice>) — Practice questions
  - [Practice.py](<Chapter%20-%2011/Practice/Practice.py>) — `.format()`, `join()`, `filter()` and `reduce()` exercises (the virtual environment, `pip freeze` and Flask questions are listed but not coded)
- [bin.py](<Chapter%20-%2011/bin.py>) — Empty scratch file

### [Chapter - 12: Iterators & Iterables](<Chapter%20-%2012>)

- [01_iteration_iterable_iterator.py](<Chapter%20-%2012/01_iteration_iterable_iterator.py>) — Definite vs indefinite iteration, iterator vs iterable, list vs `range()` memory use
- [02_iterator_protocol.py](<Chapter%20-%2012/02_iterator_protocol.py>) — Iterator protocol (`__iter__()`, `__next__()`), checking whether an object is iterable or an iterator
- [03_for_loop_and_custom_iterators.py](<Chapter%20-%2012/03_for_loop_and_custom_iterators.py>) — How the `for` loop works internally, building your own `for` loop and `range()`, custom iterators, lazy evaluation
- [04_practice_questions.py](<Chapter%20-%2012/04_practice_questions.py>) — Practice questions with solutions: `CountDown`, `EvenNumbers`, `PowerOfTwo`, `Multiples`, `Fibonacci`, an iterable `Reverse` class
- [05_beyond_the_basics.py](<Chapter%20-%2012/05_beyond_the_basics.py>) — `iter(callable, sentinel)`, the `__getitem__` fallback, built-in iterators, `itertools.islice`, preview of generators

### [13: Course Notes](<Course_Notes>)

#### [04_modules_and_random — Modules & the `random` module](<Course_Notes/04_modules_and_random>)

- [01_modules_and_imports.py](<Course_Notes/04_modules_and_random/01_modules_and_imports.py>) — What modules are, creating your own, `import` and `from … import`
- [02_random_module.py](<Course_Notes/04_modules_and_random/02_random_module.py>) — `random` module (`randint()`, `random()`, `uniform()`) and importing a custom module
- [my_module.py](<Course_Notes/04_modules_and_random/my_module.py>) — Small custom module used by the import examples

#### [12_scope — Scope](<Course_Notes/12_scope>)

- [01_scope_and_local_scope.py](<Course_Notes/12_scope/01_scope_and_local_scope.py>) — Namespaces, scope and local scope
- [02_global_scope.py](<Course_Notes/12_scope/02_global_scope.py>) — Global scope, and local vs global variables with the same name
- [03_enclosing_scope.py](<Course_Notes/12_scope/03_enclosing_scope.py>) — Enclosing scope (nested functions)
- [04_block_scope.py](<Course_Notes/12_scope/04_block_scope.py>) — Why Python has no block scope for `if`, `for` and `while`
- [05_modifying_global_variables.py](<Course_Notes/12_scope/05_modifying_global_variables.py>) — Modifying globals with `global`, and returning a value instead
- [06_python_constants.py](<Course_Notes/12_scope/06_python_constants.py>) — Global constants and the ALL_CAPS naming convention
- [07_practice_prime_checker.py](<Course_Notes/12_scope/07_practice_prime_checker.py>) — Practice: `is_prime()` — my approach and the course solution

#### [13_debugging — Debugging](<Course_Notes/13_debugging>)

- [01_debugging_basics.py](<Course_Notes/13_debugging/01_debugging_basics.py>) — What debugging is and how to identify bugs
- [02_reproduce_the_bug.py](<Course_Notes/13_debugging/02_reproduce_the_bug.py>) — Reproducing a bug reliably
- [03_play_computer.py](<Course_Notes/13_debugging/03_play_computer.py>) — Playing computer: tracing code line by line
- [04_catching_exceptions.py](<Course_Notes/13_debugging/04_catching_exceptions.py>) — Fixing editor-flagged errors and catching exceptions with `try` / `except`
- [05_debugging_with_print.py](<Course_Notes/13_debugging/05_debugging_with_print.py>) — Debugging with `print()`
- [06_using_a_debugger.py](<Course_Notes/13_debugging/06_using_a_debugger.py>) — Using an IDE debugger: breakpoints and stepping through code
- [maths.py](<Course_Notes/13_debugging/maths.py>) — Small helper module imported by `06_using_a_debugger.py`

### [14: Fundamentals (Mini Projects)](<Fundamentals>)

#### [01_band_name_generator — Band Name Generator](<Fundamentals/01_band_name_generator>)

- [main.py](<Fundamentals/01_band_name_generator/main.py>) — Combines the city you grew up in and a pet's name into a band name

#### [02_tip_calculator — Tip Calculator](<Fundamentals/02_tip_calculator>)

- [main.py](<Fundamentals/02_tip_calculator/main.py>) — Splits a bill between people with a tip, formatted to 2 decimal places

#### [03_conditionals — Conditionals](<Fundamentals/03_conditionals>)

- [pizza_delivery.py](<Fundamentals/03_conditionals/pizza_delivery.py>) — Pizza bill based on size, pepperoni and extra cheese
- [rollercoaster_ticket.py](<Fundamentals/03_conditionals/rollercoaster_ticket.py>) — Ticket price from height and age, with an optional photo (built from the flowchart)
- [treasure_island.py](<Fundamentals/03_conditionals/treasure_island.py>) — Text adventure with branching choices
- [assets/rollercoaster_flowchart.png](<Fundamentals/03_conditionals/assets/rollercoaster_flowchart.png>) — Flowchart the rollercoaster program is based on

#### [04_rock_paper_scissors — Rock Paper Scissors](<Fundamentals/04_rock_paper_scissors>)

- [main.py](<Fundamentals/04_rock_paper_scissors/main.py>) — My version of the game
- [course_solution.py](<Fundamentals/04_rock_paper_scissors/course_solution.py>) — Course solution, kept for comparison

#### [05_password_generator — Password Generator](<Fundamentals/05_password_generator>)

- [main.py](<Fundamentals/05_password_generator/main.py>) — My version: random password from letters, numbers and symbols
- [course_solution.py](<Fundamentals/05_password_generator/course_solution.py>) — Course solution, kept for comparison

#### [07_hangman — Hangman](<Fundamentals/07_hangman>)

- [main.py](<Fundamentals/07_hangman/main.py>) — My version of the word-guessing game
- [course_solution.py](<Fundamentals/07_hangman/course_solution.py>) — Course solution, kept for comparison
- [hangman_art.py](<Fundamentals/07_hangman/hangman_art.py>) — ASCII art for the hangman stages and logo
- [hangman_words.py](<Fundamentals/07_hangman/hangman_words.py>) — Word list the game picks from
- [assets/hangman_flowchart.png](<Fundamentals/07_hangman/assets/hangman_flowchart.png>) — Flowchart of the game logic

#### [08_caesar_cipher — Caesar Cipher](<Fundamentals/08_caesar_cipher>)

- [main.py](<Fundamentals/08_caesar_cipher/main.py>) — My attempts at encoding and decoding messages with a shift
- [course_solution.py](<Fundamentals/08_caesar_cipher/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/08_caesar_cipher/art.py>) — Logo art

#### [09_secret_auction — Secret Auction](<Fundamentals/09_secret_auction>)

- [main.py](<Fundamentals/09_secret_auction/main.py>) — Collects bids in a dictionary and finds the highest bidder
- [course_solution.py](<Fundamentals/09_secret_auction/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/09_secret_auction/art.py>) — Logo art

#### [10_calculator — Calculator](<Fundamentals/10_calculator>)

- [main.py](<Fundamentals/10_calculator/main.py>) — Calculator built from functions and an operations dictionary
- [course_solution.py](<Fundamentals/10_calculator/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/10_calculator/art.py>) — Logo art

#### [11_blackjack — Blackjack](<Fundamentals/11_blackjack>)

- [main.py](<Fundamentals/11_blackjack/main.py>) — My version of the card game
- [course_solution.py](<Fundamentals/11_blackjack/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/11_blackjack/art.py>) — Logo art

#### [12_number_guessing_game — Number Guessing Game](<Fundamentals/12_number_guessing_game>)

- [main.py](<Fundamentals/12_number_guessing_game/main.py>) — Guess the number within a limited number of attempts
- [course_solution.py](<Fundamentals/12_number_guessing_game/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/12_number_guessing_game/art.py>) — Logo art

#### [14_higher_lower — Higher Lower](<Fundamentals/14_higher_lower>)

- [main.py](<Fundamentals/14_higher_lower/main.py>) — Compare two randomly chosen items and guess which is higher
- [course_solution.py](<Fundamentals/14_higher_lower/course_solution.py>) — Course solution, kept for comparison
- [art.py](<Fundamentals/14_higher_lower/art.py>) — Logo and versus art
- [game_data.py](<Fundamentals/14_higher_lower/game_data.py>) — Data set the game draws from

---

## How This Repository Is Organized

- **Chapters** — each `Chapter - XX` folder groups files by the order topics were learned. Chapters 01–12 follow the learning sequence from basics to iterators.
- **Numbering** — files are numbered (`01_`, `02_`, …) to reflect the sequence within a chapter. Some numbers are skipped (for example, `Chapter - 01` goes from `06_` to `08_`).
- **Practice files** — files named `Practice` / `*Practice*.py` hold practice questions and solutions for that chapter's topics. Chapters 07, 10 and 11 keep their practice work in a `Practice/` subfolder.
- **Sample data files** — small `.txt` files used by the file-handling exercises live in `Chapter - 07` (named after the lesson they belong to, e.g. `2_demo1.txt`) and in `Chapter - 10/Practice`.
- **Images** — flowcharts are stored next to the code they explain: `Chapter - 02` for the conditional-statement diagrams, and `assets/` folders inside `Fundamentals` projects.
- **Scratch files** — `Chapter - 01` to `Chapter - 11` each have an empty `bin.py` that was used as a scratch file.
- **Course Notes** — topic folders (`04_modules_and_random`, `12_scope`, `13_debugging`) with notes on modules, scope and debugging. Their numbers are not contiguous.
- **Fundamentals** — one folder per mini project (`01_` to `14_`, with some numbers absent). Most projects have `main.py` (my version) and `course_solution.py` (the course solution, for comparison), plus helper files such as `art.py`; `03_conditionals` holds three separate programs instead.

## Repository Status

This is an ongoing Python learning repository — new chapters, topics and practice programs will be added as more Python concepts are covered.

---
