import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page config
st.set_page_config(page_title="ToolGuard AI Dashboard", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🔧 ToolGuard AI")
    st.markdown("**Welcome, Admin**")
    st.markdown("📡 System Status: 🟢 Online")
    st.markdown("---")
    st.header("📂 Navigation")
    st.button("📊 Dashboard")
    st.button("📈 Reports")
    st.button("⚙️ Settings")
    st.markdown("---")
    st.caption("🕒 Last Sync: 2 hours ago")
    st.caption("🔄 Version: v2.4.1")

# Header
st.markdown("""
<div style="background: linear-gradient(135deg, #1e3a8a, #1e40af, #1d4ed8); padding: 20px; border-radius: 12px; margin-bottom: 20px;">
    <h1 style="color: white; margin: 0;">🔧 ToolGuard AI - Tool Wear Prediction Dashboard</h1>
    <p style="color: #d1fae5;">Monitor real-time wear levels, forecast replacements, and optimize tool performance.</p>
</div>
""", unsafe_allow_html=True)

# Overview Metrics
with st.container():
    st.subheader("📊 System Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Tools", 32)
    col2.metric("Average Accuracy", "87%")
    col3.metric("Predicted Failures", 4)

# Tool Wear Status
with st.container():
    st.subheader("🛠️ Tool Wear Status")
    st.success("🟢 Optimal: 28 tools")
    st.warning("🟡 Warning: 3 tools")
    st.error("🔴 Critical: 1 tool")

# Upcoming Replacements
with st.container():
    st.subheader("🔁 Upcoming Replacements")
    st.markdown("- 🔺 **Drill Bit #M-214** — 8.3h remaining (**High Priority**)")
    st.markdown("- ⚠️ **End Mill #E-587** — 14.7h remaining (**Medium Priority**)")
    st.markdown("- ✅ **Router Bit #R-932** — 23.1h remaining (**Normal**)")


# Charts Section
with st.container():
    st.subheader("📈 Tool Wear Prediction Accuracy")

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    accuracy = [78, 81, 83, 85, 86, 87]

    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots()
    ax.plot(months, accuracy, marker='o', linestyle='-', color='#3b82f6', label="Accuracy")
    ax.fill_between(months, accuracy, alpha=0.2, color='#3b82f6')
    ax.set_ylim(70, 100)
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Prediction Accuracy Over Time")
    ax.legend()
    st.pyplot(fig)

# Uptime Chart
with st.container():
    st.subheader("⚙️ Machine Efficiency Impact")

    categories = ['Q1 Before AI', 'Q1 After AI', 'Q2 Before AI', 'Q2 After AI']
    uptimes = [82, 91, 84, 94]

    fig2, ax2 = plt.subplots()
    bars = ax2.bar(categories, uptimes, color=['#4dd0e1', '#00acc1', '#42a5f5', '#1e88e5'])
    ax2.set_ylim(70, 100)
    ax2.set_ylabel("Machine Uptime (%)")
    ax2.set_title("AI Implementation Impact on Uptime")
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    st.pyplot(fig2)

# Model Details in Expander
with st.expander("🔍 AI Model Configuration"):
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

# Footer
st.markdown("""<hr style='border:1px solid #eee'/>""", unsafe_allow_html=True)
st.markdown("<center>© 2025 ToolGuard AI — Built by Krunit Mistry</center>", unsafe_allow_html=True)
