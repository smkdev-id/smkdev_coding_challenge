import logging
from pprint import pprint
import streamlit as st
from backend.service.notion import query_base_info
from backend.static import TECH_STACK, CHALLENGE_TYPES
from streamlit_pills import pills

st.set_page_config(
    page_title = "Active Challenges",
    page_icon = '🔥'
)

with st.sidebar:
    challenges_type = pills(
        "Challenge Type",
        list(CHALLENGE_TYPES.keys()),
        list(CHALLENGE_TYPES.values())
    )
    st.write(challenges_type)

    challenges_stack = pills(
        "Challenge Stack",
        list(TECH_STACK.keys()),
        list(TECH_STACK.values())
    )
    st.write(challenges_stack)