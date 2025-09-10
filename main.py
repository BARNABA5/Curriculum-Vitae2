import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Barnabas CV", page_icon="📄", layout="wide")

# --- CUSTOM CSS ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0d1b2a; /* Dark blue */
    color: white;
    font-family: Arial, sans-serif;
    padding: 20px;
}
h1, h2, h3 {
    color: #00b4d8; /* Light blue */
}
a {
    color: #90e0ef !important;
    text-decoration: none;
}
a:hover {
    color: #caf0f8 !important;
}
button {
    border-radius: 12px !important;
}
.profile-pic {
    border-radius: 50%;
    width: 150px;
    margin-bottom: 10px;
}
.box {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- HEADER WITH PROFILE PHOTO ---
col1, col2 = st.columns([1, 4])

with col1:
    image = Image.open("Philip.jpg")  # Make sure this is in the same folder
    st.image(image, caption="Barney Phil", width=150, output_format="auto")

with col2:
    st.title("📄 My Curriculum vitae")
    st.write("Welcome to my personal CV website! 🚀")

# --- ABOUT ME SECTION ---
st.markdown('<div class="box">', unsafe_allow_html=True)
st.subheader("👋 About Me")
st.write("""
Hi, I’m **Barnabas Phil** — a passionate developer from Kenya 🇰🇪.  
I love building creative apps, solving technical problems, and helping people through technology.  
My dream is to create impactful solutions that make everyday life easier and more meaningful.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- COMING SOON BOX ---
st.markdown('<div class="box">', unsafe_allow_html=True)
st.subheader("⏳ Coming Soon")
st.write("""
Exciting new projects and updates are on the way!  
Stay tuned as activities are currently ongoing. 🔧✨
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS ---
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("🛠 Projects on GitHub")
st.write("Here are some of my highlighted projects still in progress:")

projects = {
    "Youth System (YSC)": " https://barnaba5.github.io/YSC-DESK/",
    "SmartFix  Barney 2.0": "https://barnaba5.github.io/SmartFix-Barney2.0/",
    "Sanctuary Hub": "https://barnaba5.github.io/sanctuaryhub/",
    "SmartFix Studio": "https://barnaba5.github.io/SmartFix-Art/",
}

for name, link in projects.items():
    st.markdown(f"- 🔗 [{name}]({link})")
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACT ME ---
st.markdown('<div class="box">', unsafe_allow_html=True)
st.header("📧 Contact Me")
st.write("You can reach me directly via email:")
st.markdown("[📩 Send me an Email](shivayilubarnabas@gmail.com)", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- ANIMATION AT THE BOTTOM ---
st.header("⚡ SmartFix Barney Animation")
st.write("A sneak peek of my SmartFix Barney Project 👇")

# Example Lottie Animation
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")  # Replace with SmartFix Barney styled animation
st_lottie(lottie_animation, height=300, key="smartfix")

# --- FOOTER ---
st.markdown("---")
st.write("⚡ Built with [Streamlit](https://streamlit.io/) by Barnabas Shivayilu")
st.write("All rights reserved Barney Enterprises. © 2024")
