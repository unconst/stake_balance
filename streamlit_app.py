import streamlit as st
import bittensor as bt

coldkey_address = st.text_input('Your coldkey ss58 address', '')
st.write( 'Your coldkey ss58 address is:', coldkey_address )

try:
    sub = bt.subtensor()
    delegates = sub.get_delegated( coldkey_ss58 = coldkey_address )
    st.write(f'Delegate Hotkey: \t{str(delegates[0][0].hotkey_ss58)}')
    st.write(f'Amount Delegated: \t{str(delegates[0][1])}')
except:
    pass

