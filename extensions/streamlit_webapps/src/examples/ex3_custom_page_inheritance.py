import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import PageView


class CustomPageView(PageView):

    def view(self, **kwargs):
        st.markdown("# My Custom View")
        st.info("This is the example 3!")


if __name__ == "__main__":
    with CustomPageView(page_title="Demo", page_layout="centered") as page:
        page.view()
