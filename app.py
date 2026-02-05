from text_extractor import extract_text
from clause_splitter import split_clauses
from risk_detector import detect_risk
from llm_explainer import explain_clause
from contract_classifier import classify_contract
import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Legal Contract Intelligence",
    layout="wide"
)

# -------------------------------------------------
# PREMIUM LEGAL CSS (VERY IMPORTANT)
# -------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f8fafc;
}

h1, h2, h3 {
    color: #0f172a;
}

.container {
    padding: 30px;
}

.card {
    background: #ffffff;
    padding: 26px;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 25px;
}

.subtle {
    color: #64748b;
    font-size: 14px;
}

.stat {
    font-size: 28px;
    font-weight: 600;
    color: #020617;
}

.label {
    font-size: 13px;
    color: #475569;
}

.badge-high {
    background: #fee2e2;
    color: #991b1b;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

.badge-medium {
    background: #fef3c7;
    color: #92400e;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

.badge-low {
    background: #dcfce7;
    color: #166534;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 40px 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("## Legal Contract Intelligence Platform")
st.markdown(
    "<p class='subtle'>AI-assisted contract risk analysis for small and medium enterprises</p>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# UPLOAD SECTION
# -------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### Upload Contract")
file = st.file_uploader(
    "Accepted formats: PDF, DOCX, TXT",
    type=["pdf", "docx", "txt"]
)
st.markdown("<p class='subtle'>All documents are processed locally. No data is stored.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# PROCESS CONTRACT
# -------------------------------------------------
if file:
    text = extract_text(file)
    contract_type = classify_contract(text)
    clauses = split_clauses(text)

    high = medium = low = 0
    for c in clauses:
        risk, _ = detect_risk(c)
        if risk == "High":
            high += 1
        elif risk == "Medium":
            medium += 1
        else:
            low += 1

    # -------------------------------------------------
    # SUMMARY DASHBOARD
    # -------------------------------------------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Contract Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f"<div class='stat'>{contract_type}</div><div class='label'>Contract Type</div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='stat'>{len(clauses)}</div><div class='label'>Clauses</div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='stat'>{high}</div><div class='label'>High Risk</div>", unsafe_allow_html=True)
    col4.markdown(f"<div class='stat'>{medium}</div><div class='label'>Medium Risk</div>", unsafe_allow_html=True)

    if high >= 2:
        st.markdown("<span class='badge-high'>Overall Risk: High</span>", unsafe_allow_html=True)
    elif medium >= 2:
        st.markdown("<span class='badge-medium'>Overall Risk: Medium</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='badge-low'>Overall Risk: Low</span>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # -------------------------------------------------
    # CLAUSE ANALYSIS
    # -------------------------------------------------
    st.markdown("### Clause-Level Analysis")

    for idx, clause in enumerate(clauses, 1):
        risk, reason = detect_risk(clause)
        explanation = explain_clause(clause, risk)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"#### Clause {idx}")
        st.write(clause)

        if risk == "High":
            st.markdown("<span class='badge-high'>High Risk</span>", unsafe_allow_html=True)
        elif risk == "Medium":
            st.markdown("<span class='badge-medium'>Medium Risk</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span class='badge-low'>Low Risk</span>", unsafe_allow_html=True)

        st.write("**Risk Reason:**", reason)
        st.write("**Plain-language Explanation:**")
        st.write(explanation)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
