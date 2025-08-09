import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

# --- Load Lottie Animation Safely ---
def load_lottiefile(filepath: str):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return None

# --- Page Config ---
st.set_page_config(page_title="Love for Arshin 💖", layout="centered")

# --- Background + Music ---
page_bg_music = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1495567720989-cebdbdd97913?auto=format&fit=crop&w=1650&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

h1, h2, h3, h4, h5 {
    color: #fff0f5;
    text-align: center;
}

.audio-player {
    position: fixed;
    bottom: 10px;
    left: 10px;
    z-index: 100;
}
</style>

<div class="audio-player">
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
</div>
"""
st.markdown(page_bg_music, unsafe_allow_html=True)

# --- Her Name ---
her_name = "Arshin Bagwan"
st.markdown(f"## 💗 This one’s just for you, **{her_name}** 💗")

# --- Upload Her Photo ---
her_image = st.sidebar.file_uploader("Upload a beautiful photo of Arshin 👸", type=["jpg", "jpeg", "png"])
if her_image:
    st.image(her_image, width=200, caption=f"For you, {her_name} 😍")

# --- Flirty Slide Data ---
slides = [
    "Slide 1: Hey, are you made of copper and tellurium? Because you’re Cu-Te 😉",
    "Slide 2: If kisses were snowflakes, I'd send you a blizzard 💋",
    "Slide 3: I must be a snowflake, because I’ve fallen for you ❄️",
    "Slide 4: Is your name Google? Because you’ve got everything I’ve been searching for 💻❤️",
    "Slide 5: Life without you is like a broken pencil... pointless ✏️",
    "Slide 6: Just one thing left to say...",
]

# --- Slide State ---
if 'step' not in st.session_state:
    st.session_state.step = 0

st.title("💖 Romantic Slide Show 💖")
st.subheader(slides[st.session_state.step])

# --- Next Button ---
if st.button("Next 💌"):
    if st.session_state.step < len(slides) - 1:
        st.session_state.step += 1
        st.experimental_rerun()
    else:
        st.session_state.show_final = True

# --- Final Scene ---
if st.session_state.get("show_final", False):
    st.title("🌸 I LOVE YOU 🌸")
    st.markdown("### You make my heart blossom, just like these cherry trees...")

    lottie_animation = load_lottiefile("cherry_blossom.json")
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, loop=True, quality="high", height=400)
    else:
        st.info("Cherry blossom animation not found, but love is still in the air! 🌸")

    st.markdown(f"## 💘 Forever Yours, {her_name} 💘")

    # --- Video Section ---
    video_path = "WhatsApp Video 2025-08-09 at 5.22.22 PM.mp4"  # Your uploaded file name
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning("Video file not found. Please check the path.")

    st.markdown(f"### With all my heart, {her_name} 💝")

    # WhatsApp Share Link
    message = f"Hey {her_name}, I made something special for you! 💕 Click here to open it!"
    wa_link = f"https://wa.me/?text={message.replace(' ', '%20')}"
    st.markdown("### 💌 Share this with Arshin on WhatsApp:")
    st.markdown(f"[📲 Send to WhatsApp]({wa_link})")
