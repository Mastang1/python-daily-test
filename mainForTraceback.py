import traceback

try:
    1 / 0  # 这里故意产生一个除以0的异常
except Exception as e:
    error_msg = ''.join(traceback.format_exception( e))
    print('*'*80, '\n\n')
    print(error_msg)
    # traceback.print_exc()
    # traceback.print_stack() 
