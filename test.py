from throws import raises


if (int, "hi") |raises| ValueError:
    print "casting 'hi' to int threw a valueerror"

if (int, "hi") |raises| Exception:
    print "casting 'hi' to int threw a subclass or instance of Exception"

def add(one, two):
    return one+two

if (add, "hi", 2) |raises| TypeError:
    print " adding 'hi' to 2 threw threw a typeerror"

if (int, 5) |raises| Exception:
    print "casting '5' to int threw an instance or subclass of Exception"
else:
    print "casting '5' to int threw no exceptions"

if raises(int, "hi") == ValueError:
    print "casting 'hi' to int threw a valueerror"

def test(text):
    raise Exception(text)

if raises(test, "hi") == Exception:
    print "running test threw an instance of Exception"

if raises(int, "hi") <= Exception:
    print "casting 'hi' to int threw a subclass or instance of Exception"

if not raises(int, '5') == Exception:
    print "casting '5' to int threw no exceptions"

if not raises(int, '50'):
    print "casting '50' to int threw no exceptions"

w = int("abc") if not (int, "abc") |raises| ValueError else -1
x = int("100") if not (int, "100") |raises| Exception else -1
y = int("50") if not raises(int, "50") < Exception else -1
z = int("99") if not raises(int, "99") else -1
print w, x, y, z

print type(raises(int, "abc")), raises(int, "abc")
print type(raises(int, "100")), raises(int, "100")


raise raises(int, "hi")


# Ideally, it would work like this:

# x = "hi"
# if int(x) raises TypeError:
#     print "incorrect type"
# else:
#     x = int(x)

# which lets you do things like this:
# x = int(x) if not int(x) raises TypeError else -1
