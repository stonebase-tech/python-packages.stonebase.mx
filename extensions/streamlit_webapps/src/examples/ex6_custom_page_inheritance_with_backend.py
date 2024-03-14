import streamlit as st
from tornado.web import RequestHandler

from rhdzmota.ext.streamlit_webapps.page_view import PageView
from rhdzmota.ext.streamlit_webapps.backend import BackendRequestHandler


class CustomPageEndpoint(BackendRequestHandler):
    alias="ex6"

    def get(self):
        self.write({"message": "Hello, from Ex6!"})

class CustomPageView(PageView):

    def view(self, **kwargs):
        st.markdown("# My Custom View")
        st.info(f"This is the example 6 with a backend available here: /api/{CustomPageEndpoint.alias}")


if __name__ == "__main__":
    # Creating the view instance will start the backend automatically (__post_init__) regardless
    # of the context manager.
    with CustomPageView(page_title="Demo", page_layout="centered", backend_request_handler=CustomPageEndpoint) as page:
        page.view()
