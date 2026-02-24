import streamlit as st
import time
import pandas as pd
import numpy as np

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="Python 极简前端 Demo",
    layout="wide",  # 宽屏模式
    initial_sidebar_state="expanded"
)

# --- 2. 侧边栏 (Sidebar) - 经典配置区 ---
with st.sidebar:
    st.header("⚙️ 设置面板")
    st.write("这是一个模拟的参数配置区")
    
    # 交互组件：输入框
    user_name = st.text_input("用户名", value="User_001")
    
    # 交互组件：下拉菜单
    mode = st.selectbox("选择模式", ["标准模式", "调试模式", "安全模式"])
    
    # 交互组件：滑动条
    threshold = st.slider("阈值设定", min_value=0, max_value=100, value=50)
    
    st.info(f"当前状态: {mode}")

# --- 3. 主界面 (Main Area) ---
st.title("🖥️ 数据控制台 Demo")
st.markdown("---")  # 分割线

# 使用列布局 (Columns) 来排版
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 任务操作")
    st.write(f"你好，**{user_name}**！准备执行任务吗？")
    
    # 交互组件：大按钮
    if st.button("🚀 开始执行任务", type="primary"):
        # 模拟后端处理过程
        with st.status("正在连接核心系统...", expanded=True) as status:
            st.write("正在初始化参数...")
            time.sleep(0.5)
            st.write(f"应用阈值设置: {threshold}")
            time.sleep(0.5)
            st.write("正在生成结果...")
            time.sleep(0.5)
            status.update(label="任务完成！", state="complete", expanded=False)
        
        st.success(f"执行成功！模式：{mode}")
        
        # 使用 Session State 保存状态（防止刷新丢失）
        st.session_state['data_generated'] = True
    else:
        st.write("点击按钮以开始交互。")

with col2:
    st.subheader("📊 实时监控")
    # 根据交互结果动态显示内容
    if st.session_state.get('data_generated', False):
        # 模拟生成一些数据并画图
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['CPU', 'Memory', 'IO']
        )
        st.line_chart(chart_data)
        st.caption(f"监控数据快照 - 阈值 {threshold}")
    else:
        st.info("等待任务执行后显示数据...")

# --- 4. 底部日志区 ---
st.markdown("---")
with st.expander("查看详细日志 (点击展开)"):
    st.code(f"""
    [INFO] System initialized.
    [INFO] User: {user_name} connected.
    [INFO] Mode set to: {mode}
    [INFO] Waiting for command...
    """, language="bash")