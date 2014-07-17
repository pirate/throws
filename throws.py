# Nick Sweeting 2014
# hackiest thing ever
class NoError(Exception):
    def __repr__(self):
        return "NoError"
    def __eq__(self, other):
        if not other or issubclass(other, NoError):
            return True
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        if issubclass(other, NoError):
            return True
        return False
    def __lt__(self, other):
        if issubclass(other, NoError):
            return True
        return False
    def __le__(self, other):
        if issubclass(other, NoError):
            return True
        return self.__eq__(other)
    def __ge__(self, other):
        if issubclass(other, NoError):
            return True
        return self.__eq__(other)
    def __len__(self):
        return False

def throws(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return NoError("NoError")

    except Exception as e:
        exception_type = type(e)
        class excp(exception_type):
            def __eq__(self, other):
                return exception_type == other
            def __ne__(self, other):
                return not (exception_type == other)
            def __gt__(self, other):
                return issubclass(exception_type, other) and not exception_type == other
            def __lt__(self, other):
                return issubclass(exception_type, other) and not exception_type == other
            def __le__(self, other):
                return issubclass(exception_type, other) or exception_type == other
            def __ge__(self, other):
                return issubclass(exception_type, other) or exception_type == other

        excp.__name__ = exception_type.__name__
        exception = excp()
        exception.message = e.message
        exception.args = e.args
        
        return exception

# credits to ferdinand Jamitzky for this Infix operator hack
class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, func, *args, **kwargs):
        return throws(func, *args, **kwargs)

raises=Infix(lambda x,y: throws(x[0], *x[1:]) is not None and throws(x[0], *x[1:]) <= y)
