from rhdzmota.ext.{{cookiecutter.project_slug}}.settings import Env


def test_env_app_name():
    app_name = "{{cookiecutter.project_slug}}"
    assert Env.EXT_APP_NAME.value.startswith(app_name)
