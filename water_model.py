import streamlit as st
import plotly.graph_objects as fgo

# Page Setup
st.set_page_config(layout="wide", page_title="LA County Water Portfolio Simulator ($10B Challenge)")

# Custom CSS for modern dashboard styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: white;
        padding: 18px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-top: 5px solid #3498db;
    }
    .metric-title { font-size: 13px; color: #7f8c8d; font-weight: bold; text-transform: uppercase; }
    .metric-value { font-size: 26px; color: #2c3e50; font-weight: bold; margin: 4px 0; }
    .metric-caption { font-size: 12px; color: #7f8c8d; }
    .budget-tracker {
        background-color: #eaf2f8;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #2980b9;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚰 LA County Water Resilience Challenge ($10B Capital Budget)")
st.markdown("### **Mission Objective:** Eliminate LA's 930,000 AFY Imported Water Reliance before Climate Shocks hit.")
st.markdown("---")

# MAIN CONTROLS PANEL
st.markdown("## 💰 Step 1: Allocate Your $10 Billion Capital Budget")

col1, col2 = st.columns(2)

with col1:
    b_cons = st.slider("Conservation & Efficiency ($ Millions)", 0, 10000, 1500, step=250, 
                       help="$2,500 per AF saved | $1B buys 400,000 AFY saved")
    b_storm = st.slider("Stormwater Capture Infrastructure ($ Millions)", 0, 10000, 1500, step=250, 
                        help="$10,000 per AF capacity | $1B buys 100,000 AFY yield")

with col2:
    b_rec = st.slider("Water Recycling / Potable Reuse ($ Millions)", 0, 10000, 4000, step=250, 
                      help="$16,000 per AF capacity | $1B buys 62,500 AFY yield")
    b_desal = st.slider("Ocean Desalination Buildout ($ Millions)", 0, 10000, 1000, step=250, 
                        help="$25,000 per AF capacity | $1B buys 40,000 AFY yield")

# Budget Accounting
total_spent = b_cons + b_storm + b_rec + b_desal
remaining_budget = 10000 - total_spent

if remaining_budget < 0:
    st.error(f"🚨 **BUDGET OVERRUN:** You have overspent by **${abs(remaining_budget):,} Million**! Rebalance your sliders to total $10,000M or less.")
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
# Convert Capital Spending ($ Millions) into Physical Yield (AFY) using Unit Costs
afy_saved_cons = (b_cons * 1000000) / 2500
afy_yield_storm = (b_storm * 1000000) / 10000
afy_yield_rec = (b_rec * 1000000) / 16000
afy_yield_desal = (b_desal * 1000000) / 25000

# Fixed Baseline Values
baseline_gross_demand = 1550000 * ((1 + (pop_growth / 100)) ** (target_year - 2026))
fixed_gw_baseline = 511500  # Local Adjudicated Groundwater Yield

# Net Demand after Conservation
net_demand_needed = max(0, baseline_gross_demand - afy_saved_cons)

# Climate Shock Reductions on Yield during Stress Events
imp_climate_loss = min(0.65, (warming * 0.12) + (precip_var / 100.0) * 0.35)
storm_climate_loss = min(0.75, (warming * 0.05) + (precip_var / 100.0) * 0.55)
gw_climate_loss = min(0.30, (warming * 0.05) + (precip_var / 100.0) * 0.15)

# Actual Available Local Supplies under Stress
actual_gw = fixed_gw_baseline * (1 - gw_climate_loss)
actual_storm = afy_yield_storm * (1 - storm_climate_loss)
actual_rec = afy_yield_rec      # 100% Drought-Proof
actual_desal = afy_yield_desal  # 100% Drought-Proof

total_local_supply_actual = actual_gw + actual_storm + actual_rec + actual_desal

# Imported Water Gap Calculation (Imported Water fills whatever is left over)
target_imported_needed = max(0, net_demand_needed - (fixed_gw_baseline + afy_yield_storm + afy_yield_rec + afy_yield_desal))
actual_imported_available = target_imported_needed * (1 - imp_climate_loss)

# Deficit & Resiliency Metrics
total_water_delivered = total_local_supply_actual + actual_imported_available
supply_coverage_ratio = total_water_delivered / net_demand_needed if net_demand_needed > 0 else 1.0

# Resiliency Score Calculation (0 - 100)
resiliency_score = int(supply_coverage_ratio * 100)
# Penalty for heavy reliance on imported water
imported_share = (target_imported_needed / net_demand_needed) if net_demand_needed > 0 else 0
if imported_share > 0.40:
    resiliency_score -= int((imported_share - 0.40) * 50)
resiliency_score = max(min(resiliency_score, 100), 5)

# Total Annual O&M Cost ($)
annual_om_cost = (target_imported_needed * 1250 * (1 + warming * 0.02)) + (fixed_gw_baseline * 850) + \
                 (afy_yield_rec * 1850) + (afy_yield_storm * 900) + (afy_yield_desal * 3000) + (afy_saved_cons * 350)
avg_cost_per_af = annual_om_cost / baseline_gross_demand if baseline_gross_demand > 0 else 0

# Environmental Score (0 - 100, Lower is Better)
env_score = int(((target_imported_needed * 0.7) + (fixed_gw_baseline * 0.3) + (afy_yield_rec * 0.2) + \
                 (afy_yield_storm * 0.1) + (afy_yield_desal * 1.0)) / (net_demand_needed + 1) * 100)
env_score = max(min(env_score, 100), 5)

# SIDEBAR OUTPUTS PANEL (LOCKED TO SIDEBAR)
with st.sidebar:
    st.markdown("## 📊 Portfolio Evaluation")
    
    if remaining_budget < 0:
        st.error("⚠️ **Fix Overbudget Status on main screen to view scores.**")
    else:
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

        # Donut Chart of Supply Mix
        st.markdown("### Planned Supply Mix (AFY)")
        fig = fgo.Figure(data=[fgo.Pie(
            labels=['Imported Gap', 'Groundwater', 'New Recycling', 'New Stormwater', 'Ocean Desal'], 
            values=[target_imported_needed, fixed_gw_baseline, afy_yield_rec, afy_yield_storm, afy_yield_desal], 
            hole=.4,
            marker=dict(colors=['#e67e22', '#2ecc71', '#9b59b6', '#f1c40f', '#e74c3c'])
        )])
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=200, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        # Physical Alerts
        st.markdown("### ⚠️ Physical Engineering Alerts")
        if b_storm > 2500: st.warning("**Stormwater Ceiling:** LA lacks physical land area to capture this much runoff.")
        if b_rec > 7000: st.warning("**Effluent Limitation:** Capital exceeds total municipal wastewater available to recycle.")
        if b_desal > 2000: st.warning("**Regulatory Wall:** High energy use & Coastal Commission opposition likely.")
        if b_cons > 3000: st.warning("**Public Fatigue:** High conservation targets risk public compliance failure.")
