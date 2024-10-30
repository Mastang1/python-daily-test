import sys, time


def trace_calls(frame, event, arg):
    if event == 'call':
        function_name = frame.f_code.co_name
        args = frame.f_locals
        print(f'Calling function: {function_name}, {args}')
    elif event == 'return':
        function_name = frame.f_code.co_name
        return_value = arg
        print(f'Returning from function: {function_name}, Return value: {return_value}')
    return trace_calls


def add(a, b):
    sys.settrace(trace_calls)
    for it in range(10):
        time.sleep(0.2)
    return a + b


def main():
    sys.settrace(trace_calls)
    result = add(3, 4)
    sys.settrace(None)  # 停止跟踪
    print(f"Result: {result}")


main()

