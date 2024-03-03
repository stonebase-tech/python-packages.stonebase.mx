import enum
from typing import List

import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import (
    PageView,
    CanonicalErrorView,
)


class PageSwitcher(enum.Enum):

    @classmethod
    def from_pages(
            cls,
            switcher_name: str,
            pages: List[PageView],
            disable_canonical_error: bool = False,
    ) -> 'PageSwitcher':
        canonical_error_item = ("canonical_error", CanonicalErrorView())
        return cls(
            value=switcher_name,
            names=[
                (page.refname, page)
                for page in pages
            ] + ([] if disable_canonical_error else [canonical_error_item]),
        )

    @classmethod
    def run(cls, initial_page_key: str, **initial_page_kwargs):
        # On first execution, save the inital page key with their corresponding kwargs 
        page_current = st.session_state.get(PageView.session_key_page_current, None)
        if not page_current:
            st.session_state[PageView.session_key_page_current] = initial_page_key
            st.session_state[PageView.session_key_page_current_input_kwargs] = initial_page_kwargs
        # Execute the page defined on the session-state

        with cls[page_current or initial_page_key].value as current_page_instance:
            current_page_instance.view(
                **st.session_state.get(
                    PageView.session_key_page_current_input_kwargs,
                    {}
                )
            )
