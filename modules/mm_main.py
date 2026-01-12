from module_mng import module_manager

# 加载位于不同路径的工具模块
tool_a = module_manager.load_tool_module(
    "image_processing", 
    path="d:/plugins/tools/image"
)
tool_b = module_manager.load_tool_module(
    "data_analysis", 
    path="d:/plugins/tools/analysis"
)

# 加载应用模块
app_module = module_manager.load_tool_module(
    "report_generator", 
    path="d:/plugins/apps/report"
)
