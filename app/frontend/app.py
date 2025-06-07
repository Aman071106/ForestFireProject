import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(
    page_title="🔮 Mystical Forest Fire Oracle",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced magical CSS with animations and gradients
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .main-header {
        font-family: 'Cinzel', serif;
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #ff6b35, #f7931e, #ffd700, #ff6b35);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 107, 53, 0.5);
        margin-bottom: 1rem;
    }
    
    @keyframes shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #fff;
        margin-bottom: 2rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        font-family: 'Inter', sans-serif;
    }
    
    .mystical-orb {
        width: 150px;
        height: 150px;
        margin: 0 auto 2rem;
        background: radial-gradient(circle, #ffd700, #ff6b35, #8b0000);
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite, rotate 10s linear infinite;
        box-shadow: 0 0 50px rgba(255, 215, 0, 0.7), inset 0 0 50px rgba(255, 107, 53, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .mystical-orb::before {
        content: '🔮';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 4rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes float {
        0%, 100% { transform: translate(-50%, -50%); }
        50% { transform: translate(-50%, -60%); }
    }
    
    .enchanted-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 25px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 0 30px rgba(255, 215, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .enchanted-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent 30%, rgba(255, 215, 0, 0.1) 50%, transparent 70%);
        animation: sparkle 4s linear infinite;
        pointer-events: none;
    }
    
    @keyframes sparkle {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .magical-input {
        background: linear-gradient(135deg, #f8f9ff 0%, #e6f3ff 100%);
        border: 2px solid transparent;
        border-radius: 15px;
        padding: 1rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .magical-input::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .magical-input:hover::before {
        left: 100%;
    }
    
    .crystal-metric {
        background: linear-gradient(135deg, #ffffff 0%, #f0f8ff 100%);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1), inset 0 0 20px rgba(255, 215, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .crystal-metric:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2), inset 0 0 30px rgba(255, 215, 0, 0.2);
    }
    
    .prediction-orb {
        background: radial-gradient(circle at center, #667eea 0%, #764ba2 100%);
        border-radius: 30px;
        padding: 3rem;
        text-align: center;
        color: white;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3), 0 0 50px rgba(102, 126, 234, 0.5);
        animation: mystical-glow 3s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    .prediction-orb::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent 0deg, rgba(255, 255, 255, 0.1) 60deg, transparent 120deg);
        animation: cosmic-rotate 6s linear infinite;
        pointer-events: none;
    }
    
    @keyframes mystical-glow {
        0%, 100% { box-shadow: 0 20px 60px rgba(0,0,0,0.3), 0 0 50px rgba(102, 126, 234, 0.5); }
        50% { box-shadow: 0 25px 80px rgba(0,0,0,0.4), 0 0 80px rgba(102, 126, 234, 0.8); }
    }
    
    @keyframes cosmic-rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .enchanted-button {
        background: linear-gradient(45deg, #ff6b35, #f7931e, #ffd700);
        background-size: 200% 200%;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 3rem;
        font-size: 1.2rem;
        font-weight: 600;
        font-family: 'Cinzel', serif;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.4), inset 0 0 20px rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        animation: button-glow 2s ease-in-out infinite;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        overflow: hidden;
    }
    
    .enchanted-button::before {
        content: '✨';
        position: absolute;
        left: -30px;
        animation: sparkle-move 2s linear infinite;
    }
    
    @keyframes button-glow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes sparkle-move {
        0% { left: -30px; opacity: 0; }
        50% { opacity: 1; }
        100% { left: calc(100% + 30px); opacity: 0; }
    }
    
    .enchanted-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 40px rgba(255, 107, 53, 0.6), inset 0 0 30px rgba(255, 255, 255, 0.3);
    }
    
    .risk-indicator {
        position: relative;
        width: 200px;
        height: 200px;
        margin: 0 auto;
    }
    
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: radial-gradient(circle, #ffd700, #ff6b35);
        border-radius: 50%;
        animation: float-particle 15s linear infinite;
        opacity: 0.7;
    }
    
    @keyframes float-particle {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.7;
        }
        90% {
            opacity: 0.7;
        }
        100% {
            transform: translateY(-100px) rotate(360deg);
            opacity: 0;
        }
    }
    
    .section-title {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        text-align: center;
        margin-bottom: 1.5rem;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #ff6b35, #ffd700, #ff6b35);
        border-radius: 2px;
    }
    
    .weather-icon-large {
        font-size: 3rem;
        animation: bounce 2s ease-in-out infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
</style>
""", unsafe_allow_html=True)

# Floating particles background
st.markdown("""
<div class="floating-particles">
    <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
    <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
    <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
    <div class="particle" style="left: 40%; animation-delay: 1s;"></div>
    <div class="particle" style="left: 50%; animation-delay: 3s;"></div>
    <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
    <div class="particle" style="left: 70%; animation-delay: 2.5s;"></div>
    <div class="particle" style="left: 80%; animation-delay: 4.5s;"></div>
    <div class="particle" style="left: 90%; animation-delay: 1.5s;"></div>
</div>
""", unsafe_allow_html=True)

# Magical Header
st.markdown('<div class="mystical-orb"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🔮 Mystical Forest Fire Oracle</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Unveil the Secrets of Fire Weather through Ancient Wisdom & Modern Magic ✨</p>', unsafe_allow_html=True)

# Create magical gauge chart
def create_magical_gauge(value, title, max_val=100, color_scale=None):
    if color_scale is None:
        color_scale = ["#00ff00", "#ffff00", "#ff6600", "#ff0000"]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title, 'font': {'size': 24, 'family': 'Cinzel'}},
        gauge = {
            'axis': {'range': [None, max_val], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#ff6b35", 'thickness': 0.3},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "#ffd700",
            'steps': [
                {'range': [0, max_val*0.3], 'color': 'rgba(0,255,0,0.3)'},
                {'range': [max_val*0.3, max_val*0.6], 'color': 'rgba(255,255,0,0.3)'},
                {'range': [max_val*0.6, max_val*0.8], 'color': 'rgba(255,102,0,0.3)'},
                {'range': [max_val*0.8, max_val], 'color': 'rgba(255,0,0,0.3)'}
            ],
            'threshold': {
                'line': {'color': "#ffd700", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white", 'family': 'Inter'},
        height=300
    )
    
    return fig

# Create radar chart for weather conditions
def create_weather_radar(temp, humidity, wind, rain, ffmc, dmc, isi):
    categories = ['Temperature', 'Humidity', 'Wind Speed', 'Rainfall', 'FFMC', 'DMC', 'ISI']
    
    # Normalize values to 0-100 scale for visualization
    values = [
        (temp + 50) / 110 * 100,  # Temp range -50 to +60
        humidity,  # Already 0-100
        min(wind / 200 * 100, 100),  # Wind up to 200 km/h
        min(rain / 100 * 100, 100),  # Rain up to 100mm for visualization
        ffmc,  # Already 0-100
        min(dmc / 500 * 100, 100),  # DMC up to 500
        min(isi / 50 * 100, 100)   # ISI up to 50
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Current Conditions',
        line_color='#ff6b35',
        fillcolor='rgba(255, 107, 53, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color='white'),
                gridcolor='rgba(255,255,255,0.3)'
            ),
            angularaxis=dict(
                tickfont=dict(color='white', size=12),
                gridcolor='rgba(255,255,255,0.3)'
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white", 'family': 'Inter'},
        height=400
    )
    
    return fig

# Enchanted input section
with st.container():
    st.markdown('<h2 class="section-title">🌟 Mystical Parameters</h2>', unsafe_allow_html=True)
    
    # Time Magic
    st.markdown("#### ⏰ Temporal Coordinates")
    time_col1, time_col2 = st.columns(2)
    with time_col1:
        day = st.selectbox("🌅 Day of Prophecy", options=list(range(1, 32)), key="day")
    with time_col2:
        month = st.selectbox("🌙 Moon Cycle", options=list(range(1, 13)), key="month")
    
    # Weather Enchantments
    st.markdown("#### 🌈 Elemental Forces")
    weather_col1, weather_col2 = st.columns(2)
    with weather_col1:
        temperature = st.number_input("🌡️ Fire's Breath (°C)", min_value=-50.0, max_value=60.0, value=25.0, step=0.1)
        rh = st.number_input("💧 Water's Whisper (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    with weather_col2:
        ws = st.number_input("💨 Wind's Dance (km/h)", min_value=0.0, max_value=200.0, value=10.0, step=0.1)
        rain = st.number_input("🌧️ Sky's Tears (mm)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)
    
    # Mystical Indices
    st.markdown("#### 🔮 Ancient Wisdom Codes")
    indices_col1, indices_col2 = st.columns(2)
    with indices_col1:
        ffmc = st.number_input("🍃 Fine Fuel Mysticism", min_value=0.0, max_value=100.0, value=85.0, step=0.1)
        dmc = st.number_input("🌿 Duff Moisture Divination", min_value=0.0, max_value=500.0, value=25.0, step=0.1)
    with indices_col2:
        isi = st.number_input("⚡ Initial Spread Incantation", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
    
    # Sacred Lands
    st.markdown("#### 🗺️ Sacred Realm")
    region = st.selectbox("🏔️ Mystical Territory", options=["Bejaia", "Sidi Bel-abbes"], key="region")
    region_code = 0 if region == "Bejaia" else 1
    
    st.markdown('</div>', unsafe_allow_html=True)

# Magical visualization section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<h3 class="section-title">🌟 Elemental Resonance</h3>', unsafe_allow_html=True)
    
    # Weather radar chart
    radar_fig = create_weather_radar(temperature, rh, ws, rain, ffmc, dmc, isi)
    st.plotly_chart(radar_fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Inject custom CSS style
    st.markdown("""
        <style>
        .enchanted-container {
            padding: 10px;
            border-radius: 12px;
        }
        .crystal-metric {
            background-color: #e0f0ff;  /* Light blue */
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .weather-icon-large {
            font-size: 40px;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h3 class="section-title">💎 Crystal Metrics</h3>', unsafe_allow_html=True)
    
    metric_col1, metric_col2 = st.columns(2)
    
    with metric_col1:
        st.markdown(f'''
        <div class="crystal-metric">
            <div class="weather-icon-large">🌡️</div>
            <h3 style="color:#000000;">{temperature}°C</h3>
            <p>Fire's Breath</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f'''
        <div class="crystal-metric">
            <div class="weather-icon-large">💨</div>
            <h3 style="color:#000000;">{ws} km/h</h3>
            <p>Wind's Power</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f'''
        <div class="crystal-metric">
            <div class="weather-icon-large">💧</div>
            <h3 style="color:#000000;">{rh}%</h3>
            <p>Water's Balance</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f'''
        <div class="crystal-metric">
            <div class="weather-icon-large">🌧️</div>
            <h3 style="color:#000000;">{rain} mm</h3> 
            <p>Sky's Gift</p>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Magical prediction function
def predict_with_magic():
    entries = ['day', 'month', 'Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Region']
    input_values = [day, month, temperature, rh, ws, rain, ffmc, dmc, isi, region_code]
    
    # Create magical loading animation
    with st.spinner('🔮 Consulting the Ancient Spirits...'):
        # Create a progress bar with magical elements
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        import time
        magical_phases = [
            "🌟 Gathering cosmic energies...",
            "🔥 Channeling fire spirits...",
            "🌪️ Reading wind patterns...",
            "💧 Consulting water omens...",
            "🌿 Interpreting forest whispers...",
            "🔮 Unveiling the prophecy..."
        ]
        
        for i, phase in enumerate(magical_phases):
            status_text.text(phase)
            progress_bar.progress((i + 1) / len(magical_phases))
            time.sleep(0.5)
        
        try:
            input_json = json.dumps({label: value for label, value in zip(entries, input_values)})
            
            url = 'http://127.0.0.1:5000/predict-fwi'
            headers = {'Content-Type': 'application/json'}
            
            response = requests.post(url, data=input_json, headers=headers, timeout=10)
            
            progress_bar.empty()
            status_text.empty()
            
            if response.status_code == 200:
                ans = response.json()
                
                if 'fwi' in ans:
                    fwi_value = ans['fwi']
                    
                    # Determine magical risk level
                    if fwi_value < 5:
                        risk_level = "Peaceful Harmony"
                        risk_color = "#00ff00"
                        risk_emoji = "🌿"
                        risk_desc = "The forest spirits are at peace. Fire magic is weak."
                    elif fwi_value < 15:
                        risk_level = "Gentle Stirring"
                        risk_color = "#ffaa00"
                        risk_emoji = "⚠️"
                        risk_desc = "The elements show signs of unrest. Caution is advised."
                    elif fwi_value < 30:
                        risk_level = "Fierce Awakening"
                        risk_color = "#ff4400"
                        risk_emoji = "🔥"
                        risk_desc = "Fire spirits are rousing! Great caution required!"
                    else:
                        risk_level = "Infernal Rage"
                        risk_color = "#aa0000"
                        risk_emoji = "🌋"
                        risk_desc = "The fire demons are unleashed! Extreme danger!"
                    
                    # Create magical result display
                    st.markdown(f'''
                    <div class="prediction-orb">
                        <h2 style="font-family: 'Cinzel', serif; margin-bottom: 1rem;">🔮 The Oracle Speaks</h2>
                        <div style="font-size: 5rem; margin: 1rem 0; animation: pulse 2s infinite;">{fwi_value:.1f}</div>
                        <h3 style="color: {risk_color}; font-family: 'Cinzel', serif; margin: 1rem 0;">{risk_emoji} {risk_level}</h3>
                        <p style="font-size: 1.1rem; opacity: 0.9; margin-top: 1rem;">{risk_desc}</p>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Create magical gauge
                    gauge_fig = create_magical_gauge(fwi_value, "Fire Weather Index", 50)
                    st.plotly_chart(gauge_fig, use_container_width=True)
                    
                    # Magical advice
                    st.markdown('<div class="enchanted-container">', unsafe_allow_html=True)
                    st.markdown('<h3 class="section-title">🧙‍♂️ Ancient Wisdom</h3>', unsafe_allow_html=True)
                    
                    if fwi_value < 5:
                        st.success("🌿 The forest is protected by benevolent spirits. Perfect time for peaceful activities in nature.")
                    elif fwi_value < 15:
                        st.warning("🔔 The elemental balance shifts. Stay vigilant and respect the forest's mood.")
                    elif fwi_value < 30:
                        st.error("⚡ Fire magic grows strong! Avoid all spark-creating activities. The spirits are restless.")
                    else:
                        st.error("🚨 BEWARE! The fire demons have awakened! All fire-related activities are FORBIDDEN!")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                else:
                    st.error(f"❌ The spirits are silent: {ans.get('error', 'Unknown mystical disturbance')}")
                    
            else:
                st.error(f"❌ The crystal ball is clouded: Server Error {response.status_code}")
                
        except requests.exceptions.Timeout:
            st.error("⏳ The spirits take their time... The prophecy request has timed out.")
        except requests.exceptions.ConnectionError:
            st.error("🔌 The mystical connection is severed. Ensure the Oracle server runs on localhost:5000")
        except Exception as e:
            st.error(f"❌ A dark magic interferes: {str(e)}")

# Enchanted prediction button
st.markdown("---")
button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
with button_col2:
    if st.button("🔮 Consult the Oracle", key="magical_predict"):
        predict_with_magic()

# Magical footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #fff; margin: 3rem 0; font-family: 'Cinzel', serif;">
    <h3>🌟 ✨ 🔮 Mystical Forest Fire Oracle 🔮 ✨ 🌟</h3>
    <p style="opacity: 0.8; font-family: 'Inter', sans-serif;">
        Powered by Ancient Wisdom & Modern Sorcery<br>
        <small>Based on the Sacred Algerian Forest Fire Scrolls</small>
    </p>
    <div style="margin-top: 2rem; font-size: 2rem;">
        🌲 🔥 🌟 ⚡ 💫 🌙 ✨
    </div>
</div>
""", unsafe_allow_html=True)