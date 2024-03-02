from rhdzmota.settings import Env


def test_env_retrieval():
    env_var_not_exists = "ENV_VAR_THAT_DOESNT_EXISTS"
    env_var_default = "default"
    assert not Env.get(env_var_not_exists)
    assert Env.get(env_var_not_exists, default=env_var_default) == env_var_default
    try:
        Env.get(env_var_not_exists, enforce=True)
    except ValueError as e:
        # Detected correctly that the env.var doesn't exists
        assert str(e).split(":")[-1].strip() == env_var_not_exists
