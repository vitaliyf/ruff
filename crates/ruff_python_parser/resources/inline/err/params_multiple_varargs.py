def foo(a, *, *args, b): ...
# def foo(a, *, b, c, *args): ...
def foo(a, *args1, *args2, b): ...
def foo(a, *args1, b, c, *args2): ...