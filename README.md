throws/raises
=============

This is a mini python library that allows you to use if/else statements for doing conditional logic with exceptions.
Check out `tests.py` for a comprehensive overview of how to use the keyword `raises`, provided by importing `throws.py`.

Quickstart:
```bash
git clone https://github.com/pirate/throws.git
cd throws
python tests.py
```
or:
```bash
python
>>>from throws import raises, NoError
>>>a = int("abc") if not (int, "abc") |raises| ValueError else -1
>>>print(a)
```
-----------

My proposal is to incorporate this as a python keyword, allowing us to do powerful one-liners like this:

```python
a = int("10") if not raises ValueError else -1
```


Right now, this is your only option:

```python
try:
    a = int("hi")
except ValueError:
    a = 0
except Exception:
    a = 0
    print "some other error"
```

This is ok... but not ideal.
Maybe it's wistful thinking, maybe it's python blasphemy, but I've always wanted more powerful expressions for doing conditional logic on exceptions.  

This would be so much more concise!

```python
a = int("10") if not raises ValueError else -1
```

It may seem excessive to add a new keyword, but it's extremely valuable when you're dealing with hundreds of lines of nested exception logic for parsing potentially invalid data.
Of course, the more verbose form would still be available too:

Ideally we could run code inside of parens (to do variable assignments) and test for exceptions:

```python

if not (a = int("10")) raises Exception:
  print a
else:
  print "converting to int failed"
```

We cant do this in current python, but we can combine some cool hacks and get something pretty close.
The hack I use specifically is overloading the bitwise || <<<>> operators to hack together an infix keyword like this: `if a |raises| Exception:`.
Check out `tests.py` for a comprehensive overview of what this mini-library is capable of.
