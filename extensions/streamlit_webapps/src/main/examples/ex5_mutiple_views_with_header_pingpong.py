import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view_switcher import PageViewSwitcher
from rhdzmota.ext.streamlit_webapps.page_view import (
    PageViewHeader,
    PageView,
)


class PingPongHeader(PageViewHeader):
    def on_start(self):
        st.markdown("# PingPong Header")
        st.text("This text is part of the header.")
        if self.history_exists() and st.button("Return"):
            self.backward()


class PingView(PageView, PingPongHeader):

    def view(self, **kwargs):
        st.markdown("## Ping!")
        st.info("You are in the ping view...")
        if st.button("Go pong!"):
            return self.forward(PongView.refname)


class PongView(PageView, PingPongHeader):

    def view(self, **kwargs):
        st.markdown("## Pong!")
        st.info("You are in the pong view...")
        if st.button("Go ping!"):
            return self.forward(PingView.refname)


if __name__ == "__main__":
    ping = PingView(page_title="Ping", page_layout="centered")
    pong = PongView(page_title="Pong", page_layout="centered")
    switcher = PageViewSwitcher.from_page_views(
        switcher_name="pingpong",
        page_views=[ping, pong],  # Order is not relevant here.
    )
    switcher.run(initial_page_key=ping.refname)
