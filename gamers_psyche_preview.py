import streamlit as st
from PIL import Image

# Simulate Logo & Banner
st.set_page_config(page_title="Gamers Psyche", layout="wide")

# ----- Sidebar -----
with st.sidebar:
    st.title("Categories")
    st.markdown("""
    - 🎮 Game Reviews  
    - 🧠 Game Psychology  
    - 🔥 Trending News  
    """)
    st.markdown("---")
    st.write("**Subscribe for Latest Updates**")
    st.text_input("Enter your email")
    st.button("Subscribe")

# ----- Header -----
st.markdown("""
<style>
.title {
    font-size:48px; 
    color:#00f0ff;
    font-family: 'Trebuchet MS', sans-serif;
    text-shadow: 2px 2px 5px #000;
}
.tagline {
    font-size:20px; 
    color:#ccc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Gamers Psyche</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Unraveling the Mind Behind the Game</div>", unsafe_allow_html=True)

st.markdown("---")

# ----- Main Content -----
st.header("Latest Posts")

# Simulated Post Grid
cols = st.columns(3)
with cols[0]:
    st.image("https://via.placeholder.com/300x180?text=GTA+VI", caption="GTA VI Release Insights")
    st.write("A deep dive into the much-awaited Grand Theft Auto VI, with comparisons to GTA V.")

with cols[1]:
    st.image("https://via.placeholder.com/300x180?text=Gamer+Rage", caption="Understanding Gamer Rage")
    st.write("Exploring why players experience rage, and how psychology connects to gaming behavior.")

with cols[2]:
    st.image("https://via.placeholder.com/300x180?text=Elden+Ring", caption="Elden Ring Progress")
    st.write("Progress update and experiences from the vast world of Elden Ring, including DLC insights.")

# Footer
st.markdown("---")
st.write("© 2025 Gamers Psyche | Designed for Gamers & Psychology Enthusiasts")
