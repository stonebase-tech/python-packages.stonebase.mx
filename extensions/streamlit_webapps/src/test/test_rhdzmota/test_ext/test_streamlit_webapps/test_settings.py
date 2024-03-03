from rhdzmota.ext.streamlit_webapps.settings import Env


def test_env_app_name():
    app_name = "streamlit_webapps"
    assert Env.EXT_APP_NAME.startswith(app_name)
