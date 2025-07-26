import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="ToolGuard AI", layout="wide")

# Header
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a8a, #1e40af, #1d4ed8); padding: 20px; border-radius: 10px;">
        <h1 style="color: white; margin: 0; display: flex; align-items: center;">
            <span style="margin-right: 10px;">🔧</span> ToolGuard AI - Tool Wear Prediction Dashboard
        </h1>
        <span style="color: #d1fae5;">🟢 System Online | Admin</span>
    </div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 System Overview")
    st.metric("Active Tools", 32)
    st.metric("Average Accuracy", "87%")
    st.write("**Model Version:** v2.4.1")
    st.write("**Last Updated:** 2 hours ago")

    st.subheader("🛠️ Tool Wear Status")
    st.info("🟢 Optimal: 28 tools")
    st.warning("🟡 Warning: 3 tools")
    st.error("🔴 Critical: 1 tool")

    st.subheader("🔁 Upcoming Replacements")
    st.write("🔺 Drill Bit #M-214 — 8.3h remaining (High Priority)")
    st.write("⚠️ End Mill #E-587 — 14.7h remaining (Medium Priority)")
    st.write("✅ Router Bit #R-932 — 23.1h remaining (Normal)")

with col2:
    st.subheader("📈 Tool Wear Prediction Accuracy")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    accuracy = [78, 81, 83, 85, 86, 87]

    fig, ax = plt.subplots()
    ax.plot(months, accuracy, marker='o', linestyle='-', color='#3b82f6', label="Accuracy")
    ax.fill_between(months, accuracy, alpha=0.2, color='#3b82f6')
    ax.set_ylim(70, 100)
    ax.set_ylabel("Accuracy (%)")
    ax.legend()
    st.pyplot(fig)

    st.subheader("⚙️ Machine Efficiency Impact")
    categories = ['Q1 Before AI', 'Q1 After AI', 'Q2 Before AI', 'Q2 After AI']
    uptimes = [82, 91, 84, 94]

    fig2, ax2 = plt.subplots()
    bars = ax2.bar(categories, uptimes, color=['#4dd0e1', '#00acc1', '#42a5f5', '#1e88e5'])
    ax2.set_ylim(70, 100)
    ax2.set_ylabel("Machine Uptime (%)")
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    st.pyplot(fig2)

    st.subheader("🔍 AI Model Configuration")
    st.markdown("""
    - **Architecture**: LSTM Neural Network  
    - **Training Data**: 6.5M Data Points  
    - **Maintenance Savings**: $84,500/year  
    - **Tracked Parameters**:  
        - Temperature  
        - Vibration  
        - Cutting Force  
        - Operation Hours  
        - Material Hardness  
    """)
