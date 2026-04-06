import streamlit as st

# ========== LEGAL KNOWLEDGE BASE (12 SCENARIOS) ==========
legal_knowledge = {
    "domestic_violence": {
        "keywords": ["husband", "wife", "hit", "beat", "slap", "abuse", "violence", "threaten", "torture", "dowry", "mother in law", "push", "kick", "injury"],
        "title": "🔴 Domestic Violence",
        "laws": ["Protection of Women from Domestic Violence Act, 2005", "IPC 498A"],
        "immediate_actions": ["📞 Call 181", "📞 Call 112", "🏥 Go to hospital", "👮 File police complaint"],
        "legal_options": ["File FIR", "Protection order", "Right to reside", "Compensation"],
        "documents": ["Medical reports", "Photos", "Messages", "Witness names"]
    },
    "workplace_harassment": {
        "keywords": ["boss", "manager", "colleague", "office", "work", "harass", "touch", "comment", "hr"],
        "title": "🟡 Workplace Harassment",
        "laws": ["POSH Act, 2013", "IPC 354A"],
        "immediate_actions": ["📝 Document incidents", "📞 Report to ICC", "📞 NCW: 7827170170"],
        "legal_options": ["ICC complaint", "Police FIR", "Transfer", "Compensation"],
        "documents": ["Emails", "WhatsApp", "Witness names", "Incident log"]
    },
    "tenant_dispute": {
        "keywords": ["landlord", "rent", "deposit", "evict", "lease", "agreement", "owner"],
        "title": "🟢 Tenant Rights",
        "laws": ["Rent Control Act", "Transfer of Property Act"],
        "immediate_actions": ["📝 Written notice", "📞 Rent Control Authority", "📸 Take photos"],
        "legal_options": ["Rent Controller complaint", "Legal notice", "Consumer court", "Civil suit"],
        "documents": ["Rent agreement", "Deposit receipt", "Bank statements", "Photos"]
    },
    "cyber_harassment": {
        "keywords": ["facebook", "instagram", "whatsapp", "photo", "leak", "morphed", "fake id", "online", "cyber"],
        "title": "🔵 Cyber Harassment",
        "laws": ["IT Act 2000", "IPC 354C", "BNS 2023"],
        "immediate_actions": ["📸 Screenshots", "🚫 Block", "📞 1930", "🌐 cybercrime.gov.in"],
        "legal_options": ["Cyber complaint", "Police FIR", "Court removal order", "Compensation"],
        "documents": ["Screenshots", "URLs", "Timestamps", "Device details"]
    },
    "divorce": {
        "keywords": ["divorce", "separate", "leave husband", "leave wife", "cruelty", "end marriage", "talaq"],
        "title": "🟣 Divorce & Separation",
        "laws": ["Hindu Marriage Act", "Special Marriage Act", "Muslim Personal Law"],
        "immediate_actions": ["📝 Gather marriage proof", "💰 Document assets", "👨‍👩‍👧 Decide on children"],
        "legal_options": ["Mutual divorce", "Contested divorce", "Maintenance", "Child custody"],
        "documents": ["Marriage certificate", "Income proof", "Child birth certificate", "Property papers"]
    },
    "child_custody": {
        "keywords": ["child", "kid", "son", "daughter", "custody", "visitation", "parenting", "guardian"],
        "title": "👶 Child Custody",
        "laws": ["Guardians and Wards Act", "Hindu Minority Act"],
        "immediate_actions": ["👶 Ensure safety", "📝 Document involvement", "🚫 No kidnapping"],
        "legal_options": ["Physical custody", "Joint custody", "Visitation rights", "Guardianship"],
        "documents": ["Birth certificate", "School records", "Medical records", "Financial proof"]
    },
    "dowry_harassment": {
        "keywords": ["dowry", "dahej", "demand", "in-laws", "sasural", "dowry death"],
        "title": "💰 Dowry Harassment",
        "laws": ["Dowry Prohibition Act", "IPC 304B", "IPC 498A"],
        "immediate_actions": ["📞 181", "📝 List dowry items", "📸 Photos", "🏃‍♀️ Leave unsafe place"],
        "legal_options": ["Dowry Act FIR", "IPC 498A", "Claim back items", "Protection order"],
        "documents": ["Dowry list", "Photos", "Witnesses", "Marriage invitation"]
    },
    "rape_sexual_assault": {
        "keywords": ["rape", "assault", "forced sex", "molest", "gang rape", "penetration", "pocso"],
        "title": "🔴 Rape & Sexual Assault",
        "laws": ["IPC 375/376", "POCSO Act", "BNS 2023"],
        "immediate_actions": ["🚨 112", "🏥 Hospital (don't wash)", "👮 FIR", "📞 181"],
        "legal_options": ["File FIR", "Free legal aid", "In-camera trial", "Compensation"],
        "documents": ["Medical report", "Clothes", "CCTV", "Witnesses"]
    },
    "police_negligence": {
        "keywords": ["police not filing", "police refusing", "no fir", "police lazy", "thana"],
        "title": "👮 Police Negligence",
        "laws": ["Section 154 CrPC", "Section 166A IPC"],
        "immediate_actions": ["📝 Get refusal in writing", "📞 112", "📧 SP email"],
        "legal_options": ["Magistrate complaint u/s 156(3)", "Writ petition", "Compensation"],
        "documents": ["Refusal letter", "Date/time", "Officer name", "Your complaint copy"]
    },
    "acid_attack": {
        "keywords": ["acid", "throw acid", "burn", "chemical", "face burn", "vitriol"],
        "title": "🧪 Acid Attack",
        "laws": ["IPC 326A (10 yrs - life)", "IPC 326B (attempt)"],
        "immediate_actions": ["🚨 112", "🏥 Hospital", "💧 Wash continuously", "📞 181"],
        "legal_options": ["FIR under 326A", "Compensation up to ₹15 lakhs", "Free treatment", "In-camera trial"],
        "documents": ["Medical report", "Clothes", "CCTV", "Acid bottle if available"]
    },
    "property_dispute": {
        "keywords": ["land", "plot", "property", "ownership", "encroachment", "boundary", "will", "inheritance"],
        "title": "🏠 Property Dispute",
        "laws": ["Transfer of Property Act", "Registration Act", "Specific Relief Act"],
        "immediate_actions": ["📑 Collect documents", "📸 Photos", "📝 Legal notice", "🚫 No forcible removal"],
        "legal_options": ["Civil suit for possession", "Injunction", "Police complaint", "Lok Adalat"],
        "documents": ["Sale deed", "Tax receipts", "Encumbrance certificate", "Will", "Legal heir certificate"]
    },
    "cheating_fraud": {
        "keywords": ["cheat", "fraud", "scam", "fake", "money taken", "investment fraud", "online fraud", "loan fraud"],
        "title": "💸 Cheating / Fraud",
        "laws": ["IPC 420", "IPC 406", "IT Act"],
        "immediate_actions": ["📞 1930", "🔒 Freeze bank account", "📸 Screenshots"],
        "legal_options": ["FIR under 420", "Consumer court", "RBI complaint", "Civil suit"],
        "documents": ["Payment receipts", "Bank statements", "Screenshots", "Contract"]
    }
}

helplines = {
    "Police": "112", "Women Helpline": "181", "Cyber Crime": "1930",
    "NCW": "7827170170", "Child Helpline": "1098", "Legal Aid": "15100"
}

def find_scenario(user_input):
    user_input = user_input.lower()
    for sid, data in legal_knowledge.items():
        for kw in data["keywords"]:
            if kw in user_input:
                return sid, data
    return None, None

# ========== STREAMLIT UI ==========
st.set_page_config(page_title="AI Public Defender", page_icon="⚖️")

st.title("⚖️ AI Public Defender")
st.markdown("*Free legal information for individuals without lawyers*")

st.markdown("🚨 **Emergency: 112** | Women: 181 | Cyber: 1930")

user_input = st.text_area("Describe your situation:", height=100)

if st.button("Get Legal Help"):
    if user_input:
        sid, data = find_scenario(user_input)
        if data:
            st.success(f"### {data['title']}")
            st.markdown("**Laws:** " + ", ".join(data["laws"]))
            st.markdown("**Immediate Actions:**")
            for a in data["immediate_actions"]:
                st.markdown(f"- {a}")
            with st.expander("Legal Options"):
                for o in data["legal_options"]:
                    st.markdown(f"- {o}")
            with st.expander("Documents to Collect"):
                for d in data["documents"]:
                    st.markdown(f"- {d}")
        else:
            st.warning("Not recognized. Call 15100 (Legal Aid) for help.")
    else:
        st.error("Please describe your problem.")