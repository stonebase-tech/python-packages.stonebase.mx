import streamlit as st

from rhdzmota.ext.streamlit_webapps.components.catalog import CompCatalog
from rhdzmota.ext.streamlit_webapps.components.collection_email_acl_via_token.utils import (
    PHEmailACLBouncerHeader
)

from rhdzmota.ext.streamlit_webapps.page_view_switcher import PageViewSwitcher
from rhdzmota.ext.streamlit_webapps.page_view import (
    PageViewHeader,
    PageView,
)


class ProtectedViewExample(PageView, PHEmailACLBouncerHeader):
    def view(self):
        st.markdown("# Hello!")
        st.text(
            "Only authorized users should be able to see this info."
        )


if __name__ == "__main__":
    example = ProtectedViewExample()
    email_acl_failure = CompCatalog.EMAIL_ACL_FAILURE.configure()
    email_acl_success = CompCatalog.EMAIL_ACL_SUCCESS.configure()
    email_acl_gatekeeper = CompCatalog.EMAIL_ACL_GATEKEEPER.configure(
        from_email="example@email.com",  # TODO: Replace example email with actual email
        reference_url_pattern="http://localhost:8501?token={token}",  # TODO: Replace URL Pattern
        reference_page_redirect=example.refname,
        reference_page_on_success=email_acl_success.refname,
        reference_page_on_failure=email_acl_failure.refname,
        reference_service_title="The Example Service",
    )
    switcher = PageViewSwitcher.from_page_views(
        switcher_name="example",
        page_views=[
            example,
            email_acl_failure,
            email_acl_success,
            email_acl_gatekeeper, 
        ]
    )
    switcher.run(
        initial_page_key=email_acl_gatekeeper
            .get_start_page_or_use_me_instead()
    )
