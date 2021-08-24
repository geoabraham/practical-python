# Cheatsheet

**Common operations:**

```python
x + y      # Add
x - y      # Subtract
x * y      # Multiply
x / y      # Divide (produces a float)
x // y     # Floor Divide (produces an integer)
x % y      # Modulo (remainder)
x ** y     # Power
x << n     # Bit shift left
x >> n     # Bit shift right
x & y      # Bit-wise AND
x | y      # Bit-wise OR
x ^ y      # Bit-wise XOR
~x         # Bit-wise NOT
abs(x)     # Absolute value
```

**String escape codes:**

```python
'\n'      # Line feed
'\r'      # Carriage return
'\t'      # Tab
'\''      # Literal single quote
'\"'      # Literal double quote
'\\'      # Literal backslash
```

**String methods:**

```python
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
```

**enumerate() function**
The `enumerate` function adds an extra counter value to iteration.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

The general form is `enumerate(sequence [, start = 0])`. `start` is optional.
A good example of using `enumerate()` is tracking line numbers while reading a file:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

In the end, `enumerate` is just a nice shortcut for:

```python
i = 0
for x in s:
    statements
    i += 1
```
