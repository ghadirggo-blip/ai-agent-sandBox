import sys
from pathlib import Path

# Add the parent directory to the Python path FIRST
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from core.main import run_agent_loop  # استدعي دالة الوكيل الأساسية لديك

st.title("🤖 Ghadir AI Agent Workspace")

# حفظ رسائل المحادثة في ذاكرة الجلسة الخاصة بالمتصفح
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات القديمة على الشاشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# صندوق إدخال الرسائل أسفل الشاشة مثل ChatGPT
if prompt := st.chat_input("Ask for anything Sir.."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # تشغيل الوكيل وإحضار الجواب
    with st.chat_message("assistant"):
        with st.spinner("Thinking.. ⏳"):
            response = run_agent_loop(prompt)  # الدالة التي تشغل الـ loop لديك
            st.markdown(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})