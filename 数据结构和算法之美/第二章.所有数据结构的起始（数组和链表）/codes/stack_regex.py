
regex = '3+2'
symbols_level = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,
    ')': 0,
}

def math1(regex):
    num_stack= []
    symbols_stack = []
    ready_str = ''
    for index, value in enumerate(regex):
        if index == len(regex) - 1:
            symbol = symbols_stack.pop()
            j = num_stack.pop()
            print(j+symbol+value)
            num_stack.append(result)
        if value.isdigit():
            ready_str += value
        else:
            if ready_str:
                num_stack.append(ready_str)
            if not symbols_stack:
                symbols_stack.append(value)
                continue
            if symbols_level[symbols_stack[-1]] < symbols_level[value]:
                symbols_stack.append(value)
            else:
                symbol = symbols_stack.pop()
                i = num_stack.pop()
                j = num_stack.pop()
                result = exec(j+symbol+i)
                print(result)
                num_stack.append(result)
    print(num_stack)

math1(regex)