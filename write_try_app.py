import streamlit as st
import random
import time

# Page setup
st.set_page_config(page_title="Writer's Motivational App", layout="centered")

# Background and style
page_bg_img = """
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1588776814546-ec7fbcf7b1fa");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Georgia', serif;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

h1, h2, h3, h4, h5 {
    color: #6A0DAD;
}

.stButton>button {
    background-color: #a36fa36fbdbd;
    color: black;
    border-radius: 10px;
    padding: 10px;
    font-weight: bold;
}

.quote-box {
    background-color: #f5f0fa;
    border-left: 5px solid #6A0DAD;
    padding: 20px;
    border-radius: 10px;
    font-size: 1.2em;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Quote lists
writer_quotes = [
    "You don’t have to be great to start, but you have to start to be great.",
    "Write what should not be forgotten.",
    "You can make anything by writing.",
    "The scariest moment is always just before you start.",
    "A word after a word after a word is power.",
    "Don’t get it right, just get it written.",
    "There is no greater agony than bearing an untold story inside you.",
    "Start writing, no matter what. The water does not flow until the faucet is turned on.",
    "Almost all good writing begins with terrible first efforts.",
    "If you wait for inspiration to write you’re not a writer, you’re a waiter.",
    "Write with the door closed, rewrite with the door open.",
    "Your first draft won’t be perfect—and that’s okay.",
    "Be brave enough to be bad at something new.",
    "Writers live twice.",
    "Writing is its own reward.",
    "The role of a writer is not to say what we all can say, but what we are unable to say.",
    "Writing is an exploration. You start from nothing and learn as you go.",
    "Inspiration exists, but it has to find you working.",
    "Don’t tell me the moon is shining; show me the glint of light on broken glass.",
    "The only way to do great work is to love what you write.",
    "Write drunk, edit sober.",
    "Write what disturbs you, what you fear, what you have not been willing to speak about.",
    "A professional writer is an amateur who didn’t quit.",
    "When in doubt, write it out.",
    "Let your soul spill onto the page."
]

reader_quotes = [
    "A reader lives a thousand lives before he dies.",
    "Reading is essential for those who seek to rise above the ordinary.",
    "Books are a uniquely portable magic.",
    "Until I feared I would lose it, I never loved to read. One does not love breathing.",
    "Reading gives us someplace to go when we have to stay where we are.",
    "A room without books is like a body without a soul.",
    "There is no friend as loyal as a book.",
    "Reading is dreaming with open eyes.",
    "Books are the plane, and the train, and the road. They are the destination and the journey.",
    "The man who does not read has no advantage over the man who cannot read.",
    "Reading is a discount ticket to everywhere.",
    "Books are mirrors: you only see in them what you already have inside you.",
    "The more that you read, the more things you will know.",
    "Today a reader, tomorrow a leader.",
    "You can find magic wherever you look. Sit back and relax, all you need is a book.",
    "Once you learn to read, you will be forever free.",
    "Reading is the gateway skill that makes all other learning possible.",
    "Books wash away from the soul the dust of everyday life.",
    "I have always imagined that Paradise will be a kind of library.",
    "So many books, so little time.",
    "It is what you read when you don’t have to that determines what you will be when you can’t help it.",
    "Books are lighthouses erected in the great sea of time.",
    "Reading brings us unknown friends.",
    "Books are not made for furniture, but there is nothing else that so beautifully furnishes a room.",
    "Read. Reflect. Repeat."
]

# Session state
if "username" not in st.session_state:
    st.session_state.username = ""
if "category" not in st.session_state:
    st.session_state.category = ""
if "history" not in st.session_state:
    st.session_state.history = []

# User input section
if st.session_state.username == "":
    st.title("📚 Writer’s & Reader’s Motivation App")
    username = st.text_input("✨ What should we call you?")
    if username:
        st.session_state.username = username
        st.rerun()
else:
    st.markdown(f"### Welcome, **{st.session_state.username}**! 😊")
    
    if st.session_state.category == "":
        st.subheader("Are you a writer or a reader?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✍️ Writer"):
                st.session_state.category = "writer"
                st.rerun()
        with col2:
            if st.button("📖 Reader"):
                st.session_state.category = "reader"
                st.rerun()
    else:
        # Display a random quote
        quotes = writer_quotes if st.session_state.category == "writer" else reader_quotes
        selected_quote = random.choice(quotes)

        if selected_quote not in st.session_state.history:
            st.session_state.history.append(selected_quote)

        st.markdown(f"<div class='quote-box'>💬 <em>{selected_quote}</em></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🔁 Refresh Quote"):
                st.rerun()

        with col2:
            if st.button("📋 Copy to Clipboard"):
                st.code(selected_quote)

        with col3:
            if st.button("🔄 Start Over"):
                st.session_state.username = ""
                st.session_state.category = ""
                st.session_state.history = []
                st.rerun()

        st.subheader("📝 Your Quote History")
        for idx, q in enumerate(reversed(st.session_state.history[-5:]), 1):
            st.markdown(f"**{idx}.** {q}")
