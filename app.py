import streamlit as st

st.title("DOWNLOAD BUTTON _SELF AND DOWNLOAD ATTRIBUTE DEMO")

x = st.slider("AAA", 0, 100, 27)
st.download_button("AAAAA", "BBBBBBBBBBAAABB" * x)
