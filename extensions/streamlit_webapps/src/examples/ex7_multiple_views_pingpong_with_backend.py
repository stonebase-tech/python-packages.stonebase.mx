import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import PageView
from rhdzmota.ext.streamlit_webapps.page_view_switcher import PageViewSwitcher
from rhdzmota.ext.streamlit_webapps.backend import BackendRequestHandler


class PingView(PageView):

    def view(self, **kwargs):
        st.markdown("## Ping!")
        st.info("You are in the ping view...")
        if st.button("Go pong!"):
            return self.forward(PongView.refname)

class PongView(PageView):

    def view(self, **kwargs):
        st.markdown("## Pong!")
        st.info("You are in the pong view...")
        if st.button("Go ping!"):
            return self.forward(PingView.refname)

class PingPongEndpoint(BackendRequestHandler):

    def get(self):
        respond_to = self.get_query_argument("respond_to") or ""
        if not respond_to:
            self.write({"I say": "ping"})
        self.write({"You said": respond_to, "I say": "pong"})


if __name__ == "__main__":
    ping = PingView(page_title="Ping", page_layout="centered")
    pong = PongView(page_title="Pong", page_layout="centered")
    switcher = PageViewSwitcher.from_page_views(
        switcher_name="pingpong",
        page_views=[ping, pong],  # Order is not relevant here.
    )
    switcher.run(initial_page_key=ping.refname, backend_request_handler=PingPongEndpoint)
