def operators_if(oper, x, y):
    if oper == "add":
        return x + y
    elif oper == "sub":
        return x - y
    elif oper == "mul":
        return x * y
    elif oper == "div":
        return x / y
        return None
    
def operators_dict(oper, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(oper, lambda: None)()

print(operators_dict("add", 2, 5))





    
