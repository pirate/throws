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

# class throws(Infix):
#     def __init__(self, function):
#         Infix.__init__(self, function)

def throw(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        class excep(type(e)):
            def __getattribute__(self, name):
                if name == '__class__':
                    return type(e)
                else:
                    return super(excep, self).__getattribute__(name)

            def __eq__(self, other):
                return type(self) == other or issubclass(type(self), other)

        exception = excep(e)
        exception.message = e.message
        exception.args = e.args
        
        return exception

throws=Infix(lambda x,y: throw(x[0], *x[1:]) == y)


# if int("hi") throws ValueError:
#     print ""


# try:
#     x = int('hi')
# except:
#     x = "didnt work"

# x = int('hi') if not int("hi") raises Exception else "didn't work"
