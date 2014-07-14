# Nick Sweeting 2014

def throws(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return None
    except Exception as e:
        exception_type = type(e)

        class excp(exception_type):
            def __eq__(self, other):
                return type(self) == other or issubclass(type(self), other)
            def __ne__(self, other):
                return not (type(self) == other or issubclass(type(self), other))
            def __gt__(self, other):
                return type(self) == other or issubclass(type(self), other)
            def __lt__(self, other):
                return type(self) == other or issubclass(type(self), other)

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

raises=Infix(lambda x,y: throws(x[0], *x[1:]) == y)
