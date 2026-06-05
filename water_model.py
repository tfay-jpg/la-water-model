import streamlit as st
import plotly.graph_objects as fgo

# Page Setup
st.set_page_config(layout="wide", page_title="LA County Water Portfolio Simulator")

# Custom CSS for modern dashboard styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-top: 5px solid #3498db;
    }
    .metric-title { font-size: 14px; color: #7f8c8d; font-weight: bold; text-transform: uppercase; }
    .metric-value { font-size: 28px; color: #2c3e50; font-weight: bold; margin: 5px 0; }
    .metric-caption { font-size: 12px; color: #95a5a6; }
    </style>
""", unsafe_allow_html=True)

st.title("🚰 LA County Water Management Portfolio Simulator")
st.markdown("### Interactive Policy & Climate Stress Dashboard")
st.markdown("---")

# Main Page: Controls & Sliders
st.markdown("## ⚙️ Simulation Controls")

# Section 1: Demand Side
st.markdown("<div style='background-color: #ebf5fb; padding: 15px; border-radius: 8px; margin-bottom: 15px;'><strong>Step 1: Reduce Systemic Demand</strong></div>", unsafe_allow_html=True)
conservation = st.slider("Water Conservation / Demand Reduction Target (% reduction from baseline)", 0, 30, 5)

# Section 2: Supply Side
st.markdown("<div style='background-color: #e8f8f5; padding: 15px; border-radius: 8px; margin-bottom: 15px;'><strong>Step 2: Allocate Remaining Physical Supply (Must total 100%)</strong></div>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    imp_pct = st.number_input("Imported Water (%)", 0, 100, 60, step=1)
    rec_pct = st.number_input("Water Recycling (%)", 0, 100, 5, step=1)
    desal_pct = st.number_input("Ocean Desalination (%)", 0, 100, 0, step=1)
with c2:
    gw_pct = st.number_input("Groundwater (%)", 0, 100, 33, step=1)
    storm_pct = st.number_input("Stormwater Capture (%)", 0, 100, 2, step=1)

total_portfolio_pct = imp_pct + gw_pct + rec_pct + storm_pct + desal_pct
st.markdown(f"**Current Total Allocation Check:** `{total_portfolio_pct}% / 100%`")

# Section 3: Stressors
st.markdown("<div style='background-color: #fef9e7; padding: 15px; border-radius: 8px; margin-bottom: 15px;'><strong>Step 3: Apply Future Environmental Stressors</strong></div>", unsafe_allow_html=True)
target_year = st.slider("Target Planning Horizon Year", 2026, 2060, 2026, step=1)
pop_growth = st.slider("Annual Population Growth Rate (%)", -0.5, 1.5, 0.4, step=0.1)
warming = st.slider("Climate Warming / Temp Rise (°C)", 0.0, 4.0, 0.0, step=0.1)
precip_var = st.slider("Precipitation Variability / Chaos (%)", 0, 100, 0, step=5)

# ENGINE LOGIC
years_out = target_year - 2026
baseline_gross_demand = 1550000 * ((1 + (pop_growth / 100)) ** years_out)
net_reduced_demand = baseline_gross_demand * (1 - (conservation / 100))

# Calculate target intended volumes
imp_target = net_reduced_demand * (imp_pct / 100)
gw_target = net_reduced_demand * (gw_pct / 100)
rec_target = net_reduced_demand * (rec_pct / 100)
storm_target = net_reduced_demand * (storm_pct / 100)
desal_target = net_reduced_demand * (desal_pct / 100)
cons_vol = baseline_gross_demand - net_reduced_demand

# CLIMATE SHOCK IMPACT: Calculate actual available water during the stress test
# Weather-dependent sources take a hit based on warming and precipitation chaos
imp_climate_loss = min(0.60, (warming * 0.10) + (precip_var / 100.0) * 0.30)
storm_climate_loss = min(0.70, (warming * 0.05) + (precip_var / 100.0) * 0.50)
gw_climate_loss = min(0.25, (warming * 0.05) + (precip_var / 100.0) * 0.10)

actual_imp_supply = imp_target * (1 - imp_climate_loss)
actual_storm_supply = storm_target * (1 - storm_climate_loss)
actual_gw_supply = gw_target * (1 - gw_climate_loss)
actual_rec_supply = rec_target      # 100% resilient
actual_desal_supply = desal_target  # 100% resilient

total_actual_supply = actual_imp_supply + actual_storm_supply + actual_gw_supply + actual_rec_supply + actual_desal_supply

# FINANCIAL CALCULATIONS (Based on planned portfolio infrastructure)
escalated_imp_cost = 1250 * (1 + (warming * 0.02))
total_cost = (imp_target * escalated_imp_cost) + (gw_target * 850) + (rec_target * 1850) + (storm_target * 900) + (desal_target * 3000) + (cons_vol * 350)
avg_cost_per_af = total_cost / baseline_gross_demand

# RESILIENCY SCORE CALCULATIONS (0 - 100)
# Measures how close the actual available water comes to covering 100% of the population's net demand
if net_reduced_demand > 0:
    supply_coverage_ratio = total_actual_supply / net_reduced_demand
    resiliency_score = int(supply_coverage_ratio * 100)
else:
    resiliency_score = 100

# Penalty for over-reliance on a single vulnerable source (Lack of structural diversity)
if imp_pct > 50:
    resiliency_score -= int((imp_pct - 50) * 0.4)

resiliency_score = max(min(resiliency_score, 100), 5)

# ENVIRONMENTAL COST SCORE (0 - 100, Lower is better)
env_score = max(min(int((imp_pct * 0.8) + (gw_pct * 0.4) + (rec_pct * 0.2) + (storm_pct * 0.1) + (desal_pct * 1.0)), 100), 5)

# SIDEBAR OUTPUTS (Locks metrics to the side panel so they stay frozen as students scroll)
with st.sidebar:
    st.markdown("## 📊 Evaluation & Metrics")
    
    if total_portfolio_pct != 100:
        st.error(f"⚠️ **PORTFOLIO MISMATCH:** Your allocation totals {total_portfolio_pct}%. Please adjust the numbers until they equal exactly 100% to view performance scores.")
    else:
        # Cost Card
        st.markdown(f"""<div class='metric-card'><div class='metric-title'>💰 Total Financial Profile</div><div class='metric-value'>${total_cost / 1e9:.2f} Billion / yr</div><div class='metric-caption'>Average Cost: ${int(avg_cost_per_af)} per acre-foot (Baseline: ~$1,020)</div></div>""", unsafe_allow_html=True)
        
        # Resiliency Card
        res_color = "🟢 High Resiliency" if resiliency_score >= 90 else ("🟡 Moderate Risk" if resiliency_score >= 70 else "🔴 Severe Supply Failure")
        st.markdown(f"""<div class='metric-card' style='border-top-color: #2ecc71;'><div class='metric-title'>🛡️ Portfolio Resiliency Index</div><div class='metric-value'>{resiliency_score} / 100</div><div class='metric-caption'>Status: <strong>{res_color}</strong><br>The mix meets {int(min(supply_coverage_ratio, 1.0)*100)}% of population needs under this climate stressor event.</div></div>""", unsafe_allow_html=True)
        
        # Eco Card
        eco_color = "🟢 Low Strain" if env_score <= 40 else ("🟡 Moderate Strain" if env_score <= 65 else "🔴 Severe Degradation")
        st.markdown(f"""<div class='metric-card' style='border-top-color: #e74c3c;'><div class='metric-title'>🌿 Environmental Impact Score</div><div class='metric-value'>{env_score} / 100</div><div class='metric-caption'>Status: <strong>{eco_color}</strong> (Lower scores indicate healthier local ecosystems).</div></div>""", unsafe_allow_html=True)
        
        # Donut Chart
        st.markdown("### Resource Balance Allocation")
        fig = fgo.Figure(data=[fgo.Pie(labels=['Imported Water', 'Groundwater', 'Water Recycling', 'Stormwater Capture', 'Ocean Desalination'], 
                                       values=[imp_target, gw_target, rec_target, storm_target, desal_target], hole=.4,
                                       marker=dict(colors=['#3498db', '#2ecc71', '#9b59b6', '#f1c40f', '#e74c3c']))])
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=220, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        # Warnings Area
        st.markdown("### ⚠️ Infrastructure Flags")
        if gw_pct > 35: st.warning("**Groundwater Overdraft:** Exceeds basin safe yield.")
        if storm_pct > 15: st.warning("**Hydrologic Ceiling:** LA's climate cannot physically generate this much catchable runoff.")
        if rec_pct > 45: st.warning("**Effluent Limitation:** Allocation exceeds available total wastewater baseline.")
        if desal_pct > 10: st.warning("**Regulatory Wall:** Scale faces grid power constraints and Coastal Commission blocking.")
        if gw_pct <= 35 and storm_pct <= 15 and rec_pct <= 45 and desal_pct <= 10:
            st.success("All allocated strategies fall within realistic engineering thresholds for LA County.")
