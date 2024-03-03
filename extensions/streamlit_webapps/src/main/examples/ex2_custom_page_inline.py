import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import PageView


def view(*args, **kwargs):
    st.markdown("# My Custom View")
    st.info("This is the example 2!")
    st.error(
        "Consider that we do not recommend inline-views; "
        "see example 3 for an alternative using inheritance."
    )


if __name__ == "__main__":
    with PageView.inline("CustomView", func=view)(page_title="Demo", page_layout="centered") as page:
        page.view()
