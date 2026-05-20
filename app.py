import streamlit as st
import random

# 台词列表
words = [
    "hello, world",
    "你好，胖友",
    "今天也要加油呀",
]

# 页面标题
st.title("🎤 随机说话器")

# 默认显示内容
if "talk" not in st.session_state:
    st.session_state.talk = "点击按钮开始说话"

# 按钮
if st.button("点击说话"):

    # 随机选一句
    st.session_state.talk = random.choice(words)

# 显示文字
st.write(st.session_state.talk)
