from throws import throws

if (int, "hi") |throws| ValueError:
    print "infix style threw valueerror"
elif (int, "hi") |throws| TypeError:
    print "infix style threw typeerror"
elif (int, "hi") |throws| Exception:
    print "infix threw other exception"

if throws(int, "hi") == ValueError:
    print "func style threw valueerror"
elif throws(int, "hi") == TypeError:
    print "func style threw typeerror"
else:
    print "func style threw other exception"


print throws(int, "hi").__class__
raise throws(int, "hi")
