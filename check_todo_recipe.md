# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user_
_So that I can find my tasks among all my notes_
_I want to check if a line from my notes_ _includes the string `#TODO`._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def check_todo(note):
    # parameters is a string: note

    # returns:
    # either True or False

    # no side effects

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given a string only including #TODO
It returns True
"""
check_todo("#TODO") => True

"""
Given a string only including #TODO and one word
It returns True
"""
check_todo("#TODO walk") => True

"""
Given an empty string
It returns False
"""
check_todo("") => False

"""
Given a string without #TODO
It returns False
"""
check_todo("go to the grocery store") => False

"""
Given a string with #todo (lowercase)
It returns False
"""
check_todo("#todo go to the grocery store") => False

"""
Given a string with TODO and no #
It returns False
"""
check_todo("TODO go to the grocery store") => False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
