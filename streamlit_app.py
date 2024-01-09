
from __future__ import annotations
import os
import streamlit as st
import numpy as np

from pages import feedback, past_challenges, the_challenges, welcome, your_stats
from config import active_props, static


def main() -> None:
    st.set_page_config(
        page_title="SMKDEV Coding Challenge",
        layout="wide",
    )

    # st.sidebar.title("Home")

    st.title("SMKDEV Coding Challenge 🚀")
    main_dash, leading_score = st.columns([0.7, 0.3])
    with main_dash:
        st.header("Today Problems")
        st.image("https://www.pixground.com/wp-content/uploads/2023/04/Clouds-Meet-The-Sea-AI-Generated-4K-Wallpaper-jpg.webp")

    with leading_score:
        st.markdown("### Real Time Standing Points")
        data = np.random.randn(10, 1)
        leading_score.line_chart(data)


if __name__ == '__main__':
    main()
