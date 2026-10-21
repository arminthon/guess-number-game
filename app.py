import streamlit as st
import random
st.title("Hadse Adad")

if "target" not in st.session_state:
    st.session_state.target = random.randint(1,100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0


guess = st.number_input("hadse khodeto benevis (beyne 1 ta 100) : ", min_value=1, max_value=100, step=1 )

if st.button("بررسی حدس"):
    st.session_state.attempts += 1

    if guess == st.session_state.target:
        st.success(f"🎉 آفرین! بعد از {st.session_state.attempts} بار تلاش، درست حدس زدی! عدد همون {st.session_state.target} بود.")
    elif guess < st.session_state.target:
        st.warning("📈 برو بالاتر! عدد من بزرگ‌تره.")
    else:
        st.warning("📉 بیا پایین‌تر! عدد من کوچک‌تره.") 
  
if st.button("شروع مجدد / بازی جدید 🔄"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()