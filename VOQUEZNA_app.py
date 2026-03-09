"""
ROACCUTANE (Isotretinoin) - Professional Drug Information App
Pre-Pharmacode V2.5 Standard
FDA-verified | Evidence-based | Updated February 2026
Reference ID: FDA-Isotretinoin-2024
"""

import streamlit as st
import os
from datetime import datetime

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="ROACCUTANE (Isotretinoin) Info",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS (LIGHT + DARK MODE) ====================
st.markdown("""
<style>
    /* إخفاء القائمة الجانبية تماماً */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* إخفاء زر المشاركة والقائمة العلوية */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden; height: 0 !important; padding: 0 !important; margin: 0 !important; min-height: 0 !important;}
    footer {visibility: hidden;}
    
    /* تحسين الهوامش الرئيسية للموبايل */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
        max-width: 100% !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0066B1;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #0066B1 0%, #004F8A 50%, #0080D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #3C4C5A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #E8F0F8;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #0066B1;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .warning-box {
        background-color: #FDF0F1;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #C4293A;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .success-box {
        background-color: #EDF7F1;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #1A8748;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .critical-box {
        background-color: #FDF0F1;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #C4293A;
        margin: 0.8rem 0;
        border: 2px solid #C4293A;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* تحسين التبويبات للموبايل */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        flex-wrap: wrap !important;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        padding: 0 12px;
        background-color: #F0F5FB;
        border-radius: 8px;
        font-size: 0.9rem;
        white-space: nowrap;
        flex: 0 1 auto;
        margin: 2px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0066B1;
        color: white;
    }
    /* إخفاء الخط السفلي للتبويبة النشطة */
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }
    
    /* تحسين العرض على الموبايل */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        .main-header {
            font-size: 1.6rem;
            padding: 0.5rem 0;
        }
        
        .sub-header {
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 3px;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.75rem;
            padding: 0 6px;
            height: 38px;
            min-width: auto;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.8rem;
            font-size: 0.9rem;
        }
        
        .info-box h3, .warning-box h3, .success-box h3, .critical-box h3,
        .info-box h4, .warning-box h4, .success-box h4, .critical-box h4 {
            font-size: 1rem;
        }
        
        /* جعل الأعمدة تتراص عمودياً على الموبايل */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        
        /* تحسين حجم النصوص */
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        h4 { font-size: 1rem !important; }
        
        .element-container {
            margin-bottom: 0.5rem;
        }
    }
    
    /* شاشات أصغر (هواتف صغيرة) */
    @media (max-width: 480px) {
        .main-header {
            font-size: 1.3rem;
        }
        
        .sub-header {
            font-size: 0.85rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.7rem;
            padding: 0 4px;
            height: 34px;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.6rem;
            font-size: 0.85rem;
            border-radius: 8px;
        }
    }
    
    /* تنسيق صورة الدواء */
    .drug-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
    }
    
    /* تنسيق المصادر */
    .reference-item {
        background-color: #F0F5FB;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 3px solid #0066B1;
    }
    .reference-item strong { color: #0066B1; font-size: 1.05rem; }
    .reference-item a { color: #0080D4; text-decoration: none; word-break: break-all; display: block; margin-top: 0.3rem; }
    .reference-item a:hover { color: #0066B1; text-decoration: underline; }
    
    /* بطاقات المعلومات بدل الجداول */
    .card-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.6rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        transition: box-shadow 0.3s ease, transform 0.2s ease;
    }
    .card-item:hover { box-shadow: 0 4px 12px rgba(200, 0, 110, 0.18); transform: translateY(-1px); }
    .card-item h4 { margin: 0 0 0.5rem 0; color: #C8006E; font-size: 1.05rem; }
    .card-item .card-detail { font-size: 0.92rem; color: #3C4C5A; margin: 0.25rem 0; line-height: 1.5; }
    .card-item .card-detail strong { color: #475569; }
    .card-item .card-badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.82rem; font-weight: 600; margin-right: 4px; }
    .card-badge-red { background: #FDEAEA; color: #C4293A; }
    .card-badge-green { background: #E5F5EC; color: #1A8748; }
    .card-badge-blue { background: #E0EEF9; color: #0066B1; }
    .card-badge-yellow { background: #FBF7EC; color: #B8920E; }
    .card-badge-purple { background: #F0EAF8; color: #9B8EC4; }
    
    @media (max-width: 768px) {
        .card-item { padding: 0.8rem; margin: 0.4rem 0; }
        .card-item h4 { font-size: 0.95rem; }
        .card-item .card-detail { font-size: 0.85rem; }
    }
    
    /* ============================== DARK MODE ============================== */
    @media (prefers-color-scheme: dark) {
        .main-header {
            background: linear-gradient(135deg, #5AA8E0 0%, #7CBDE8 50%, #E07CB0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sub-header { color: #94a3b8; }
        
        /* ---- Info Box (Roche blue) ---- */
        .info-box { background-color: #0B1A2C; border-left-color: #5AA8E0; color: #e2e8f0; }
        .info-box h3, .info-box h4, .info-box h5 { color: #7CBDE8 !important; }
        .info-box p, .info-box li, .info-box em { color: #cbd5e1; }
        .info-box strong { color: #f1f5f9; }
        .info-box a { color: #5AA8E0; }
        
        /* ---- Warning Box (harmonized red) ---- */
        .warning-box { background-color: #2A1215; border-left-color: #E05B5B; color: #e2e8f0; }
        .warning-box h3, .warning-box h4, .warning-box h5 { color: #EF8F8E !important; }
        .warning-box p, .warning-box li, .warning-box em { color: #cbd5e1; }
        .warning-box strong { color: #f1f5f9; }
        
        /* ---- Success Box (harmonized green) ---- */
        .success-box { background-color: #0E1F14; border-left-color: #3BBD6C; color: #e2e8f0; }
        .success-box h3, .success-box h4, .success-box h5 { color: #6CD798 !important; }
        .success-box p, .success-box li, .success-box em { color: #cbd5e1; }
        .success-box strong { color: #f1f5f9; }
        
        /* ---- Critical Box (harmonized dark red) ---- */
        .critical-box { background-color: #2D1114; border-color: #C4293A; border-left-color: #C4293A; color: #e2e8f0; }
        .critical-box h2, .critical-box h3, .critical-box h4, .critical-box h5 { color: #EF8F8E !important; }
        .critical-box p, .critical-box li, .critical-box em { color: #cbd5e1; }
        .critical-box strong { color: #f1f5f9; }
        .critical-box span { color: #EF8F8E !important; }
        
        /* ---- Cards ---- */
        .card-item { background: #1A2536; border-color: #2D3D50; box-shadow: 0 1px 3px rgba(0,0,0,0.4); }
        .card-item:hover { box-shadow: 0 4px 12px rgba(200, 0, 110, 0.2); transform: translateY(-1px); }
        .card-item h4 { color: #E07CB0; }
        .card-item .card-detail { color: #cbd5e1; }
        .card-item .card-detail strong { color: #e2e8f0; }
        
        /* ---- Badges ---- */
        .card-badge-red { background: #3D0F12; color: #EF8F8E; }
        .card-badge-green { background: #0A2814; color: #6CD798; }
        .card-badge-blue { background: #0C2440; color: #7CBDE8; }
        .card-badge-yellow { background: #332508; color: #E8C45A; }
        .card-badge-purple { background: #2A2040; color: #BDB2DA; }
        
        /* ---- Metric Card ---- */
        .metric-card { background: #1A2536; box-shadow: 0 2px 4px rgba(0,0,0,0.4); color: #e2e8f0; }
        
        /* ---- References ---- */
        .reference-item { background-color: #1A2536; border-left-color: #5AA8E0; }
        .reference-item strong { color: #7CBDE8; }
        .reference-item a { color: #5AA8E0; }
        .reference-item a:hover { color: #7CBDE8; }
        
        /* ---- Links inside boxes ---- */
        .info-box a:hover, .warning-box a:hover,
        .success-box a:hover, .critical-box a:hover { color: #7CBDE8; }
        
        /* ---- Tabs (unselected) ---- */
        .stTabs [data-baseweb="tab"] { background-color: #1A2536; color: #cbd5e1; }
        .stTabs [aria-selected="true"] { background-color: #0066B1; color: white; }
    }

    /* ===== EXPANDER / ACCORDION STYLES ===== */
    /* Legacy Streamlit class names */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #0066B1, #0080D4) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        border: none !important;
    }
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #004F8A, #0066B1) !important;
        box-shadow: 0 4px 12px rgba(0, 102, 177, 0.35) !important;
        transform: translateY(-1px) !important;
    }
    .streamlit-expanderHeader p { color: white !important; margin: 0 !important; }
    .streamlit-expanderHeader svg { fill: white !important; }
    .streamlit-expanderContent {
        border: 1px solid #D0DDE8 !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
        padding: 1rem !important;
    }

    /* data-testid selectors (modern Streamlit) */
    [data-testid="stExpander"] {
        border: none !important;
        border-radius: 10px !important;
        margin-bottom: 0.8rem !important;
        overflow: hidden !important;
        box-shadow: 0 2px 6px rgba(0, 102, 177, 0.1) !important;
    }
    [data-testid="stExpander"] details {
        border: none !important;
    }
    [data-testid="stExpander"] summary {
        background: linear-gradient(135deg, #0066B1, #0080D4) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stExpander"] summary:hover {
        background: linear-gradient(135deg, #004F8A, #0066B1) !important;
        box-shadow: 0 4px 12px rgba(0, 102, 177, 0.35) !important;
    }
    [data-testid="stExpander"] summary span { color: white !important; }
    [data-testid="stExpander"] summary svg { fill: white !important; color: white !important; }
    [data-testid="stExpander"] details[open] summary {
        border-radius: 10px 10px 0 0 !important;
    }
    [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        border: 2px solid #0080D4 !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
        padding: 1rem !important;
    }

    /* Broad fallback selectors for any Streamlit version */
    .st-expander {
        border: none !important;
        border-radius: 10px !important;
        margin-bottom: 0.8rem !important;
        overflow: hidden !important;
        box-shadow: 0 2px 6px rgba(0, 102, 177, 0.1) !important;
    }
    .st-expander details {
        border: none !important;
    }
    .st-expander summary {
        background: linear-gradient(135deg, #0066B1, #0080D4) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .st-expander summary:hover {
        background: linear-gradient(135deg, #004F8A, #0066B1) !important;
        box-shadow: 0 4px 12px rgba(0, 102, 177, 0.35) !important;
    }
    .st-expander summary span { color: white !important; }
    .st-expander summary svg { fill: white !important; color: white !important; }
    .st-expander details[open] summary {
        border-radius: 10px 10px 0 0 !important;
    }

    @media (max-width: 768px) {
        .streamlit-expanderHeader,
        [data-testid="stExpander"] summary,
        .st-expander summary {
            font-size: 0.9rem !important;
            padding: 0.6rem 0.8rem !important;
        }
    }
    @media (prefers-color-scheme: dark) {
        [data-testid="stExpander"],
        .st-expander { box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important; }

        [data-testid="stExpander"] summary,
        .st-expander summary { background: linear-gradient(135deg, #004F8A, #0066B1) !important; }

        [data-testid="stExpander"] summary:hover,
        .st-expander summary:hover { background: linear-gradient(135deg, #003D6B, #004F8A) !important; }

        [data-testid="stExpander"] [data-testid="stExpanderDetails"],
        .streamlit-expanderContent,
        .st-expander [data-testid="stExpanderDetails"] { border-color: #2D3D50 !important; background-color: #0C1520 !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER WITH DRUG IMAGE ====================
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ROACCUTANE.png")
if not os.path.exists(image_path):
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ROACCUTANE.png")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("⚠️ Drug box image not found. Please place ROACCUTANE.png in the app folder.")

st.markdown('<h1 class="main-header">💊 ROACCUTANE (Isotretinoin)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">✅ FDA-verified • 🔬 Evidence-based • 📅 Updated February 2026</p>', unsafe_allow_html=True)

st.markdown("---")

# ==================== MAIN TABS ====================
tabs = st.tabs([
    "📖 Overview",
    "⚗️ Mechanism",
    "💊 Dosage",
    "⚖️ Pharmacokinetics",
    "🚫 Contraindications",
    "⚠️ Side Effects",
    "💊⚖️ Interactions",
    "📊 Comparison",
    "📚 References",
    "🏢 Roche AG"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.header("📖 Overview of ROACCUTANE (Isotretinoin)")

    st.markdown("""
    <div class="info-box">
    <h4>ℹ️ Basic Information</h4>
    <p class="card-detail">🧪 <strong>Generic Name:</strong> Isotretinoin</p>
    <p class="card-detail">🏷️ <strong>Brand Names:</strong> Accutane® (US, discontinued original), Roaccutane® (Global), Absorica®, Absorica LD®</p>
    <p class="card-detail">� <strong>Original Manufacturer:</strong> F. Hoffmann-La Roche AG</p>
    <p class="card-detail">💊 <strong>Drug Class:</strong> Retinoid (Vitamin A Derivative)</p>
    <p class="card-detail">📅 <strong>FDA Approval:</strong> 1982</p>
    <p class="card-detail">📋 <strong>REMS Program:</strong> iPLEDGE — Mandatory for all prescribers, patients, and pharmacies</p>
    <p class="card-detail">📌 <strong>NDA Reference:</strong> 021951 / 211913</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Indications & Available Strengths")
    st.markdown("""
    <div class="info-box">
    <h4>👨‍⚕️ Primary Indication:</h4>
    <ul>
        <li><strong>Treatment of severe recalcitrant nodular acne in non-pregnant patients 12 years of age and older</strong></li>
        <li><em>Nodules:</em> Inflammatory lesions with a diameter of ≥5 mm (may become suppurative or hemorrhagic)</li>
        <li><em>"Severe":</em> Defined as "many" nodules as opposed to "few or several"</li>
        <li><em>Prescribing Prerequisite:</em> Reserved ONLY for patients unresponsive to conventional therapy, including systemic antibiotics</li>
    </ul>
    <h4>📋 Limitations of Use:</h4>
    <ul>
        <li>A single course of therapy for <strong>15 to 20 weeks</strong> has been shown to result in complete and prolonged remission</li>
        <li>If a second course is needed, it is <strong>not recommended</strong> before a <strong>two-month (8-week) waiting period</strong>, as acne may continue to improve off-therapy</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏆 Key Clinical Points"):
        st.markdown("""
        <div class="success-box">
        <h4>✅ Unique Efficacy:</h4>
        <ul>
            <li>🎯 <strong>Only agent capable of inducing permanent acne remission</strong></li>
            <li>📊 Complete and prolonged remission after a single 15–20 week course</li>
            <li>📅 FDA Approved: 1982 (Accutane®/Roaccutane® by Roche)</li>
        </ul>
        <h4>⚠️ Critical Safety Notes:</h4>
        <ul>
            <li>🚨 <strong>Category X — iPLEDGE REMS Program REQUIRED</strong> — Extreme teratogenic risk</li>
            <li>⚠️ Two forms of contraception required for females of reproductive potential</li>
            <li>🔬 Monthly pregnancy tests, LFTs, and lipid panel monitoring mandatory</li>
            <li>🧠 Monitor for psychiatric adverse effects (depression, suicidal ideation)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)



# ==================== TAB 2: MECHANISM ====================
with tabs[1]:
    st.header("⚗️ Mechanism of Action")

    st.markdown("### 🔬 Retinoid Overview")
    st.markdown("""
    <div class="info-box">
    <h3 style="color: #1e3a8a;">🔬 Systemic Retinoid — Multi-Target Action</h3>
    <p>Isotretinoin (13-cis-retinoic acid) is a naturally occurring derivative of Vitamin A. It is the <strong>only drug that addresses all four major pathogenic factors of acne</strong>: sebum production, follicular keratinization, bacterial colonization (<em>Cutibacterium acnes</em>), and inflammation. Its unique ability to cause irreversible shrinkage of sebaceous glands is the basis for its capacity to induce long-term remission.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⚙️ Detailed Mechanism"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 1️⃣ Sebaceous Gland Suppression")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Primary Mechanism</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Induces apoptosis of sebocytes, causing <strong>irreversible shrinkage of sebaceous glands</strong> (up to 90% reduction in size)</li>
                <li>Dramatically reduces sebum production (up to an 80% reduction)</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Removes the lipid-rich environment essential for <em>C. acnes</em> proliferation</li>
                <li>✅ This permanent gland alteration is the basis for long-term remission</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### 2️⃣ Normalization of Keratinization")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Anti-Comedogenic Effect</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Normalizes follicular epithelial desquamation, preventing formation of the keratin plug (microcomedone)</li>
                <li>Reduces hyperkeratosis within the pilosebaceous unit</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Prevents follicular occlusion — the initial step in all acne lesion formation</li>
                <li>✅ Eliminates existing comedones (blackheads/whiteheads)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("### 3️⃣ Anti-inflammatory Action")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Immune Modulation</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Inhibits neutrophil chemotaxis and migration to the follicle</li>
                <li>Suppresses pro-inflammatory mediators (lipoxygenase products)</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Reduces redness, swelling, and pain of nodular lesions</li>
                <li>✅ Facilitates healing and reduces post-inflammatory scarring</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### 4️⃣ Indirect Antibacterial Effect")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Microbial Reduction</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Does NOT directly kill bacteria</li>
                <li>By shrinking sebaceous glands and reducing sebum, it eliminates the anaerobic, lipid-rich environment that <em>C. acnes</em> requires to thrive</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Significant reduction in <em>C. acnes</em> colony counts</li>
                <li>✅ No risk of antibiotic resistance (unlike doxycycline)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 3: DOSAGE ====================
with tabs[2]:
    st.header("💊 Dosage and Administration")
    st.markdown("### 👨‍⚕️ Important Notes & Standard Dosing")
    st.markdown("""
    <div class="critical-box">
    <h3 style="color: #dc2626; text-align: center;">🚨 iPLEDGE REMS PROGRAM — MANDATORY 🚨</h3>
    <p style="font-size: 1.1rem; font-weight: bold; text-align: center;">
    Isotretinoin is ONLY available through the iPLEDGE REMS program. All prescribers, patients, and dispensing pharmacies MUST be registered and comply with all requirements before dispensing.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-item">
        <h4>1️⃣ Standard Dosing (Generic / Absorica)</h4>
        <p class="card-detail"><strong>Dose:</strong> 0.5 to 1 mg/kg/day</p>
        <p class="card-detail"><strong>Schedule:</strong> Given in two divided doses daily</p>
        <p class="card-detail"><strong>Duration:</strong> 15 to 20 weeks</p>
        <p class="card-detail"><strong>Food:</strong> Generic isotretinoin MUST be taken with a high-fat meal to ensure absorption. Absorica may be taken with or without food.</p>
    </div>
    <div class="card-item">
        <h4>2️⃣ Micronized Dosing (Absorica LD)</h4>
        <p class="card-detail"><strong>Dose:</strong> 0.4 to 0.8 mg/kg/day</p>
        <p class="card-detail"><strong>Schedule:</strong> Given in two divided doses daily</p>
        <p class="card-detail"><strong>Duration:</strong> 15 to 20 weeks</p>
        <p class="card-detail"><span class="card-badge card-badge-red">NOT interchangeable with Absorica — different bioavailability</span></p>
    </div>
    <div class="card-item">
        <h4>3️⃣ Very Severe Disease / Trunk Acne (Adults)</h4>
        <p class="card-detail"><strong>Dose:</strong> Up to 2 mg/kg/day (or 1.6 mg/kg/day for Absorica LD)</p>
        <p class="card-detail"><strong>Schedule:</strong> Given in divided doses, as tolerated</p>
        <p class="card-detail"><strong>Note:</strong> For adult patients with severe scarring or disease primarily manifested on the trunk</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📉 Dose Adjustments & Discontinuation"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔄 Discontinuation Criteria")
            st.markdown("""
            <div class="card-item">
                <h4>✅ Early Discontinuation</h4>
                <p class="card-detail">The drug may be discontinued early if the total nodule count has been reduced by more than <strong>70%</strong> prior to completing 15 to 20 weeks.</p>
            </div>
            <div class="card-item">
                <h4>🔄 Second Course</h4>
                <p class="card-detail">If a second course is needed, wait a minimum of <strong>8 weeks (2 months)</strong> after the first course, as acne may continue to improve off-therapy.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("#### 💊 Missed Dose")
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>⚠️ Missed Dose Instructions</h4>
                <p class="card-detail"><strong>Action:</strong> Skip the missed dose. Do NOT take two doses at the same time.</p>
                <p class="card-detail"><strong>Important:</strong> Take the next dose at the regularly scheduled time.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("#### 🚫 Dosing Warnings")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>❌ Once-daily dosing is <strong>NOT recommended</strong></li>
                <li>💊 Swallow capsules whole with a full glass of liquid</li>
                <li>⚠️ Decreases the risk of esophageal irritation</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📋 Administration Instructions"):
        st.success("""
        ✅ Generic isotretinoin: MUST be taken with a high-fat meal for proper absorption

        ✅ Absorica / Absorica LD: May be taken with or without food

        ✅ Swallow capsules whole with a full glass of liquid — decreases esophageal irritation risk

        ❌ Once-daily dosing is NOT recommended — always divide into two daily doses

        ❌ Do NOT double the dose if a dose is missed — skip and resume at next scheduled time
        """)

# ==================== TAB 4: PHARMACOKINETICS ====================
with tabs[3]:
    st.header("⚖️ Pharmacokinetics")
    st.markdown("### 📊 PK Parameters Summary")
    st.markdown("""
    <div class="card-item">
        <h4>📊 Isotretinoin (Parent Drug)</h4>
        <p class="card-detail"><strong>Bioavailability:</strong> ~25% (fasting); significantly increased with high-fat meal</p>
        <p class="card-detail"><strong>Tmax:</strong> 3–5 hours</p>
        <p class="card-detail"><strong>Half-life:</strong> ~21 hours (terminal elimination)</p>
        <p class="card-detail"><strong>Protein Binding:</strong> 99.9%</p>
        <p class="card-detail"><strong>Metabolism:</strong> Hepatic — oxidation via CYP2C8, CYP3A4, CYP2C9, CYP2B6; also glucuronidation</p>
        <p class="card-detail"><strong>Active Metabolite:</strong> 4-oxo-isotretinoin (comparable plasma levels after steady state)</p>
    </div>
    <div class="card-item">
        <h4>📊 4-oxo-Isotretinoin (Major Active Metabolite)</h4>
        <p class="card-detail"><strong>Half-life:</strong> ~24 hours</p>
        <p class="card-detail"><strong>Protein Binding:</strong> 99.9%</p>
        <p class="card-detail"><strong>Clinical Note:</strong> Reaches plasma levels exceeding those of the parent drug at steady state; contributes to overall clinical activity</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🧬 Distribution, Metabolism & Elimination"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧬 Distribution")
            st.info("""
            **Protein Binding:** 99.9% (primarily to albumin)

            **Tissue Distribution:**
            - Lipophilic — distributes well to skin and sebaceous glands
            - Crosses the placenta — basis for extreme teratogenicity

            **Food Effect:**
            - Generic: Bioavailability doubles with a high-fat meal
            - Absorica/Absorica LD: Designed for food-independent absorption
            """)
            st.markdown("### 🔄 Metabolism")
            st.warning("""
            **CYP Enzymes Involved:**
            - CYP2C8, CYP3A4, CYP2C9, CYP2B6

            **Key Metabolic Pathway:**
            - Oxidation to 4-oxo-isotretinoin (major active metabolite)
            - Glucuronidation and further oxidation

            **Enterohepatic Recirculation:**
            - Contributes to prolonged half-life
            """)
        with col2:
            st.markdown("### 🚰 Elimination")
            st.markdown("""
            <div class="card-item">
                <h4>🚰 Renal — Urine</h4>
                <p class="card-detail">Excreted in urine as metabolites and conjugates</p>
            </div>
            <div class="card-item">
                <h4>💩 Fecal — Bile</h4>
                <p class="card-detail">Excreted in feces via biliary elimination; enterohepatic recirculation extends duration</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### 👥 Special Populations")
            st.warning("""
            **Pediatric (<12 years):**
            - Not indicated; safety and efficacy not established

            **Hepatic Impairment:**
            - Use with extreme caution; isotretinoin is hepatotoxic
            - Monitor LFTs closely; discontinue if significant elevation

            **Renal Impairment:**
            - No specific dosage adjustments in labeling

            **Elderly:**
            - Not typically indicated for this population
            """)

# ==================== TAB 5: CONTRAINDICATIONS ====================
with tabs[4]:
    st.header("🚫 Contraindications and Warnings")

    st.markdown("### ⚠️ Boxed Warning & Absolute Contraindications")
    st.markdown("""
    <div class="critical-box">
    <h2 style="color: #dc2626; text-align: center;">🚨 BOXED WARNING — TERATOGENICITY 🚨</h2>
    <p style="font-size: 1.1rem; text-align: center; font-weight: bold;">
    Isotretinoin MUST NOT be used by female patients who are or may become pregnant. There is an extremely high risk that severe birth defects will result if pregnancy occurs while taking isotretinoin in any amount, even for short periods of time. Potentially any fetus exposed during pregnancy can be affected. iPLEDGE REMS program is MANDATORY.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 1. Pregnancy (Category X)</h4>
        <p class="card-detail"><strong>Risk:</strong> Extremely high risk of severe birth defects — craniofacial, cardiac, CNS, and thymic malformations</p>
        <p class="card-detail"><strong>Action:</strong> iPLEDGE REMS — two forms of contraception required; monthly pregnancy tests mandatory</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 2. Hypersensitivity</h4>
        <p class="card-detail"><strong>Risk:</strong> Anaphylactic reactions and other allergic reactions</p>
        <p class="card-detail"><strong>Action:</strong> Do not use in patients with known hypersensitivity to isotretinoin or any component (contains parabens, soybean oil)</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 3. Hypervitaminosis A</h4>
        <p class="card-detail"><strong>Risk:</strong> Isotretinoin is a Vitamin A derivative; concurrent use of Vitamin A supplements causes additive toxicity</p>
        <p class="card-detail"><strong>Action:</strong> Patients must NOT take Vitamin A supplements during therapy</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 4. Concomitant Tetracycline Use</h4>
        <p class="card-detail"><strong>Risk:</strong> Additive risk of pseudotumor cerebri (increased intracranial pressure) — may cause permanent vision loss</p>
        <p class="card-detail"><strong>Action:</strong> Do NOT co-administer with tetracyclines (doxycycline, minocycline)</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⚠️ Warnings and Precautions"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🧠 Psychiatric Effects")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>⚠️ <strong>Depression</strong>, psychosis, suicidal ideation, and suicide attempts have been reported</li>
                <li>⚠️ Aggressive and/or violent behavior reported</li>
                <li>🔬 <strong>Action:</strong> Discontinue isotretinoin if significant psychiatric symptoms develop</li>
                <li>📋 Patients should be monitored for signs of depression at each visit</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("#### 🧪 Hepatotoxicity")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>⚠️ Clinical hepatitis and elevated liver transaminases (~15% of patients)</li>
                <li>🔬 <strong>Monitor:</strong> LFTs at baseline, then at regular intervals during therapy</li>
                <li>⚠️ Discontinue if liver enzyme levels fail to return to normal or if hepatitis is suspected</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("#### 🦴 Musculoskeletal Effects")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>⚠️ Premature epiphyseal closure in pediatric patients</li>
                <li>⚠️ Decreased bone mineral density, hyperostosis</li>
                <li>⚠️ Arthralgia, back pain, increased CPK</li>
                <li>🔬 <strong>Caution:</strong> Use with care in patients involved in strenuous physical activity</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("#### 🧠 Pseudotumor Cerebri")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>⚠️ Benign intracranial hypertension — presenting as severe headache, nausea/vomiting, visual disturbances</li>
                <li>🚨 Risk significantly increased with concomitant tetracyclines</li>
                <li>🔬 <strong>Action:</strong> Discontinue immediately and refer for neurological evaluation</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 6: SIDE EFFECTS ====================
with tabs[5]:
    st.header("⚠️ Side Effects")

    st.markdown("### 🔴 Common Effects (>5% Incidence)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-item">
            <h4>💋 Cheilitis (Chapped Lips)</h4>
            <p class="card-detail"><span class="card-badge card-badge-red">Very Common</span></p>
            <p class="card-detail">Most frequent side effect; occurs in nearly all patients. Use lip balm/emollients.</p>
        </div>
        <div class="card-item">
            <h4>🧴 Dry Skin (Xerosis)</h4>
            <p class="card-detail"><span class="card-badge card-badge-red">Very Common</span></p>
            <p class="card-detail">Generalized skin dryness, peeling, and increased skin fragility.</p>
        </div>
        <div class="card-item">
            <h4>👃 Dry Nose / Epistaxis</h4>
            <p class="card-detail"><span class="card-badge card-badge-yellow">Common</span></p>
            <p class="card-detail">Nasal dryness and nosebleeds. Saline nasal spray recommended.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card-item">
            <h4>👁️ Dry Eyes / Conjunctivitis</h4>
            <p class="card-detail"><span class="card-badge card-badge-yellow">Common</span></p>
            <p class="card-detail">May cause contact lens intolerance. Artificial tears recommended.</p>
        </div>
        <div class="card-item">
            <h4>🧪 Hypertriglyceridemia</h4>
            <p class="card-detail"><span class="card-badge card-badge-red">~25% of patients</span></p>
            <p class="card-detail">Elevations >800 mg/dL reported. Monitor lipid panel regularly.</p>
        </div>
        <div class="card-item">
            <h4>🧪 Elevated Liver Transaminases</h4>
            <p class="card-detail"><span class="card-badge card-badge-yellow">~15% of patients</span></p>
            <p class="card-detail">Monitor LFTs at baseline and regular intervals. Discontinue if significant.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h4>📊 Additional Laboratory Changes:</h4>
    <ul>
        <li>📉 Decreased HDL (~15% of patients)</li>
        <li>📈 Increased total cholesterol (~7% of patients)</li>
        <li>🔬 Alterations in fasting blood sugar</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🚨 Serious Reactions"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🧠 Psychiatric Disorders</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">SERIOUS</span></p>
                <p class="card-detail"><strong>Depression</strong>, psychosis, suicidal ideation, suicide attempts, aggressive/violent behavior</p>
                <p class="card-detail"><strong>Action:</strong> Discontinue immediately if symptoms develop</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🧠 Pseudotumor Cerebri</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">SERIOUS</span></p>
                <p class="card-detail">Severe headache, nausea/vomiting, visual disturbances. Risk increased with tetracyclines.</p>
                <p class="card-detail"><strong>Action:</strong> Stop drug immediately; neurological evaluation required</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🫁 Acute Pancreatitis</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">SERIOUS</span></p>
                <p class="card-detail">Often linked to hypertriglyceridemia (triglycerides >800 mg/dL). Cases may be fatal.</p>
                <p class="card-detail"><strong>Action:</strong> Discontinue if pancreatitis is diagnosed</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🧬 Stevens-Johnson Syndrome (SJS) / TEN</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">RARE — LIFE-THREATENING</span></p>
                <p class="card-detail">Severe mucocutaneous reactions including toxic epidermal necrolysis and erythema multiforme</p>
                <p class="card-detail"><strong>Action:</strong> Discontinue immediately; hospitalization required</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🫘 Inflammatory Bowel Disease (IBD)</h4>
                <p class="card-detail"><span class="card-badge card-badge-yellow">REPORTED</span></p>
                <p class="card-detail">Including regional ileitis. Patients with abdominal pain, rectal bleeding, or severe diarrhea should discontinue.</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>👁️ Visual Disturbances</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">POTENTIALLY PERMANENT</span></p>
                <p class="card-detail">Decreased night vision (may persist), corneal opacities</p>
                <p class="card-detail"><strong>Action:</strong> Caution patients about night driving</p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📋 Monitoring & Emergency Signs"):
        st.markdown("""
        <div class="warning-box">
        <h4>🔬 Required Monitoring Schedule:</h4>
        <ul>
            <li>📊 <strong>Lipid Panel:</strong> Baseline + every 2-4 weeks during therapy</li>
            <li>🧪 <strong>LFTs:</strong> Baseline + regular intervals; every 2-4 weeks recommended</li>
            <li>🤰 <strong>Pregnancy Tests:</strong> Monthly (for females of reproductive potential) — via iPLEDGE</li>
            <li>🧠 <strong>Psychiatric Assessment:</strong> At each visit — screen for depression, mood changes</li>
            <li>🦴 <strong>Musculoskeletal:</strong> CPK if symptoms arise; monitor for bone pain</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="critical-box">
        <h4>🚨 SEEK IMMEDIATE MEDICAL ATTENTION FOR:</h4>
        <ul>
            <li>🧠 Severe headaches, blurred vision, or vision changes (pseudotumor cerebri)</li>
            <li>🫁 Severe abdominal pain (pancreatitis)</li>
            <li>🧬 Widespread skin rash, blistering, or mucosal erosion (SJS/TEN)</li>
            <li>💭 New or worsening depression, suicidal thoughts, or mood changes</li>
            <li>🩸 Rectal bleeding or severe diarrhea (IBD)</li>
            <li>👂 New onset hearing impairment or tinnitus</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 7: INTERACTIONS ====================
with tabs[6]:
    st.header("💊⚖️ Drug Interactions")

    st.markdown("### 🔴 Contraindicated & Avoid")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 Tetracyclines (Doxycycline, Minocycline)</h4>
        <p class="card-detail"><span class="card-badge card-badge-red">CONTRAINDICATED</span></p>
        <p class="card-detail"><strong>Mechanism:</strong> Additive pharmacological risk of increased intracranial pressure</p>
        <p class="card-detail"><strong>Clinical Effect:</strong> Pseudotumor cerebri (benign intracranial hypertension) — can cause permanent vision loss</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 Vitamin A Supplements</h4>
        <p class="card-detail"><span class="card-badge card-badge-red">CONTRAINDICATED</span></p>
        <p class="card-detail"><strong>Mechanism:</strong> Additive toxicity (isotretinoin is a Vitamin A derivative)</p>
        <p class="card-detail"><strong>Clinical Effect:</strong> Hypervitaminosis A — compounding hepatotoxic and teratogenic risks</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 Micro-dosed Progesterone ("Minipills")</h4>
        <p class="card-detail"><span class="card-badge card-badge-red">AVOID</span></p>
        <p class="card-detail"><strong>Mechanism:</strong> Isotretinoin alters the pharmacokinetics of micro-dosed progestins</p>
        <p class="card-detail"><strong>Clinical Effect:</strong> Inadequate contraception — unintended pregnancy carries extreme risk of life-threatening fetal abnormalities</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 St. John's Wort</h4>
        <p class="card-detail"><span class="card-badge card-badge-yellow">AVOID</span></p>
        <p class="card-detail"><strong>Mechanism:</strong> CYP3A4 induction increases clearance of oral contraceptives</p>
        <p class="card-detail"><strong>Clinical Effect:</strong> Breakthrough bleeding and contraceptive failure — jeopardizes the two-method contraception requirement</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🟡 Monitor Closely"):
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>⚠️ Phenytoin</h4>
            <p class="card-detail"><span class="card-badge card-badge-yellow">MONITOR</span></p>
            <p class="card-detail"><strong>Mechanism:</strong> Both drugs independently affect bone metabolism</p>
            <p class="card-detail"><strong>Clinical Effect:</strong> Additive risk of osteomalacia and decreased bone mineral density</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>⚠️ Systemic Corticosteroids</h4>
            <p class="card-detail"><span class="card-badge card-badge-yellow">MONITOR</span></p>
            <p class="card-detail"><strong>Mechanism:</strong> Additive negative effect on bone remodeling</p>
            <p class="card-detail"><strong>Clinical Effect:</strong> Increased risk of osteoporosis and bone fractures, especially with prolonged co-administration</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("✅ Safe & CYP Profile"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="success-box">
            <h4>🧬 CYP450 Profile of Isotretinoin:</h4>
            <ul>
                <li><strong>Substrate of:</strong> CYP2C8, CYP3A4, CYP2C9, CYP2B6</li>
                <li><strong>Inhibitor of:</strong> No significant CYP inhibition reported</li>
                <li><strong>Inducer of:</strong> No significant CYP induction reported</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-box">
            <h4>💡 Clinical Note:</h4>
            <p>Isotretinoin's primary drug interaction risk is <strong>pharmacodynamic</strong> (additive toxicity) rather than pharmacokinetic (CYP-mediated). The critical interactions to manage are tetracyclines, Vitamin A, and contraceptive adequacy.</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 8: COMPARISON ====================
with tabs[7]:
    st.header("📊 Drug Comparison — Systemic Acne Agents")

    st.markdown("### 🔬 Isotretinoin vs Alternatives")
    st.markdown("#### Isotretinoin (ROACCUTANE)")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #0460A9;">
        <h4>💊 Isotretinoin (ROACCUTANE / Accutane)</h4>
        <p class="card-detail"><strong>Mechanism:</strong> Shrinks sebaceous glands, normalizes keratinization, anti-inflammatory, indirect antibacterial</p>
        <p class="card-detail"><strong>Primary Indication:</strong> Severe recalcitrant nodular acne</p>
        <p class="card-detail"><strong>Key Interactions:</strong> Tetracyclines, Vitamin A, Minipills, St. John's Wort</p>
        <p class="card-detail"><strong>Pregnancy Risk:</strong> <span class="card-badge card-badge-red">Category X — iPLEDGE REMS required</span></p>
        <p class="card-detail"><strong>Monitoring:</strong> LFTs, Lipid panel, Pregnancy tests (monthly)</p>
        <p class="card-detail"><strong>Clinical Advantage:</strong> <span class="card-badge card-badge-green">ONLY agent capable of inducing permanent acne remission</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Doxycycline (Oral Antibiotic)")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #eab308;">
        <h4>💊 Doxycycline</h4>
        <p class="card-detail"><strong>Mechanism:</strong> Inhibits bacterial protein synthesis & anti-inflammatory</p>
        <p class="card-detail"><strong>Primary Indication:</strong> Moderate to severe inflammatory acne</p>
        <p class="card-detail"><strong>Key Interactions:</strong> Isotretinoin, Antacids, Iron, Warfarin</p>
        <p class="card-detail"><strong>Pregnancy Risk:</strong> <span class="card-badge card-badge-red">Category D — Tooth discoloration</span></p>
        <p class="card-detail"><strong>Monitoring:</strong> Minimal (clinical response)</p>
        <p class="card-detail"><strong>Clinical Advantage:</strong> <span class="card-badge card-badge-blue">Rapid onset for inflammatory lesions</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Spironolactone (Off-label)")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #7c3aed;">
        <h4>💊 Spironolactone</h4>
        <p class="card-detail"><strong>Mechanism:</strong> Aldosterone/Androgen receptor antagonist</p>
        <p class="card-detail"><strong>Primary Indication:</strong> Hormonal acne in adult females (off-label)</p>
        <p class="card-detail"><strong>Key Interactions:</strong> ACE inhibitors, ARBs, K+ supplements</p>
        <p class="card-detail"><strong>Pregnancy Risk:</strong> <span class="card-badge card-badge-yellow">Category C — Feminization of male fetus</span></p>
        <p class="card-detail"><strong>Monitoring:</strong> Renal function, Serum Potassium</p>
        <p class="card-detail"><strong>Clinical Advantage:</strong> <span class="card-badge card-badge-green">Excellent long-term safety profile for females</span></p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏆 When to Choose & Key Differentiators"):
        st.markdown("""
        <div class="success-box">
        <h4>✅ Choose Isotretinoin When:</h4>
        <ul>
            <li>🎯 Severe nodular acne unresponsive to antibiotics and topicals</li>
            <li>📊 Goal is <strong>long-term or permanent remission</strong></li>
            <li>🔬 Patient can comply with iPLEDGE REMS requirements</li>
            <li>⚠️ Patient is NOT pregnant and can commit to two forms of contraception</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        <h4>💡 Choose Doxycycline When:</h4>
        <ul>
            <li>Moderate inflammatory acne requiring quick onset of action</li>
            <li>Patient cannot commit to iPLEDGE / isotretinoin requirements</li>
            <li>Short-term therapy needed (typically 3-6 months)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        <h4>💡 Choose Spironolactone When:</h4>
        <ul>
            <li>Adult female with hormonal/cyclical acne pattern</li>
            <li>Long-term maintenance therapy desired with excellent safety</li>
            <li>Patient prefers to avoid isotretinoin risks</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 9: REFERENCES ====================
with tabs[8]:
    st.header("📚 References and Sources")

    st.markdown("### 🏛️ Primary Regulatory & Safety Sources")
    st.markdown("""
    <div class="reference-item">
        <strong>1. Official FDA Prescribing Information (Label)</strong>
        <p class="card-detail">The primary reference for dosing, contraindications, and drug interactions.</p>
        <a href="https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/021951s015lbl.pdf" target="_blank">https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/021951s015lbl.pdf</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>2. National Institutes of Health (NIH) - DailyMed</strong>
        <p class="card-detail">Comprehensive and up-to-date structured product labeling for Isotretinoin.</p>
        <a href="https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=ISOTRETINOIN" target="_blank">https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=ISOTRETINOIN</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>3. The iPLEDGE® REMS Program</strong>
        <p class="card-detail">Mandatory FDA Risk Evaluation and Mitigation Strategy program documenting the Category X pregnancy risk and contraceptive interactions.</p>
        <a href="https://www.ipledgeprogram.com/" target="_blank">https://www.ipledgeprogram.com/</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📋 Clinical Guidelines & Professional Monographs")
    st.markdown("""
    <div class="reference-item">
        <strong>4. American Academy of Dermatology (AAD) Guidelines</strong>
        <p class="card-detail">Official clinical practice guidelines for the management of acne vulgaris, specifying Isotretinoin use.</p>
        <a href="https://www.aad.org/member/clinical-quality/guidelines/acne" target="_blank">https://www.aad.org/member/clinical-quality/guidelines/acne</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>5. Drugs.com Professional Monograph</strong>
        <p class="card-detail">Detailed pharmacokinetic and drug interaction data backed by IBM Watson Micromedex.</p>
        <a href="https://www.drugs.com/pro/isotretinoin.html" target="_blank">https://www.drugs.com/pro/isotretinoin.html</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>6. UpToDate (Lexicomp Drug Information)</strong>
        <p class="card-detail">Premium clinical decision support resource for systemic Isotretinoin information. (Note: Requires practitioner login for full text).</p>
        <a href="https://www.uptodate.com/contents/isotretinoin-systemic-drug-information" target="_blank">https://www.uptodate.com/contents/isotretinoin-systemic-drug-information</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔬 Verified Clinical Studies (PubMed)")
    st.markdown("""
    <div class="reference-item">
        <strong>7. Drug Interaction Verification: Tetracyclines (PMID: 15152994)</strong>
        <p class="card-detail">Clinical study documenting the risk of Pseudotumor cerebri when combining Isotretinoin with Tetracyclines.</p>
        <a href="https://pubmed.ncbi.nlm.nih.gov/15152994/" target="_blank">https://pubmed.ncbi.nlm.nih.gov/15152994/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>8. Comprehensive Safety & Toxicity Review (PMID: 31600216)</strong>
        <p class="card-detail">Peer-reviewed clinical synthesis of Isotretinoin's adverse effect profile (psychiatric, hepatic, and metabolic).</p>
        <a href="https://pubmed.ncbi.nlm.nih.gov/31600216/" target="_blank">https://pubmed.ncbi.nlm.nih.gov/31600216/</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🏭 Manufacturer & Historical Context")
    st.markdown("""
    <div class="reference-item">
        <strong>9. F. Hoffmann-La Roche AG - Corporate History</strong>
        <p class="card-detail">The official timeline and historical medical milestones of the manufacturer that developed Roaccutane.</p>
        <a href="https://www.roche.com/about/history" target="_blank">https://www.roche.com/about/history</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>10. Historical Medical Context: Roche Innovations</strong>
        <p class="card-detail">NCBI archived article detailing Roche's history in drug discovery (e.g., Benzodiazepines) to support the manufacturer's profile.</p>
        <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4657308/" target="_blank">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4657308/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("""
    **📊 Data Accuracy Statement**

    All information in this application has been verified against:
    - FDA Prescribing Information
    - Peer-reviewed clinical studies and guidelines

    **📅 Last Updated:** February 2026  
    **📌 Version:** 1.0.0  
    **✅ Verification Status:** All references checked and validated  
    **🔬 Methodology:** Pre-Pharmacode V2.5 Standard with Triple-Verification
    """)

# ==================== TAB 10: ROCHE AG ====================
with tabs[9]:
    st.header("🏢 F. Hoffmann-La Roche AG — Manufacturer Profile")

    st.markdown("### 🏛️ Corporate Overview")
    st.markdown("""
    <div class="info-box">
    <p class="card-detail">🏢 <strong>Company Name:</strong> F. Hoffmann-La Roche AG</p>
    <p class="card-detail">📅 <strong>Founded:</strong> October 1, 1896 (by Fritz Hoffmann-La Roche)</p>
    <p class="card-detail">📍 <strong>Headquarters:</strong> Basel, Switzerland 🇨🇭</p>
    <p class="card-detail">🌍 <strong>Global Ranking:</strong> 5th largest pharmaceutical company worldwide by revenue</p>
    <p class="card-detail">🎯 <strong>Leadership Position:</strong> Undisputed global leader in oncology (cancer therapeutics) and in vitro diagnostics</p>
    <p class="card-detail">🏗️ <strong>Divisions:</strong> Pharmaceuticals and Diagnostics — highly integrated and synergistic</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #e74c3c;">
        <h4>💊 History with Roaccutane (Isotretinoin)</h4>
        <p class="card-detail"><strong>1960s:</strong> Isotretinoin was first synthesized and developed within Roche laboratories. The initial clinical goal was to investigate its potential as a treatment for skin cancer.</p>
        <p class="card-detail"><strong>1970s:</strong> Collaborative studies with the National Cancer Institute revealed that while it was ineffective for cancer, it possessed unprecedented efficacy in treating severe, treatment-resistant nodular acne.</p>
        <p class="card-detail"><strong>1982:</strong> Roche secured FDA approval to launch the drug under the brand name <strong>Accutane</strong> (US) and <strong>Roaccutane</strong> (globally). It revolutionized dermatology as the only medication capable of inducing long-term or permanent remission of severe acne.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏆 Leadership & Quick Facts"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #22c55e;">
                <h4>🧪 Vitamin C Pioneer (1934)</h4>
                <p class="card-detail">Became the <strong>first company in history</strong> to achieve mass commercial production of synthetic Vitamin C, marketed as <em>Redoxon</em>.</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #3b82f6;">
                <h4>🧠 Benzodiazepine Revolution (1957)</h4>
                <p class="card-detail">Revolutionized modern psychiatry by discovering the Benzodiazepine class of tranquilizers, later launching iconic medications such as <em>Valium</em> (diazepam).</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #7c3aed;">
                <h4>🧬 Diagnostics Pioneer (1990s)</h4>
                <p class="card-detail">Played a critical role by developing early <strong>HIV diagnostic tests</strong> and acquiring foundational patents for <strong>PCR (Polymerase Chain Reaction)</strong> technology.</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #eab308;">
                <h4>🔬 Current Vision & R&D</h4>
                <p class="card-detail">Invests <strong>billions annually</strong> in R&D with strategic focus on <strong>Personalized Healthcare</strong>, alongside pioneering treatments in immunology, neurology, infectious diseases, and ophthalmology.</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p><strong>ROACCUTANE (Isotretinoin) Professional Drug Information</strong></p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        ⚠️ <em>This information is for healthcare professionals only. 
        Always consult the full prescribing information and clinical judgment when making treatment decisions.</em>
    </p>
</div>
""", unsafe_allow_html=True)
