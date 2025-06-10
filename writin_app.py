app.py

import streamlit as st import random import time

-------- App Config --------

st.set_page_config( page_title="Motivation for Writers & Readers", page_icon="📖", layout="centered" )

-------- Custom Styling --------

st.markdown(""" <style> body { background-image: url('https://images.unsplash.com/photo-1529148482759-b35b25c52f3c?auto=format&fit=crop&w=1400&q=80'); background-size: cover; background-attachment: fixed; } .main { background-color: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 15px; } h1, h2 { color: #6A1B9A; font-family: 'Georgia', serif; } .quote-box { background-color: #f3e5f5; padding: 20px; border-radius: 10px; margin-top: 20px; color: #4A148C; font-style: italic; font-size: 18px; } </style> """, unsafe_allow_html=True)

-------- Initialize Session State --------

if "username" not in st.session_state: st.session_state.username = "" if "role" not in st.session_state: st.session_state.role = "" if "shown_quotes" not in st.session_state: st.session_state.shown_quotes = [] if "last_quote" not in st.session_state: st.session_state.last_quote = ""

-------- Quotes --------

writer_quotes = [ "Write drunk, edit sober. – Ernest Hemingway", "The first draft is just you telling yourself the story. – Terry Pratchett", "Start writing, no matter what. – Louis L’Amour", "The scariest moment is always just before you start. – Stephen King", "You can make anything by writing. – C.S. Lewis", "A word after a word after a word is power. – Margaret Atwood", "You fail only if you stop writing. – Ray Bradbury", "Keep writing. Keep going. No matter what. – Unknown", "The desire to write grows with writing. – Erasmus", "Don't get it right, just get it written. – James Thurber", "Almost all good writing begins with terrible first efforts. – Anne Lamott", "Writing is an exploration. – E. L. Doctorow", "I write to discover what I know. – Flannery O’Connor", "We are all apprentices in a craft where no one ever becomes a master. – Ernest Hemingway", "Write what disturbs you. – Natalie Goldberg", "If you wait for inspiration, you're not a writer. – Dan Poynter", "You learn to write by writing. – William Zinsser", "There is no greater agony than bearing an untold story inside you. – Maya Angelou", "A professional writer is an amateur who didn’t quit. – Richard Bach", "Don’t tell me the moon is shining; show me the glint of light on broken glass. – Anton Chekhov", "Writing is a socially acceptable form of schizophrenia. – E.L. Doctorow", "Writing well means never having to say, ‘I guess you had to be there.’ – Jef Mallett", "Being a writer means developing a thick skin. – Unknown", "To survive, you must tell stories. – Umberto Eco", "The art of writing is the art of discovering what you believe. – Gustave Flaubert" ]

reader_quotes = [ "A reader lives a thousand lives before he dies. – George R.R. Martin", "Reading is essential for those who seek to rise above the ordinary. – Jim Rohn", "Until I feared I would lose it, I never loved to read. – Harper Lee", "There is no friend as loyal as a book. – Ernest Hemingway", "Books are a uniquely portable magic. – Stephen King", "Reading gives us someplace to go when we have to stay where we are. – Mason Cooley", "Today a reader, tomorrow a leader. – Margaret Fuller", "The reading of all good books is like a conversation with the finest minds. – Descartes", "Reading is to the mind what exercise is to the body. – Joseph Addison", "Books wash away from the soul the dust of everyday life. – Unknown", "If you only read the books that everyone else is reading, you can only think what everyone else is thinking. – Haruki Murakami", "You can never get a cup of tea large enough or a book long enough to suit me. – C.S. Lewis", "Once you learn to read, you will be forever free. – Frederick Douglass", "We read to know we are not alone. – William Nicholson", "Some books leave us free and some books make us free. – Ralph Waldo Emerson", "Reading one book is like eating one potato chip. – Diane Duane", "The world belongs to those who read. – Rick Holland", "Books are mirrors: you only see in them what you already have inside you. – Carlos Ruiz Zafón", "A good book is an event in my life. – Stendhal", "So many books, so little time. – Frank Zappa", "I do believe something very magical can happen when you read a book. – J.K. Rowling", "Reading brings us unknown friends. – Honoré de Balzac", "Book lovers never go to bed alone. – Unknown", "Books are the quietest and most constant of friends. – Charles W. Eliot", "If you love books enough, books will love you back. – Jo Walton" ]

-------- Login Interface --------

if not st.session_state.username: st.title("📖 Welcome to the Motivation App") username = st.text_input("What should we call you?") role = st.radio("Are you a...", ["Writer", "Reader"]) if st.button("Enter") and username: st.session_state.username = username st.session_state.role = role st.rerun() else: st.title(f"Welcome, {st.session_state.username} ✨")

# Determine quote list
quotes = writer_quotes if st.session_state.role == "Writer" else reader_quotes

# Auto-refresh countdown
countdown = st.empty()
seconds = 10
for i in range(seconds, 0, -1):
    countdown.markdown(f"⏳ New quote in **{i}** seconds...")
    time.sleep(1)

# Random new quote
quote = random.choice(quotes)
while quote == st.session_state.last_quote:
    quote = random.choice(quotes)
st.session_state.last_quote = quote

# Typing effect
quote_box = st.empty()
typed = ""
for char in quote:
    typed += char
    time.sleep(0.03)
    quote_box.markdown(f"<div class='quote-box'>{typed}</div>", unsafe_allow_html=True)

# Save to history
if quote not in st.session_state.shown_quotes:
    st.session_state.shown_quotes.append(quote)

# Copy to clipboard
st.code(quote, language="")

# Quote history
if st.session_state.shown_quotes:
    with st.expander("📝 Quote History"):
        for past in st.session_state.shown_quotes[::-1]:
            st.markdown(f"• *{past}*")

st.markdown("---")
st.markdown("<small style='color:#b39ddb'>Enjoy your journey with words ✍️</small>", unsafe_allow_html=True)

if st.button("🔁 Start Over"):
    st.session_state.username = ""
    st.session_state.role = ""
    st.session_state.shown_quotes = []
    st.session_state.last_quote = ""
    st.rerun()

