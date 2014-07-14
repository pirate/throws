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
        return throw(func, *args, **kwargs)

def throw(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        exception_type = type(e)

        class excp(exception_type):
            def __eq__(self, other):
                return type(self) == other or issubclass(type(self), other)

        excp.__name__ = exception_type.__name__
        exception = excp()
        exception.message = e.message
        exception.args = e.args
        
        return exception

throws=Infix(lambda x,y: throw(x[0], *x[1:]) == y)
