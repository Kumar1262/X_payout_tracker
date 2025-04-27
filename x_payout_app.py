import streamlit as st
import datetime
import time
import random

# Set page config
st.set_page_config(
    page_title="X Payout Tracker",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'message_shown' not in st.session_state:
    st.session_state.message_shown = False
    st.session_state.selected_message = None

# Light theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f9fa;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown(
    "<h1 style='text-align: center; color: #1DA1F2; font-size: 48px; margin-bottom: 30px;'>Have I been paid by 𝕏?</h1>",
    unsafe_allow_html=True
)

# Target date
target_date = datetime.datetime(2025, 3, 29, 12, 0, 0)

# Function to calculate time difference
def get_time_diff():
    now = datetime.datetime.now()
    diff = abs(target_date - now)
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    return days, hours, minutes, seconds

# Create placeholder for the counter
counter_placeholder = st.empty()

# Funny messages
funny_messages = [
    "Ask again tomorrow 🤔",
    "Highly unlikely 😅",
    "LMAO no 🤣",
    "Dream on 😴",
    "Payment pending... forever. ⏳",
    "Congratulations! You received $0.00! 🎉",
    "Keep waiting... the suspense is real! 🕰️",
    "Maybe next century? 🦕",
    "Still loading your payment... please stand by. ⏳",
    "You get nothing! Good day, sir! 🚫",
    "Your patience is impressive. Your payout? Not so much. 🧘‍♂️",
    "If you squint, you might see your payment. 👀",
    "Try unplugging and plugging your bank account back in. 🔌💸",
    "Your payment is in another castle. 🏰",
    "404 Payment Not Found 🖥️",
    "You miss 100% of the payouts you don't get. 🏒",
    "Manifesting money... still manifesting... ✨💸",
    "The check is in the (e)mail. 📬",
    "You have been selected for a random act of... nothing. 🎲",
    "Your payout is like Bigfoot: often talked about, never seen. 🦶",
    "If only wishes were dollars... 🌠"
]

# Button styling for light theme
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #1DA1F2;
        color: white;
        font-size: 24px;
        padding: 20px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        margin: 20px 0;
    }
    div.stButton > button:hover {
        background-color: #1a91da;
    }
    </style>
""", unsafe_allow_html=True)

# Check payment button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("CHECK IF YOU GOT PAID!", use_container_width=True):
        st.session_state.message_shown = True
        st.session_state.selected_message = random.choice(funny_messages)

# Display message if button was clicked
if st.session_state.message_shown and st.session_state.selected_message:
    st.markdown(
        f"<div style='text-align: center; font-size: 36px; padding: 20px; margin: 20px 0; background-color: #e3f2fd; color: #1565c0; border-radius: 10px;'>{st.session_state.selected_message}</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    "<div style='text-align: center; color: #657786; margin-top: 20px; font-style: italic;'>Keep waiting... maybe someday! 🤞</div>",
    unsafe_allow_html=True
)

# Social follow text
st.markdown(
    """
    <div style='text-align: center; color: #888; margin-top: 10px; font-size: 22px;'>
        Don't forget to hit follow button for <b style='color: #1DA1F2;'>@codersthings</b>
    </div>
    """,
    unsafe_allow_html=True
)

# Update counter continuously
while True:
    days, hours, minutes, seconds = get_time_diff()
    counter_placeholder.markdown(
        f"<div style='text-align: center; font-size: 80px; font-family: monospace; color: #222; white-space: nowrap;'>"
        f"{days}d {hours}h {minutes}m {seconds}s"
        f"</div>",
        unsafe_allow_html=True
    )
    time.sleep(1) 