import streamlit as st
import bittensor as bt

coldkey_address = st.text_input('Your coldkey ss58 address', '0x')
st.write( 'Your coldkey ss58 address is:', coldkey_address )

sub = bt.subtensor()
delegates = sub.get_delegated( coldkey_ss58 = coldkey_address )
st.write( 'Delegates', str(coldkey_address) )

