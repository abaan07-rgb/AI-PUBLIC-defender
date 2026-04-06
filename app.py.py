import streamlit as st

st.set_page_config(page_title="AI Public Defender", page_icon="⚖️", layout="wide")

# ========== SEXY CUSTOM CSS ==========
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        background-attachment: fixed;
        animation: gradientShift 10s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glassmorphism card effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 100, 100, 0.5);
    }
    
    /* Neon title */
    .neon-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neonPulse 3s ease infinite, gradientFlow 4s ease infinite;
        margin-bottom: 0;
        text-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
    }
    
    @keyframes neonPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.95; }
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }
    
    /* Glowing emergency banner */
    .emergency-banner {
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        padding: 1rem;
        border-radius: 50px;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 30px rgba(255, 75, 43, 0.6);
        animation: glow 1.5s ease-in-out infinite alternate;
        letter-spacing: 1px;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 10px #ff416c; }
        to { box-shadow: 0 0 30px #ff4b2b; }
    }
    
    /* Input field styling */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        border: 2px solid transparent;
        font-size: 1rem;
        padding: 1rem;
        transition: all 0.3s ease;
        color: #1a1a2e;
        font-weight: 500;
    }
    
    .stTextArea textarea:focus {
        border: 2px solid #feca57;
        box-shadow: 0 0 20px rgba(254, 202, 87, 0.4);
        background: white;
    }
    
    /* Sexy gradient button */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% 200%;
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        width: 100%;
        border: none;
        animation: buttonGradient 3s ease infinite;
        letter-spacing: 1px;
    }
    
    @keyframes buttonGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stButton button:hover {
        transform: scale(1.03);
        box-shadow: 0 10px 30px rgba(114, 9, 183, 0.5);
        cursor: pointer;
    }
    
    /* Result card styling */
    .result-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 1.8rem;
        margin-top: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: slideUp 0.5s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Law badges */
    .law-badge {
        background: linear-gradient(135deg, #00b4db, #0083b0);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 30px;
        font-size: 0.85rem;
        display: inline-block;
        margin-right: 0.6rem;
        margin-bottom: 0.6rem;
        font-weight: 600;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #feca57, #ff9ff3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] * {
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Helpline boxes */
    .helpline-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        color: white;
        font-weight: 600;
    }
    
    /* Info/warning boxes */
    .stAlert {
        border-radius: 15px;
        backdrop-filter: blur(5px);
    }
    
    footer {
        text-align: center;
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.8rem;
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown('<div class="neon-title">⚖️ AI Public Defender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">✨ Intelligent legal guidance. Instant. Free. Empowering. ✨</div>', unsafe_allow_html=True)

# ========== EMERGENCY BANNER ==========
st.markdown("""
<div class="emergency-banner">
    🚨 IMMEDIATE HELP 🚨 | Police: 112 | Women: 181 | Cyber: 1930 | Legal Aid: 15100
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 📞 Emergency Helplines")
    st.markdown("---")
    
    helplines_list = [
        ("🚓 Police Emergency", "112"),
        ("👩 Women Helpline", "181"),
        ("💻 Cyber Crime", "1930"),
        ("⚖️ NCW", "7827170170"),
        ("👶 Child Helpline", "1098"),
        ("📚 Legal Aid", "15100")
    ]
    
    for name, num in helplines_list:
        st.markdown(f'<div class="helpline-item">📞 <strong>{name}</strong><br><span style="font-size: 1.2rem;">{num}</span></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## ⚖️ 12 Legal Scenarios")
    st.markdown("---")
    
    issues = [
        "🔴 Domestic Violence",
        "🟡 Workplace Harassment",
        "🟢 Tenant Disputes",
        "🔵 Cyber Harassment",
        "🟣 Divorce",
        "👶 Child Custody",
        "💰 Dowry Harassment",
        "🔴 Rape/Assault",
        "👮 Police Negligence",
        "🧪 Acid Attack",
        "🏠 Property Dispute",
        "💸 Cheating/Fraud"
    ]
    
    for issue in issues:
        st.markdown(f"✅ {issue}")
    
    st.markdown("---")
    st.markdown("### 📢 Disclaimer")
    st.info("⚡ **Informational purposes only.** For specific legal advice, consult a lawyer. In emergency, call 112.")

# ========== MAIN INPUT ==========
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Tell us what happened")
    st.markdown("*Be as specific as possible for better guidance*")
    user_input = st.text_area("", height=120, placeholder="🔍 Example: My husband has been physically abusing me for 2 years. He demands dowry and threatens to kill me. I have photos of injuries.", label_visibility="collapsed")
    search_btn = st.button("✨ Get Legal Guidance ✨", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== KNOWLEDGE BASE ==========
legal_knowledge = {
    "domestic_violence": {
        "keywords": ["husband", "wife", "hit", "beat", "slap", "abuse", "violence", "threaten", "torture", "dowry", "mother in law", "push", "kick", "injury"],
        "title": "🔴 Domestic Violence",
        "laws": ["Protection of Women from Domestic Violence Act, 2005", "IPC 498A"],
        "immediate_actions": ["📞 Call 181 (Women Helpline) – 24x7", "📞 Call 112 for police", "🏥 Go to nearest hospital for medical exam", "👮 File complaint at police station (women's help desk)"],
        "legal_options": ["File FIR under IPC 498A", "Apply for Protection Order", "Right to reside in shared household", "Claim compensation"],
        "documents": ["Medical reports", "Photos of injuries", "Messages/call recordings", "Witness names"]
    },
    "workplace_harassment": {
        "keywords": ["boss", "manager", "colleague", "office", "work", "harass", "touch", "comment", "hr"],
        "title": "🟡 Workplace Harassment",
        "laws": ["POSH Act, 2013", "IPC 354A"],
        "immediate_actions": ["📝 Document every incident", "📞 Report to Internal Complaints Committee (ICC)", "📞 NCW helpline: 7827170170", "✉️ Send written complaint to HR"],
        "legal_options": ["ICC complaint (resolve in 90 days)", "Police FIR under IPC 354A", "Seek transfer of harasser", "Claim compensation"],
        "documents": ["Emails", "WhatsApp messages", "Witness names", "Incident log with dates"]
    },
    "tenant_dispute": {
        "keywords": ["landlord", "rent", "deposit", "evict", "lease", "agreement", "owner"],
        "title": "🟢 Tenant Rights",
        "laws": ["Rent Control Act", "Transfer of Property Act"],
        "immediate_actions": ["📝 Send written notice (registered post)", "📞 Call local Rent Control Authority", "📸 Take photos of property condition", "🚫 Do not stop paying rent without advice"],
        "legal_options": ["Complaint to Rent Controller", "Legal notice through lawyer", "Consumer court complaint", "Civil suit for deposit refund"],
        "documents": ["Rent agreement", "Deposit receipt", "Bank statements", "Photos of property"]
    },
    "cyber_harassment": {
        "keywords": ["facebook", "instagram", "whatsapp", "photo", "leak", "morphed", "fake id", "online", "cyber"],
        "title": "🔵 Cyber Harassment",
        "laws": ["IT Act 2000", "IPC 354C", "BNS 2023"],
        "immediate_actions": ["📸 Take screenshots (critical)", "🚫 Block the person", "📞 Call 1930 (Cyber Helpline)", "🌐 Report at cybercrime.gov.in"],
        "legal_options": ["File online cyber complaint", "Register FIR at cyber cell", "Court order for content removal", "Claim compensation"],
        "documents": ["Screenshots", "URLs", "Timestamps", "Device details"]
    },
    "divorce": {
        "keywords": ["divorce", "separate", "leave husband", "leave wife", "cruelty", "end marriage", "talaq"],
        "title": "🟣 Divorce & Separation",
        "laws": ["Hindu Marriage Act", "Special Marriage Act", "Muslim Personal Law"],
        "immediate_actions": ["📝 Gather marriage proof (certificate, photos)", "💰 Document all assets and incomes", "👨‍👩‍👧 Discuss child custody if applicable", "🏠 Decide who keeps the house"],
        "legal_options": ["Mutual consent divorce (6-18 months)", "Contested divorce (if partner disagrees)", "Claim maintenance/alimony", "Seek child custody"],
        "documents": ["Marriage certificate", "Income proof", "Child birth certificate", "Property documents"]
    },
    "child_custody": {
        "keywords": ["child", "kid", "son", "daughter", "custody", "visitation", "parenting", "guardian"],
        "title": "👶 Child Custody",
        "laws": ["Guardians and Wards Act", "Hindu Minority Act"],
        "immediate_actions": ["👶 Ensure child's safety first", "📝 Document your involvement (school, medical)", "🚫 Do not hide or kidnap the child", "👨‍⚖️ File for interim custody if urgent"],
        "legal_options": ["Physical custody", "Joint custody (shared parenting)", "Visitation rights for other parent", "Legal guardianship"],
        "documents": ["Child's birth certificate", "School records", "Medical records", "Proof of financial stability"]
    },
    "dowry_harassment": {
        "keywords": ["dowry", "dahej", "demand", "in-laws", "sasural", "dowry death"],
        "title": "💰 Dowry Harassment",
        "laws": ["Dowry Prohibition Act", "IPC 304B", "IPC 498A"],
        "immediate_actions": ["📞 Call 181 immediately", "📝 List all dowry items given", "📸 Take photos of jewelry/gifts", "🏃‍♀️ Leave the unsafe environment"],
        "legal_options": ["File FIR under Dowry Prohibition Act", "IPC 498A for cruelty", "Claim back dowry items", "Protection order"],
        "documents": ["List of dowry items", "Photos", "Witnesses (relatives/friends)", "Marriage invitation (shows gifts)"]
    },
    "rape_sexual_assault": {
        "keywords": ["rape", "assault", "forced sex", "molest", "gang rape", "penetration", "pocso"],
        "title": "🔴 Rape & Sexual Assault",
        "laws": ["IPC 375/376", "POCSO Act", "BNS 2023"],
        "immediate_actions": ["🚨 Call 112 immediately", "🏥 Go to hospital (do not wash or change clothes)", "👮 File FIR (woman officer will record)", "📞 Call 181 for support"],
        "legal_options": ["Free legal aid under Legal Services Authority", "In-camera trial (privacy protected)", "Claim compensation from State", "Medical termination if allowed"],
        "documents": ["Medical report", "Clothes worn during assault", "CCTV footage", "Witness names"]
    },
    "police_negligence": {
        "keywords": ["police not filing", "police refusing", "no fir", "police lazy", "thana"],
        "title": "👮 Police Negligence",
        "laws": ["Section 154 CrPC", "Section 166A IPC"],
        "immediate_actions": ["📝 Get refusal in writing (if possible)", "📞 Call 112 and complain about station", "📧 Send email to SP/DGP", "📞 State Human Rights Commission"],
        "legal_options": ["File complaint before Magistrate u/s 156(3) CrPC", "Write petition in High Court", "Claim compensation for negligence"],
        "documents": ["Written refusal", "Date/time of visit", "Officer's name", "Your complaint copy"]
    },
    "acid_attack": {
        "keywords": ["acid", "throw acid", "burn", "chemical", "face burn", "vitriol"],
        "title": "🧪 Acid Attack",
        "laws": ["IPC 326A (10 years to life)", "IPC 326B (attempted acid attack)"],
        "immediate_actions": ["🚨 Call 112", "🏥 Go to hospital immediately", "💧 Wash continuously with water", "📞 Call 181 for rehabilitation"],
        "legal_options": ["FIR under IPC 326A", "Compensation up to ₹15 lakhs", "Free medical treatment", "In-camera trial"],
        "documents": ["Medical report", "Clothes", "CCTV footage", "Acid bottle if available"]
    },
    "property_dispute": {
        "keywords": ["land", "plot", "property", "ownership", "encroachment", "boundary", "will", "inheritance"],
        "title": "🏠 Property Dispute",
        "laws": ["Transfer of Property Act", "Registration Act", "Specific Relief Act"],
        "immediate_actions": ["📑 Collect all property documents", "📸 Take photos of encroachment", "📝 Send legal notice", "🚫 Do not forcibly remove encroachment"],
        "legal_options": ["Civil suit for possession", "Injunction to stop construction", "Police complaint for criminal trespass", "Lok Adalat for settlement"],
        "documents": ["Sale deed", "Tax receipts", "Encumbrance certificate", "Will/legal heir certificate"]
    },
    "cheating_fraud": {
        "keywords": ["cheat", "fraud", "scam", "fake", "money taken", "investment fraud", "online fraud", "loan fraud"],
        "title": "💸 Cheating / Fraud",
        "laws": ["IPC 420", "IPC 406", "IT Act"],
        "immediate_actions": ["📞 Call 1930 (Cyber Fraud Helpline)", "🔒 Freeze bank account immediately", "📸 Save all transaction screenshots", "📞 Police cyber cell"],
        "legal_options": ["File FIR under Section 420", "Consumer court complaint", "RBI complaint for banking fraud", "Civil suit for recovery"],
        "documents": ["Payment receipts", "Bank statements", "Screenshots of communication", "Contract/agreement"]
    }
}

def find_scenario(user_input):
    user_input = user_input.lower()
    for sid, data in legal_knowledge.items():
        for kw in data["keywords"]:
            if kw in user_input:
                return sid, data
    return None, None

# ========== PROCESS INPUT ==========
if search_btn and user_input:
    with st.spinner("🔍 Analyzing your situation..."):
        sid, data = find_scenario(user_input)
    
    if data:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        st.markdown(f"## {data['title']}")
        
        # Laws
        st.markdown('<div class="section-header">📚 Laws That Protect You</div>', unsafe_allow_html=True)
        for law in data["laws"]:
            st.markdown(f'<span class="law-badge">{law}</span>', unsafe_allow_html=True)
        st.markdown("")
        
        # Immediate actions
        st.markdown('<div class="section-header">🚨 What You Can Do RIGHT NOW</div>', unsafe_allow_html=True)
        for action in data["immediate_actions"]:
            st.markdown(f"- {action}")
        
        # Legal options
        with st.expander("⚖️ Detailed Legal Options (Click to expand)"):
            for opt in data["legal_options"]:
                st.markdown(f"- {opt}")
        
        # Documents needed
        with st.expander("📄 Documents to Collect (Click to expand)"):
            for doc in data["documents"]:
                st.markdown(f"- {doc}")
        
        # Download guide
        guide_text = f"""AI PUBLIC DEFENDER - LEGAL GUIDE
{data['title']}

LAWS: {', '.join(data['laws'])}

IMMEDIATE ACTIONS:
{chr(10).join(data['immediate_actions'])}

LEGAL OPTIONS:
{chr(10).join(data['legal_options'])}

DOCUMENTS NEEDED:
{chr(10).join(data['documents'])}

HELPLINES:
Police: 112 | Women: 181 | Cyber: 1930 | Legal Aid: 15100

Disclaimer: This is for information only. Consult a lawyer for specific advice.
"""
        st.download_button("📥 Download Legal Guide", guide_text, file_name=f"legal_guide_{sid}.txt", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ **Couldn't match your situation.** Please rephrase or call helplines.")
        st.info("💡 **Tips:** Use words like 'hit', 'harass', 'deposit not returned', 'divorce', 'custody', 'fraud'.")
        st.markdown('<div class="glass-card" style="text-align:center;">📞 <strong>Legal Aid Helpline: 15100</strong> – Free legal advice from certified lawyers</div>', unsafe_allow_html=True)

elif search_btn and not user_input:
    st.error("✨ Please describe your situation first ✨")

# ========== FOOTER ==========
st.markdown("---")
st.markdown('<footer>⚖️ AI Public Defender – Empowering justice for all | Hackathon 2026 | <span style="color:#ff6b6b;">❤️</span> Made for social impact</footer>', unsafe_allow_html=True)