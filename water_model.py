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

# Budget Accounting Variables
total_spent = b_cons + b_storm + b_gw_recharge + b_storage + b_rec + b_desal
remaining_budget = 10000 - total_spent

if remaining_budget < 0:
    st.error(f"🚨 **BUDGET OVERRUN:** Overspent by **${abs(remaining_budget):,} Million**! Rebalance sliders to total $10,000M or less.")
else:
    st.markdown(f"""
    <div class='budget-tracker'>
        <strong>Capital Budget Status:</strong> Spent <strong>${total_spent:,} Million</strong> of $10,000 Million | 
        Unallocated Reserve: <strong>${remaining_budget:,} Million</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🌡️ Step 2: Set Future Environmental Stressors")

s_col1, s_col2 = st.columns(2)
with s_col1:
    target_year = st.slider("Target Planning Horizon Year", 2026, 2060, 2040, step=1)
    pop_growth = st.slider("Annual Population Growth Rate (%)", -0.5, 1.5, 0.4, step=0.1)
with s_col2:
    warming = st.slider("Climate Warming / Temp Rise (°C)", 0.0, 4.0, 1.5, step=0.1)
    precip_var = st.slider("Precipitation Variability / Chaos (%)", 0, 100, 30, step=5)

# ENGINE LOGIC & CAPACITY CALCULATIONS
afy_saved_cons = (b_cons * 1000000) / 2500
afy_yield_storm = (b_storm * 1000000) / 10000
afy_cap_gw_recharge = (b_gw_recharge * 1000000) / 6000
afy_cap_storage = (b_storage * 1000000) / 12000
afy_yield_rec = (b_rec * 1000000) / 16000
afy_yield_desal = (b_desal * 1000000) / 25000

# Fixed Baseline
baseline_gross_demand = 1550000 * ((1 + (pop_growth / 100)) ** (target_year - 2026))
fixed_gw_baseline = 511500  # Adjudicated natural groundwater yield

# Net Demand after Conservation
net_demand_needed = max(0, baseline_gross_demand - afy_saved_cons)

# Stress Event Losses & Buffer Boosts
imp_climate_loss = min(0.65, (warming * 0.12) + (precip_var / 100.0) * 0.35)
storm_climate_loss = min(0.75, (warming * 0.05) + (precip_var / 100.0) * 0.55)
gw_climate_loss = min(0.30, (warming * 0.05) + (precip_var / 100.0) * 0.15)

storm_buffer_boost = min(afy_yield_storm * 0.4, afy_cap_storage * (precip_var / 100.0))
actual_storm = max(0, (afy_yield_storm * (1 - storm_climate_loss)) + storm_buffer_boost)

gw_bank_drawdown = min(afy_cap_gw_recharge * 0.5, net_demand_needed * 0.15)
actual_gw = max(0, (fixed_gw_baseline * (1 - gw_climate_loss)) + gw_bank_drawdown)

actual_rec = afy_yield_rec
actual_desal = afy_yield_desal

# Imported Water Gap Calculation
target_imported_needed = max(0, net_demand_needed - (fixed_gw_baseline + afy_yield_storm + afy_cap_gw_recharge*0.2 + afy_yield_rec + afy_yield_desal))
actual_imported_available = target_imported_needed * (1 - imp_climate_loss)

# Totals & Resiliency
total_water_delivered = actual_gw + actual_storm + actual_rec + actual_desal + actual_imported_available
supply_coverage_ratio = total_water_delivered / net_demand_needed if net_demand_needed > 0 else 1.0

resiliency_score = int(supply_coverage_ratio * 100)
imported_share = (target_imported_needed / net_demand_needed) if net_demand_needed > 0 else 0
if imported_share > 0.40:
    resiliency_score -= int((imported_share - 0.40) * 45)
resiliency_score = max(min(resiliency_score, 100), 5)

# Financial Calculations: Annual Operations & Maintenance (O&M) Cost
annual_om_cost = (target_imported_needed * 1250 * (1 + warming * 0.02)) + \
                 (fixed_gw_baseline * 850) + \
                 (afy_yield_rec * 1850) + \
                 (afy_yield_storm * 900) + \
                 (afy_cap_gw_recharge * 650) + \
                 (afy_cap_storage * 500) + \
                 (afy_yield_desal * 3000) + \
                 (afy_saved_cons * 350)

avg_cost_per_af = annual_om_cost / baseline_gross_demand if baseline_gross_demand > 0 else 0

# Environmental Score (0 - 100, Lower is Better)
env_score = int(((target_imported_needed * 0.7) + (fixed_gw_baseline * 0.3) + (afy_yield_rec * 0.2) + \
                 (afy_yield_storm * 0.1) + (afy_cap_storage * 0.4) + (afy_yield_desal * 1.0)) / (net_demand_needed + 1) * 100)
env_score = max(min(env_score, 100), 5)

# SIDEBAR OUTPUTS PANEL
with st.sidebar:
    st.markdown("## 📊 Portfolio Evaluation")
    
    if remaining_budget < 0:
        st.error("⚠️ **Fix Overbudget Status on main screen to view scores.**")
    else:
        # Financial Profile Card
        st.markdown(f"""
        <div class='metric-card' style='border-top-color: #3498db;'>
            <div class='metric-title'>💰 Financial Summary</div>
            <div class='metric-value'>${total_spent / 1000:.2f}B CapEx</div>
            <div class='metric-caption'>
                Upfront Capital Spent: <strong>${total_spent:,} Million</strong><br>
                Annual System O&M Cost: <strong>${annual_om_cost / 1e9:.2f} Billion/yr</strong><br>
                Avg Unit Cost: <strong>${int(avg_cost_per_af):,}/AF</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Resiliency Card
        res_color = "🟢 High Resiliency" if resiliency_score >= 85 else ("🟡 Moderate Risk" if resiliency_score >= 65 else "🔴 Severe Supply Crisis")
        st.markdown(f"""
        <div class='metric-card' style='border-top-color: #2ecc71;'>
            <div class='metric-title'>🛡️ Portfolio Resiliency Score</div>
            <div class='metric-value'>{resiliency_score} / 100</div>
            <div class='metric-caption'>Status: <strong>{res_color}</strong><br>
            Meets <strong>{int(supply_coverage_ratio * 100)}%</strong> of net demand under drought stress.</div>
        </div>
        """, unsafe_allow_html=True)

        # Imported Reliance Card
        st.markdown(f"""
        <div class='metric-card' style='border-top-color: #e67e22;'>
            <div class='metric-title'>🌊 Imported Water Reliance</div>
            <div class='metric-value'>{int(target_imported_needed):,} AFY</div>
            <div class='metric-caption'>Baseline was 930,000 AFY.<br>
            Accounted for <strong>{int(imported_share * 100)}%</strong> of total portfolio.</div>
        </div>
        """, unsafe_allow_html=True)

        # Environmental Score Card
        eco_color = "🟢 Low Impact" if env_score <= 35 else ("🟡 Moderate Strain" if env_score <= 60 else "🔴 High Ecological Strain")
        st.markdown(f"""
        <div class='metric-card' style='border-top-color: #e74c3c;'>
            <div class='metric-title'>🌿 Environmental Impact Score</div>
            <div class='metric-value'>{env_score} / 100</div>
            <div class='metric-caption'>Status: <strong>{eco_color}</strong> (Lower is healthier).</div>
        </div>
        """, unsafe_allow_html=True)

        # Donut Chart
        st.markdown("### Planned Supply & Storage Mix")
        fig = fgo.Figure(data=[fgo.Pie(
            labels=['Imported Gap', 'Groundwater', 'Stormwater', 'GW Recharge Bank', 'Reservoir Buffer', 'Recycling', 'Ocean Desal'], 
            values=[target_imported_needed, fixed_gw_baseline, afy_yield_storm, afy_cap_gw_recharge, afy_cap_storage, afy_yield_rec, afy_yield_desal], 
            hole=.35,
            marker=dict(colors=['#e67e22', '#2ecc71', '#f1c40f', '#27ae60', '#34495e', '#9b59b6', '#e74c3c'])
        )])
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=210, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        # Physical Alerts
        st.markdown("### ⚠️ Physical Engineering Alerts")
        if b_storm > 2500: st.warning("**Stormwater Ceiling:** LA lacks urban land area to capture this much runoff.")
        if b_gw_recharge > 3000: st.warning("**Aquifer Capacity Limit:** Recharge exceeds local basin storage limits.")
        if b_storage > 2500: st.warning("**Topographic Barrier:** High land cost and environmental permitting hurdles for dams/reservoirs.")
        if b_rec > 6000: st.warning("**Effluent Limitation:** Capital exceeds total municipal wastewater baseline.")
        if b_desal > 2000: st.warning("**Regulatory Wall:** High energy grid load & Coastal Commission blocking.")
        if b_cons > 3000: st.warning("**Public Fatigue:** High conservation targets risk compliance failure.")
