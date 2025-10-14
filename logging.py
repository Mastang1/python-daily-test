import logging
import logging.handlers
import os

def setup_logging():
    """
    配置日志系统，同时输出到文件和控制台
    """
    # 创建logger实例
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置最低日志级别
    
    # 避免重复添加handler
    if logger.handlers:
        logger.handlers.clear()
    
    # 创建formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    
    # 1. 文件处理器 - 输出到文件
    # 确保logs目录存在
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 使用RotatingFileHandler，自动轮转日志文件
    file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(log_dir, 'app.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,           # 保留5个备份文件
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)  # 文件日志级别
    file_handler.setFormatter(formatter)
    
    # 2. 控制台处理器 - 输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 控制台日志级别
    console_handler.setFormatter(formatter)
    
    # 添加处理器到logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def main():
    """
    主函数，演示日志使用
    """
    # 设置日志
    logger = setup_logging()
    
    # 演示不同级别的日志
    logger.debug('这是一条调试信息')
    logger.info('这是一条普通信息')
    logger.warning('这是一条警告信息')
    logger.error('这是一条错误信息')
    logger.critical('这是一条严重错误信息')
    
    # 演示带变量的日志
    user_id = 12345
    operation = '数据查询'
    logger.info('用户 %d 执行了 %s 操作', user_id, operation)
    
    # 演示异常日志
    try:
        result = 10 / 0
    except Exception as e:
        logger.error('发生数学运算错误: %s', str(e), exc_info=True)

if __name__ == '__main__':
    main()
