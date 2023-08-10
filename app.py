import streamlit as st

x = st.slider("AAA", 0, 100, 27)
st.download_button("AAAAA", "BBBBBBBBBB" * x)
