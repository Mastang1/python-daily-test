def trace_dispatch(self, frame, event, arg):
    if self.quitting:
        return None
    
    # 只追踪最外层调用
    if frame.f_back is None or frame.f_back.f_back is None:
        if event == 'call':
            func_name = frame.f_code.co_name
            filename = self.canonic(frame.f_code.co_filename)
            lineno = frame.f_lineno
            
            print(f"[TOP LEVEL] 调用函数: {func_name}() "
                  f"在 {filename}:{lineno}")
            
            # 测试用例特殊处理
            if func_name.startswith('test'):
                args = ', '.join(f"{k}={v!r}" for k,v in frame.f_locals.items())
                print(f"[TEST CASE] {func_name}({args})")
                
        # 返回追踪函数
        return trace_dispatch
    
    # 非顶层调用直接返回None停止追踪
    return None

"""
线程特性：

每个线程有独立的跟踪设置，需要通过threading.settrace()为其他线程设置
跟踪调用是线程安全的，因为总是在当前线程的上下文中同步执行
性能影响：

由于是同步调用，会显著降低代码执行速度
复杂的跟踪逻辑可能导致性能下降数十倍
"""