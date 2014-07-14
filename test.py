from throws import raises

if (int, "hi") |raises| ValueError:
    print "infix style threw valueerror"

elif (int, "hi") > raises > TypeError:
    print "infix style threw typeerror"

elif (int, "hi") |raises| Exception:
    print "infix threw other exception"

# "infix style threw valueerror"

if raises(int, "hi") > ValueError:
    print "func style threw valueerror"
elif raises(int, "hi") > TypeError:
    print "func style threw typeerror"
elif raises(int, "hi") > Exception:
    print "func style threw other exception"
elif not raises(int, "hi"):
    print "func style threw no exceptions"

# "func style threw valueerror"


x = int("abc") if not (int, "abc") |raises| ValueError else -1
y = int(100) if not (int, 100) |raises| Exception else -1
z = int(100) if not raises(int, 100) else -1
print x, y, z
# -1 100 50

print raises(int, "abc")
# invalid literal for int() with base 10: 'hi'
print raises(int, "abc").__class__
# <class 'throws.ValueError'>

print raises(int, 100)
# None
print raises(int, 100).__class__
# <type 'NoneType'>


raise raises(int, "hi")
# Traceback (most recent call last):
#   File "test.py", line 42, in <module>
#     raise raises(int, "hi")
# throws.ValueError: invalid literal for int() with base 10: 'hi'


# Ideally, it would work like this:

# x = "hi"
# if int(x) raises TypeError:
#     print "incorrect type"
# else:
#     x = int(x)

# which lets you do things like this:
# x = int(x) if not int(x) raises TypeError else -1
