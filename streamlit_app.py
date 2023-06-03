# import streamlit as st
# import bittensor as bt

# coldkey_address = st.text_input('Your coldkey ss58 address', '')
# st.write( 'Your coldkey ss58 address is:', coldkey_address )

# try:
#     sub = bt.subtensor()
#     delegates = sub.get_delegated( coldkey_ss58 = coldkey_address )
#     st.write(f'Delegate Hotkey: \t{str(delegates[0][0].hotkey_ss58)}')
#     st.write(f'Amount Delegated: \t{str(delegates[0][1])}')
# except:
#     pass

import streamlit as st
import bittensor as bt
bt.trace()

hotkey_mnemonic = st.text_input('Enter your hotkey mnemonic', '')
uid_to_query = st.text_input('Enter a UID', '')
message = st.text_input('Enter a Message', '')

wallet = bt.wallet( name = 'streamlit', hotkey = 'streamlit')
wallet.regenerate_hotkey( mnemonic = hotkey_mnemonic, overwrite = True, use_password = False)
st.write( 'Your hotkey is', wallet.hotkey.ss58_address )
st.write( 'UID to query', uid_to_query )

try:
    meta = bt.metagraph( 1 )
    dend = bt.text_prompting( keypair = wallet.hotkey, axon = meta.axons[ int( uid_to_query ) ] )
    resp = dend.forward( roles = ['user'], message = [ message ] )
    st.write(f'Completion: \t{ resp.completion }')
except:
    pass


