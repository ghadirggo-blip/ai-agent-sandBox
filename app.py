import streamlit as st
from main import run_agent_loop  # استدعي دالة الوكيل الأساسية لديك

st.title("🤖 My AI Agent Workspace")

# حفظ رسائل المحادثة في ذاكرة الجلسة الخاصة بالمتصفح
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات القديمة على الشاشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# صندوق إدخال الرسائل أسفل الشاشة مثل ChatGPT
if prompt := st.chat_input("اطلب من الوكيل أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # تشغيل الوكيل وإحضار الجواب
    with st.chat_message("assistant"):
        with st.spinner("الوكيل يفكر وينفذ الأدوات... ⏳"):
            response = run_agent_loop(prompt)  # الدالة التي تشغل الـ loop لديك
            st.markdown(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})