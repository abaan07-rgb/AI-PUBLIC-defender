import streamlit as st

st.set_page_config(page_title="AI Public Defender", page_icon="⚖️")

st.title("⚖️ AI Public Defender")
st.markdown("*Legal information for individuals without lawyers*")

st.info("Emergency? Call 112 immediately")

user_input = st.text_area("Describe your problem:", height=100)

if st.button("Get Legal Help"):
    if "husband" in user_input.lower() or "hit" in user_input.lower():
        st.success("🔴 Domestic Violence detected")
        st.markdown("""
        **Call now:** 181 (Women Helpline)
        
        **What to do:**
        - Go to nearest police station
        - Get medical help
        - Save evidence (photos, messages)
        """)
    elif "boss" in user_input.lower() or "office" in user_input.lower():
        st.success("🟡 Workplace Harassment detected")
        st.markdown("""
        **Call now:** 7827170170 (NCW)
        
        **What to do:**
        - Report to HR immediately
        - Save emails and messages
        """)
    else:
        st.warning("Call 112 for emergency help")