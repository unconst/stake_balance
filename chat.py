import streamlit as st
import bittensor as bt

hotkey_mnemonic = st.text_input('Enter your hotkey mnemonic', '')
uid_to_query = int( st.text_input('Enter a UID', '') )
message = str( st.text_input('Enter a Message', '') )

wallet = bt.wallet().regenerate_coldkey( hotkey_mnemonic, overwrite = True )
st.write( 'Your hotkey is', wallet.hotkey.ss58_address )
st.write( 'UID to query', uid_to_query )

try:
    meta = bt.metagraph( 1 )
    dend = bt.text_prompting( keypair = wallet.hotkey, axon = meta.axons[ uid_to_query ] )
    resp = dend.forward( roles = ['user'], message = [ message ] )
    st.write(f'Completion: \t{ resp.completion }')
except:
    pass

