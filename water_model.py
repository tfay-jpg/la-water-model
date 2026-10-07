import streamlit as st
import plotly.graph_objects as fgo

# Page Setup
st.set_page_config(layout="wide", page_title="LA County Water Portfolio Simulator ($10B Challenge)")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: white;
        padding: 16px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border-top: 5px solid #3498db;
    }
    .metric-title { font-size: 12px; color: #7f8c8d; font-weight: bold; text-transform: uppercase; }
    .metric-value { font-size: 24px; color: #2c3e50; font-weight: bold; margin: 4px 0; }
    .metric-caption { font-size: 11px; color: #7f8c8d; }
    .budget-tracker {
        background-color: #eaf2f8;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #2980b9;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚰 LA County Water Resilience Challenge ($10B Capital Budget)")
st.markdown("### **Mission Objective:** Replace LA's 930,000 AFY Imported Water Gap using Local Infrastructure & Demand Management.")
st.markdown("---")

# MAIN CONTROLS PANEL
st.markdown("## 💰 Step 1: Allocate Your $10 Billion Capital Budget")

c1, c2 = st.columns(2)

with c1:
    st.markdown("#### **Demand Reduction & Catchment**")
    
    # 1. INDOOR CONSERVATION
    b_cons_in = st.slider("1. Water Conservation & Demand Reduction (Indoors) ($M)", 0, 10000, 0, step=250, 
                          help="CapEx: $2,000/AF | O&M: $250/AF | $1B = 500,000 AFY saved")
    with st.expander("ℹ️ Strategy Guide: Indoor Water Conservation"):
        st.markdown("* **The Mechanism:** High-efficiency toilet retrofits, low-flow showerheads, commercial appliance standards, and municipal leak detection.\n* **Cost Profile:** **Lowest CapEx ($2,000/AF).** High volume savings per dollar spent.\n* **Resilience & Reliability:** Constant year-round savings; unaffected by weather or climate shocks.\n* **Eco & Social Impact:** Excellent environmental score; reduces indoor wastewater volume sent to treatment plants.")

    # 2. LANDSCAPE TRANSFORMATION
    b_cons_out = st.slider("2. Landscape Transformation / Outdoor Water Reduction ($M)", 0, 10000, 0, step=250, 
                           help="CapEx: $3,000/AF | O&M: $400/AF | $1B = 333,333 AFY saved")
    with st.expander("ℹ️ Strategy Guide: Outdoor Landscape Transformation"):
        st.markdown("* **The Mechanism:** Turf replacement rebates (grass removal), native/drought-tolerant landscaping, and smart irrigation controllers.\n* **Cost Profile:** **Low CapEx ($3,000/AF).** Turf removal is more labor-intensive than indoor appliance retrofits.\n* **Resilience & Reliability:** Significantly reduces outdoor summer peak water demand.\n* **Eco & Social Impact:** Supports local biodiversity, reduces urban heat island effect, and prevents pesticide runoff into storm drains.")

    # 3. STORMWATER CAPTURE
    b_storm = st.slider("3. Stormwater Capture & Passive Infiltration ($M)", 0, 10000, 0, step=250, 
                        help="CapEx: $10,000/AF | O&M: $900/AF | $1B = 100,000 AFY yield")
    with st.expander("ℹ️ Strategy Guide: Stormwater Capture & Spreading Grounds"):
        st.markdown("* **The Mechanism:** Spreading grounds, unpaved basins, bioswales, and permeable street pavement that catch urban runoff and let it passively soak into shallow aquifers.\n* **Cost Profile:** **Moderate CapEx ($10,000/AF).** Requires urban land acquisition and surface drainage structures.\n* **Resilience & Reliability:** **Weather-Dependent.** Captures massive storm surges during wet years, but yield drops during multi-year droughts.\n* **Eco & Social Impact:** High local co-benefits (urban park greening, street flood control, reduced ocean runoff pollution).")

    # 4. UPSTREAM RESERVOIRS & STORAGE
    b_storage = st.slider("4. Increasing Upstream Rainwater Storage / Reservoirs ($M)", 0, 10000, 0, step=250, 
                          help="CapEx: $12,000/AF | O&M: $500/AF | $1B = 83,333 AF atmospheric river runoff capture")
    with st.expander("ℹ️ Strategy Guide: Upstream Reservoirs & Storage"):
        st.markdown("* **The Mechanism:** Expanding dam heights, foothill catch basins, and off-stream reservoirs to capture direct mountain watershed precipitation and snowmelt.\n* **Cost Profile:** **High CapEx ($12,000/AF).** High civil engineering and land purchase costs in canyon corridors.\n* **Resilience & Reliability:** **Direct Local Yield & Buffer.** Essential for capturing flash-flood surges from intense atmospheric rivers.\n* **Eco & Social Impact:** High environmental impact due to canyon flooding, sediment trapping, and river ecosystem disruption.")

with c2:
    st.markdown("#### **Tech Yield & Subterranean Banking**")

    # 5. AQUIFER BANKING & DEEP WELL INJECTION
    b_gw_recharge = st.slider("5. Aquifer Banking & Deep Well Injection ($M)", 0, 10000, 0, step=250, 
                             help="CapEx: $6,000/AF | O&M: $650/AF | $1B = 166,666 AFY storage capacity")
    with st.expander("ℹ️ Strategy Guide: Aquifer Banking & Deep Well Injection"):
        st.markdown("* **The Mechanism:** High-pressure injection wells that actively pump treated surface water deep underground into subterranean aquifers for long-term storage and drought recovery.\n* **Cost Profile:** **Moderate CapEx ($6,000/AF).** Uses natural geology as a free subterranean storage tank.\n* **Resilience & Reliability:** **Critical Drought Buffer.** Acts as a multi-year 'water bank account' to pump out when surface water dries up.\n* **Eco & Social Impact:** Prevents basin overdraft, land sinking (subsidence), and ocean saltwater intrusion into coastal freshwater wells.")

    # 6. WATER RECYCLING FOR POTABLE REUSE
    b_rec = st.slider("6. Wastewater Recycling for Potable Reuse ($M)", 0, 10000, 0,
