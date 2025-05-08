from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel

class FunctionMonitor(QObject):
    log_signal = pyqtSignal(str)
    
    def monitor(self, func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            info = f"{func.__name__}({', '.join(map(repr, args))}) -> {result!r}"
            self.log_signal.emit(info)
            return result
        return wrapped

if __name__ == '__main__':
    app = QApplication([])
    debug_label = QLabel()
    debug_label.show()
    
    monitor = FunctionMonitor()
    monitor.log_signal.connect(debug_label.setText)
    
    @monitor.monitor
    def sub_function(x, y):
        return x * y
    
    result = sub_function(2, 3)
    print(f"Result: {result}")
    
    app.exec_()