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
    .guide-box {
        background-color: #f1f9fe;
        border-left: 4px solid #3498db;
        padding: 10px 14px;
        border-radius: 4px;
        font-size: 13px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚰 LA County Water Resilience Challenge ($10B Capital Budget)")
st.markdown("### **Mission Objective:** Replace LA's 930,000 AFY Imported Water Gap using Local Infrastructure & Storage.")
st.markdown("---")

# MAIN CONTROLS PANEL
st.markdown("## 💰 Step 1: Allocate Your $10 Billion Capital Budget")

c1, c2 = st.columns(2)

with c1:
    st.markdown("#### **Demand Reduction & Local Yield**")
    
    # 1. CONSERVATION
    b_cons = st.slider("1. Demand Reduction & Conservation ($M)", 0, 10000, 0, step=250, 
                       help="CapEx: $2,500/AF | O&M: $350/AF | $1B = 400,000 AFY saved")
    with st.expander("ℹ️ Strategy Guide: Conservation & Efficiency"):
        st.markdown("""
        * **The Mechanism:** Turf replacement rebates, smart irrigation controllers, low-flow fixture retrofits, and municipal leak repair.
        * **Cost Profile:** **Lowest CapEx ($2,500/AF).** Extremely cost-effective way to stretch existing water supplies.
        * **Resilience & Reliability:** High immediate impact, but subject to **public compliance fatigue** and diminishing returns over time.
        * **Eco & Social Impact:** **Best Environmental Score.** Zero carbon footprint; preserves river ecosystems by leaving water in natural streams.
        """)

    # 2. STORMWATER CAPTURE
    b_storm = st.slider("2. Stormwater Capture & Green Infra ($M)", 0, 10000, 0, step=250, 
                        help="CapEx: $10,000/AF | O&M: $900/AF | $1B = 100,000 AFY yield")
    with st.expander("ℹ️ Strategy Guide: Stormwater Capture"):
        st.markdown("""
        * **The Mechanism:** Spreading grounds, permeable pavements, bioswales, and urban park basins to catch rainwater runoff.
        * **Cost Profile:** **Moderate CapEx ($10,000/AF).** Requires significant urban land acquisition and engineering.
        * **Resilience & Reliability:** **Weather-Dependent.** Yield spikes during wet years/atmospheric rivers, but collapses during multi-year droughts.
        * **Eco & Social Impact:** Excellent local co-benefits (urban green spaces, reduced street flooding, filtered ocean runoff).
        """)

    # 3. GROUNDWATER RECHARGE
    b_gw_recharge = st.slider("3. Groundwater Recharge & Aquifer Banking ($M)", 0, 10000, 0, step=250, 
                             help="CapEx: $6,000/AF | O&M: $650/AF | $1B = 166,666 AFY storage capacity")
    with st.expander("ℹ️ Strategy Guide: Aquifer Banking & Recharge"):
        st.markdown("""
        * **The Mechanism:** Deep injection wells and spreading basins that store excess winter surface water deep underground.
        * **Cost Profile:** **Low-to-Moderate CapEx ($6,000/AF).** Utilizes natural subterranean geology as free storage reservoirs.
        * **Resilience & Reliability:** **Critical Drought Buffer.** Allows LA to draw down banked reserves when surface supplies dry up.
        * **Eco & Social Impact:** Prevents basin overdraft, land subsidence (sinking ground), and seawater intrusion into coastal freshwater aquifers.
        """)

with c2:
    st.markdown("#### **Storage Expansion & Tech Yield**")

    # 4. SURFACE STORAGE
    b_storage = st.slider("4. Surface Storage Expansion / Reservoirs ($M)", 0, 10000, 0, step=250, 
                          help="CapEx: $12,000/AF | O&M: $500/AF | $1B = 83,333 AF atmospheric river buffer")
    with st.expander("ℹ️ Strategy Guide: Reservoirs & Surface Storage"):
        st.markdown("""
        * **The Mechanism:** Expanding dam heights, building off-stream reservoirs, and upgrading flood-control basins.
        * **Cost Profile:** **High CapEx ($12,000/AF).** High civil engineering and land purchase costs.
        * **Resilience & Reliability:** Essential for capturing flash-flood surges from intense **Atmospheric Rivers** caused by climate change.
        * **Eco & Social Impact:** High environmental impact due to land flooding, ecosystem disruption, and heavy state permitting barriers.
        """)

    # 5. WATER RECYCLING
    b_rec = st.slider("5. Water Recycling / Potable Reuse ($M)", 0, 10000, 0, step=250, 
                      help="CapEx: $16,000/AF | O&M: $1,850/AF | $1B = 62,500 AFY drought-proof yield")
    with st.expander("ℹ️ Strategy Guide: Advanced Water Recycling"):
        st.markdown("""
        * **The Mechanism:** Microfiltration, reverse osmosis, and UV purification of municipal wastewater (e.g., *Pure Water Los Angeles*).
        * **Cost Profile:** **High CapEx ($16,000/AF)** and **High O&M ($1,850/AF)** due to complex treatment infrastructure and energy requirements.
        * **Resilience & Reliability:** **100% Drought-Proof.** Municipal wastewater flows 24/7/365 regardless of weather or precipitation.
        * **Eco & Social Impact:** Prevents treated wastewater effluent from polluting coastal bays; highly accepted by modern water planners.
        """)

    # 6. OCEAN DESALINATION
    b_desal = st.slider("6. Ocean Desalination Buildout ($M)", 0, 10000, 0, step=250, 
                        help="CapEx: $25,000/AF | O&M: $3,000/AF | $1B = 40,000 AFY yield")
    with st.expander("ℹ️ Strategy Guide: Ocean Desalination"):
        st.markdown("""
        * **The Mechanism:** Coastal plants forcing seawater through high-pressure membranes to remove salt and minerals.
        * **Cost Profile:** **Highest CapEx ($25,000/AF)** and **Highest O&M ($3,000/AF)**. Extremely expensive to build and run.
        * **Resilience & Reliability:** **Unlimited Local Yield.** Completely independent of weather, snowpack, or rainfall patterns.
        * **Eco & Social Impact:** **Worst Environmental Score.** Heavy grid energy demand, greenhouse gas footprint, marine life intake impacts, and toxic brine discharge.
        """)

# Budget Accounting
total_spent
