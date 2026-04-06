import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="AI Public Defender", page_icon="⚖️", layout="wide", initial_sidebar_state="expanded")

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    /* Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Background with subtle animation */
    .stApp {
        background: linear-gradient(135deg, #0B1120 0%, #19223B 50%, #1A2A4A 100%);
        background-attachment: fixed;
    }
    
    /* Floating particles */
    .particle {
        position: fixed;
        border-radius: 50%;
        background: rgba(100, 200, 255, 0.3);
        pointer-events: none;
        z-index: 0;
    }
    
    /* Main container */
    .main-container {
        position: relative;
        z-index: 1;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 1rem;
    }
    
    .hero h1 {
        font-size: 4.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 5s ease infinite;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    @keyframes gradientFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .hero p {
        color: #A0B3D9;
        font-size: 1.2rem;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Emergency banner with pulse */
    .emergency-banner {
        background: linear-gradient(135deg, #FF416C, #FF4B2B);
        border-radius: 20px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        animation: pulse 1.5s infinite;
        box-shadow: 0 10px 30px rgba(255, 65, 108, 0.3);
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.01); opacity: 0.95; }
    }
    
    .emergency-banner span {
        color: white;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.5px;
    }
    
    /* Glass card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 1.8rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-4px);
    }
    
    /* Input styling */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        border: 2px solid #4ECDC4;
        font-size: 1rem;
        padding: 1rem;
        transition: all 0.3s;
    }
    
    .stTextArea textarea:focus {
        border-color: #FF6B6B;
        box-shadow: 0 0 15px rgba(255, 107, 107, 0.3);
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 40px;
        padding: 0.7rem;
        transition: all 0.3s;
        border: none;
        width: 100%;
        letter-spacing: 1px;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Result card */
    .result-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(15px);
        border-radius: 28px;
        padding: 1.8rem;
        margin-top: 2rem;
        border: 1px solid rgba(255,255,255,0.15);
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
    
    /* Badge styling */
    .badge {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        padding: 0.3rem 1rem;
        border-radius: 50px;
        display: inline-block;
        margin: 0.3rem;
        color: white;
        font-weight: 500;
        font-size: 0.85rem;
    }
    
    .badge-blue {
        background: linear-gradient(135deg, #4ECDC4, #45B7D1);
    }
    
    .badge-purple {
        background: linear-gradient(135deg, #a8c0ff, #3f2b96);
    }
    
    /* Section headers */
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        background: linear-gradient(135deg, #FFD166, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(11, 17, 32, 0.95);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Stat cards */
    .stat-card {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s;
    }
    
    .stat-card:hover {
        background: rgba(255,255,255,0.1);
        transform: scale(1.02);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFD166, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6B7B8F;
        font-size: 0.85rem;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
if "history" not in st.session_state:
    st.session_state.history = []
if "case_id" not in st.session_state:
    st.session_state.case_id = random.randint(10000, 99999)

# ========== KNOWLEDGE BASE (ENHANCED) ==========
legal_knowledge = {
    "domestic_violence": {
        "keywords": ["husband", "wife", "hit", "beat", "slap", "abuse", "violence", "threaten", "torture", "dowry", "mother in law", "push", "kick", "injury", "blood", "fight", "angry"],
        "title": "🔴 Domestic Violence",
        "severity": "Critical",
        "response_time": "Immediate",
        "laws": ["Protection of Women from Domestic Violence Act, 2005", "IPC Section 498A", "Dowry Prohibition Act, 1961"],
        "immediate_actions": [
            "📞 Call 181 (Women Helpline) – 24x7, Confidential",
            "📞 Call 112 for immediate police assistance",
            "🏥 Go to nearest hospital for free medical examination",
            "👮 File complaint at police station (women's help desk available)",
            "🏠 You have legal right to live in shared household"
        ],
        "legal_options": [
            "File FIR under IPC 498A (cruelty by husband/relatives)",
            "Apply for Protection Order from Magistrate",
            "Seek Right to Reside in matrimonial home",
            "Claim monetary compensation for injuries",
            "File for divorce on grounds of cruelty"
        ],
        "documents": ["Medical reports", "Photos of injuries", "Call recordings", "WhatsApp messages", "Witness names", "Marriage certificate"],
        "helplines": ["181", "112", "7827170170"]
    },
    "workplace_harassment": {
        "keywords": ["boss", "manager", "colleague", "office", "work", "harass", "touch", "comment", "hr", "coworker", "supervisor", "staff"],
        "title": "🟡 Workplace Harassment",
        "severity": "High",
        "response_time": "24 hours",
        "laws": ["Sexual Harassment of Women at Workplace Act, 2013 (POSH)", "IPC Section 354A"],
        "immediate_actions": [
            "📝 Document every incident with date, time, location",
            "📞 Report to Internal Complaints Committee (ICC) – mandatory in all companies",
            "✉️ Send written complaint to HR (keep a copy)",
            "📞 Call NCW helpline: 7827170170",
            "🚫 Tell the harasser clearly to stop (in writing if possible)"
        ],
        "legal_options": [
            "ICC complaint – must resolve within 90 days",
            "Police FIR under IPC 354A",
            "Seek transfer of harasser or yourself",
            "Claim compensation from employer",
            "File civil suit for damages"
        ],
        "documents": ["Emails", "WhatsApp messages", "Witness names", "Incident log with dates", "CCTV footage request"],
        "helplines": ["7827170170", "112"]
    },
    "tenant_dispute": {
        "keywords": ["landlord", "rent", "deposit", "evict", "house", "apartment", "lease", "agreement", "owner", "tenancy", "security deposit"],
        "title": "🟢 Tenant Rights",
        "severity": "Medium",
        "response_time": "48 hours",
        "laws": ["Rent Control Act (state specific)", "Transfer of Property Act, 1882", "Consumer Protection Act"],
        "immediate_actions": [
            "📝 Send written notice to landlord via registered post",
            "📞 Call local Rent Control Authority",
            "📸 Take photos/videos of property condition",
            "💰 Do not stop paying rent without legal advice"
        ],
        "legal_options": [
            "File complaint with Rent Controller for illegal eviction",
            "Send legal notice through lawyer",
            "Consumer court complaint for unfair practice",
            "Civil suit for deposit refund"
        ],
        "documents": ["Rent agreement", "Deposit receipt", "Bank statements", "Photos of property", "Notice copies"],
        "helplines": ["15100"]
    },
    "cyber_harassment": {
        "keywords": ["facebook", "instagram", "whatsapp", "telegram", "photo", "video", "leak", "morphed", "fake id", "online", "social media", "troll", "cyber", "internet", "email"],
        "title": "🔵 Cyber Harassment",
        "severity": "High",
        "response_time": "Immediate",
        "laws": ["IT Act 2000 Sections 66E, 67", "IPC 354C, 509", "Bharatiya Nyaya Sanhita 2023"],
        "immediate_actions": [
            "📸 Take screenshots of EVERYTHING (critical evidence)",
            "🚫 Block the person immediately",
            "📞 Call cyber helpline: 1930",
            "🌐 Report on cybercrime.gov.in (anonymous option available)",
            "🔒 Change all passwords and enable 2FA"
        ],
        "legal_options": [
            "File complaint on cybercrime portal (online FIR)",
            "Register FIR at local cyber cell",
            "Get court order for content removal",
            "Claim compensation under IT Act",
            "Report to platform for account suspension"
        ],
        "documents": ["Screenshots", "URLs", "Profile links", "Timestamps", "Device details"],
        "helplines": ["1930", "112"]
    },
    "divorce": {
        "keywords": ["divorce", "separate", "leave husband", "leave wife", "cruelty", "no love", "end marriage", "talaq", "mutual", "contested"],
        "title": "🟣 Divorce & Separation",
        "severity": "High",
        "response_time": "1 week",
        "laws": ["Hindu Marriage Act, 1955", "Special Marriage Act, 1954", "Muslim Personal Law", "Indian Divorce Act, 1869"],
        "immediate_actions": [
            "📝 Gather all marriage proof (certificate, photos, invitations)",
            "💰 Document all assets, incomes, expenses",
            "👨‍👩‍👧 Discuss and decide about children",
            "🏠 Decide who will stay in the house"
        ],
        "legal_options": [
            "Mutual consent divorce (quickest, 6-18 months)",
            "Contested divorce (if partner doesn't agree)",
            "File for maintenance/alimony under Section 125 CrPC",
            "Seek child custody (physical or joint)",
            "Annulment if marriage was fraudulent"
        ],
        "documents": ["Marriage certificate", "Income proofs", "Child birth certificates", "Property documents", "Evidence of cruelty"],
        "helplines": ["15100"]
    },
    "child_custody": {
        "keywords": ["child", "kid", "son", "daughter", "custody", "visitation", "parenting", "guardian", "minor", "children"],
        "title": "👶 Child Custody",
        "severity": "High",
        "response_time": "48 hours",
        "laws": ["Guardians and Wards Act, 1890", "Hindu Minority and Guardianship Act, 1956", "Juvenile Justice Act"],
        "immediate_actions": [
            "👶 Ensure child's safety first",
            "📝 Document your involvement in child's life",
            "🚫 Do NOT hide or kidnap the child",
            "👨‍⚖️ File for interim custody if urgent"
        ],
        "legal_options": [
            "Physical custody (child lives with you)",
            "Joint custody (shared parenting time)",
            "Visitation rights for other parent",
            "Legal guardianship (decision-making power)",
            "Supervised visitation if safety concerns"
        ],
        "documents": ["Child's birth certificate", "School records", "Medical records", "Proof of financial stability"],
        "helplines": ["1098", "15100"]
    },
    "dowry_harassment": {
        "keywords": ["dowry", "dahej", "money", "gift", "car", "jewelry", "demand", "in-laws", "sasural", "dowry death"],
        "title": "💰 Dowry Harassment",
        "severity": "Critical",
        "response_time": "Immediate",
        "laws": ["Dowry Prohibition Act, 1961", "IPC 304B (dowry death)", "IPC 498A"],
        "immediate_actions": [
            "📞 Call 181 IMMEDIATELY",
            "📝 Make list of all dowry items given with approximate value",
            "📸 Take photos of jewelry/gifts",
            "🏃‍♀️ Leave the unsafe environment",
            "👮 File complaint before dowry demands escalate"
        ],
        "legal_options": [
            "File FIR under Dowry Prohibition Act",
            "Section 498A IPC for cruelty",
            "If death occurs, Section 304B (7 years to life)",
            "Claim back dowry items",
            "Protection order from court"
        ],
        "documents": ["List of dowry items", "Photos", "Witnesses (relatives, friends)", "Bank statements", "Marriage invitation"],
        "helplines": ["181", "112"]
    },
    "rape_sexual_assault": {
        "keywords": ["rape", "assault", "forced sex", "molest", "gang rape", "penetration", "pocso", "minor", "child"],
        "title": "🔴 Rape & Sexual Assault",
        "severity": "Critical",
        "response_time": "Immediate",
        "laws": ["IPC 375 (rape)", "IPC 376 (punishment)", "POCSO Act, 2012 (for minors)", "Bharatiya Nyaya Sanhita 2023"],
        "immediate_actions": [
            "🚨 Call 112 IMMEDIATELY",
            "🏥 Go to nearest hospital for medical examination (free, DON'T wash or change clothes)",
            "👮 File FIR – your statement recorded by woman police officer",
            "🤝 Contact NGO: RAHI Foundation 1800-11-4313",
            "📞 Call 181 for support"
        ],
        "legal_options": [
            "File FIR – police must register (zero FIR if jurisdiction issue)",
            "Free legal aid under Legal Services Authority",
            "In-camera trial (privacy protected)",
            "Claim compensation from State Legal Services Authority",
            "Medical termination of pregnancy if allowed"
        ],
        "documents": ["Medical report", "Clothes worn during assault", "CCTV footage", "Witnesses", "Call records"],
        "helplines": ["112", "181", "1098"]
    },
    "police_negligence": {
        "keywords": ["police not filing", "police refusing", "no fir", "police lazy", "police corrupt", "thana"],
        "title": "👮 Police Negligence",
        "severity": "Medium",
        "response_time": "24 hours",
        "laws": ["Section 154 CrPC", "Section 166A IPC"],
        "immediate_actions": [
            "📝 Get refusal in writing (if police refuse to file FIR)",
            "📞 Call 112 and complain about the specific police station",
            "📧 Send complaint to Superintendent of Police (SP) by email",
            "📞 Contact State Human Rights Commission"
        ],
        "legal_options": [
            "File complaint before Magistrate under Section 156(3) CrPC",
            "Send legal notice to Police Commissioner",
            "File writ petition in High Court",
            "Claim compensation for police negligence"
        ],
        "documents": ["Written refusal", "Date/time of visit", "Police officer name", "Your complaint copy"],
        "helplines": ["112", "15100"]
    },
    "acid_attack": {
        "keywords": ["acid", "throw acid", "burn", "chemical", "face burn", "corrosive", "vitriol"],
        "title": "🧪 Acid Attack",
        "severity": "Critical",
        "response_time": "Immediate",
        "laws": ["IPC 326A (acid attack – minimum 10 years, maximum life)", "IPC 326B (attempted acid attack)"],
        "immediate_actions": [
            "🚨 Call 112 IMMEDIATELY",
            "🏥 Go to nearest hospital (acid attack is medical emergency)",
            "💧 Do NOT rub, wash with running water continuously",
            "👮 Police must file FIR under non-bailable sections",
            "📞 Call 181 for support and rehabilitation"
        ],
        "legal_options": [
            "File FIR – strict punishment (minimum 10 years)",
            "Claim compensation up to ₹15 lakhs from State",
            "Free medical treatment and rehabilitation",
            "In-camera trial for privacy",
            "Apply for disability certificate for benefits"
        ],
        "documents": ["Medical report", "Clothes", "Witnesses", "CCTV footage", "Acid bottle (if available)"],
        "helplines": ["112", "181"]
    },
    "property_dispute": {
        "keywords": ["land", "plot", "house", "property", "ownership", "encroachment", "boundary", "will", "inheritance", "ancestral"],
        "title": "🏠 Property Dispute",
        "severity": "Medium",
        "response_time": "1 week",
        "laws": ["Transfer of Property Act", "Registration Act", "Specific Relief Act", "Indian Succession Act"],
        "immediate_actions": [
            "📑 Collect all property documents (sale deed, gift deed, will)",
            "📸 Take photos of encroachment or boundary dispute",
            "📝 Send legal notice to other party",
            "🚫 Do NOT forcibly remove encroachment – go to court"
        ],
        "legal_options": [
            "File civil suit for possession",
            "Injunction to stop construction/encroachment",
            "File police complaint if criminal trespass",
            "Mutation in revenue records",
            "Approach Lok Adalat for settlement"
        ],
        "documents": ["Sale deed", "Property tax receipts", "Encumbrance certificate", "Survey map", "Will (if inheritance)"],
        "helplines": ["15100"]
    },
    "cheating_fraud": {
        "keywords": ["cheat", "fraud", "scam", "fake", "promise", "money taken", "investment fraud", "online fraud", "loan fraud", "credit card fraud"],
        "title": "💸 Cheating / Fraud",
        "severity": "High",
        "response_time": "24 hours",
        "laws": ["IPC 420 (cheating)", "IPC 406 (criminal breach of trust)", "IT Act for online fraud"],
        "immediate_actions": [
            "📞 Call 1930 (cyber fraud helpline) IMMEDIATELY",
            "🔒 Freeze bank account (contact bank immediately)",
            "📸 Save all transaction screenshots",
            "📞 Call police cyber cell"
        ],
        "legal_options": [
            "File FIR under Section 420",
            "Consumer court complaint if product/service fraud",
            "Complaint to RBI for banking fraud",
            "Civil suit for recovery of money",
            "Claim compensation"
        ],
        "documents": ["Payment receipts", "Bank statements", "Communication screenshots", "Contract/agreement"],
        "helplines": ["1930", "112"]
    }
}

# ========== HELPLINES ==========
helplines = {
    "🚓 Police Emergency": "112",
    "👩 Women Helpline": "181",
    "💻 Cyber Crime": "1930",
    "⚖️ NCW": "7827170170",
    "👶 Child Helpline (POCSO)": "1098",
    "📚 Legal Aid Helpline": "15100",
    "👴 Senior Citizens Helpline": "14567",
    "🤝 RAHI (Sexual assault support)": "1800-11-4313"
}

# ========== UTILITY FUNCTIONS ==========
def find_scenario(user_input):
    user_input = user_input.lower()
    scores = {}
    for sid, data in legal_knowledge.items():
        score = 0
        for kw in data["keywords"]:
            if kw in user_input:
                score += 1
        if score > 0:
            scores[sid] = score
    if scores:
        best = max(scores, key=scores.get)
        return best, legal_knowledge[best], scores[best]
    return None, None, 0

def save_to_history(question, scenario):
    st.session_state.history.append({
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "question": question[:100],
        "scenario": scenario if scenario else "Unmatched",
        "case_id": st.session_state.case_id
    })

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("### ⚖️ AI Public Defender")
    st.markdown("*Your legal companion*")
    st.markdown("---")
    
    # Quick stats
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-number">12</div>Legal Scenarios</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-number">24/7</div>Available</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Emergency helplines
    st.markdown("### 🚨 Emergency Helplines")
    for name, num in helplines.items():
        st.markdown(f"**{name}**  \n`{num}`")
    
    st.markdown("---")
    
    # Supported issues
    with st.expander("📋 Supported Issues (12)", expanded=False):
        for issue in legal_knowledge.keys():
            st.markdown(f"• {legal_knowledge[issue]['title']}")
    
    st.markdown("---")
    
    # Session info
    st.caption(f"Session ID: #{st.session_state.case_id}")
    if st.session_state.history:
        st.caption(f"Queries: {len(st.session_state.history)}")

# ========== MAIN CONTENT ==========
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>⚖️ AI Public Defender</h1>
    <p>Intelligent legal guidance. Free. Private. Empowering.</p>
</div>
""", unsafe_allow_html=True)

# Emergency banner
st.markdown("""
<div class="emergency-banner">
    <span>🚨 IMMEDIATE HELP: Police 112 | Women 181 | Cyber 1930 | Legal Aid 15100 🚨</span>
</div>
""", unsafe_allow_html=True)

# Input section
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 📝 Describe your legal situation")
st.markdown("*Be specific – include what happened, who did it, and when*")

user_input = st.text_area(
    "", 
    height=120, 
    placeholder="Example: My husband has been physically abusing me for 2 years. He demands dowry and threatens to kill me. I have photos of my injuries.",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    search_btn = st.button("🔍 Analyze My Situation", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Process input
if search_btn and user_input:
    with st.spinner("Analyzing your situation..."):
        scenario_id, data, confidence = find_scenario(user_input)
        save_to_history(user_input, scenario_id)
    
    if data:
        # Confidence indicator
        if confidence >= 3:
            st.success(f"✅ **High confidence match** – {data['title']}")
        elif confidence >= 2:
            st.info(f"📌 **Medium confidence match** – {data['title']}")
        else:
            st.warning(f"⚠️ **Low confidence match** – {data['title']}")
        
        # Main result card
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        # Title and severity
        st.markdown(f"## {data['title']}")
        severity_colors = {"Critical": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}
        st.markdown(f"**Severity:** {severity_colors.get(data['severity'], '⚪')} {data['severity']} | **Response needed:** {data['response_time']}")
        st.markdown("---")
        
        # Laws
        st.markdown('<p class="section-title">📚 Laws That Protect You</p>', unsafe_allow_html=True)
        for law in data["laws"]:
            st.markdown(f'<span class="badge">{law}</span>', unsafe_allow_html=True)
        st.markdown("")
        
        # Immediate actions
        st.markdown('<p class="section-title">🚨 What You Can Do RIGHT NOW</p>', unsafe_allow_html=True)
        for action in data["immediate_actions"]:
            st.markdown(f"- {action}")
        
        # Legal options
        with st.expander("⚖️ Detailed Legal Options (Click to expand)"):
            for opt in data["legal_options"]:
                st.markdown(f"• {opt}")
        
        # Documents
        with st.expander("📄 Documents to Collect (Click to expand)"):
            for doc in data["documents"]:
                st.markdown(f"• {doc}")
        
        # Helplines for this scenario
        if data.get("helplines"):
            st.markdown("---")
            st.markdown("### 📞 Specific Helplines for Your Situation")
            cols = st.columns(len(data["helplines"]))
            for idx, hl in enumerate(data["helplines"]):
                name = [n for n, num in helplines.items() if num == hl]
                name = name[0] if name else hl
                cols[idx].markdown(f"**{name}**  \n`{hl}`")
        
        # Download guide
        guide = f"""AI PUBLIC DEFENDER - LEGAL GUIDE
Case ID: #{st.session_state.case_id}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{data['title']} (Severity: {data['severity']})

LAWS:
{chr(10).join(data['laws'])}

IMMEDIATE ACTIONS:
{chr(10).join(data['immediate_actions'])}

LEGAL OPTIONS:
{chr(10).join(data['legal_options'])}

DOCUMENTS NEEDED:
{chr(10).join(data['documents'])}

HELPLINES:
{chr(10).join([f'{k}: {v}' for k,v in helplines.items()])}

Disclaimer: This is for informational purposes only. Consult a lawyer for specific advice.
"""
        st.download_button("📥 Download Complete Legal Guide (TXT)", guide, file_name=f"legal_guide_{scenario_id}_{st.session_state.case_id}.txt", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ **We couldn't match your situation**")
        st.markdown("""
        ### 💡 Try these tips:
        - Use specific words like **"hit"**, **"harass"**, **"deposit not returned"**, **"divorce"**, **"custody"**
        - Mention **who** did it (husband, boss, landlord, stranger)
        - Include **what** happened (abuse, fraud, eviction, threat)
        """)
        st.info("📞 **Need immediate help? Call Legal Aid Helpline: 15100** (Free, confidential)")

elif search_btn and not user_input:
    st.error("📝 Please describe your situation before clicking the button.")

# History section
if st.session_state.history:
    with st.expander("📜 Your Query History", expanded=False):
        for h in st.session_state.history[-5:]:
            st.markdown(f"**{h['timestamp']}** – {h['scenario']}  \n*\"{h['question']}...\"*")
            st.markdown("---")

# Footer
st.markdown("""
<div class="footer">
    ⚖️ AI Public Defender – Hackathon 2026<br>
    <span style="font-size: 0.75rem;">Not a substitute for a lawyer. In emergency, call 112.</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)