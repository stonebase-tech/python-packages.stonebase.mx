from rhdzmota.ext.streamlit_webapps.page_view import PageView


if __name__ == "__main__":
    with PageView(page_title="EX1", page_layout="wide") as page:
        page.view()
