import streamlit as st

coldkey_address = st.text_input('Your coldkey ss58 address', '0x')
st.write( 'Your coldkey ss58 address is:', coldkey_address )