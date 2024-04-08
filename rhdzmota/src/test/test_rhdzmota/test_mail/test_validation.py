from rhdzmota.mail.validation import validate_email_pattern


def test_valid_email_patterns():
    for should_be_valid in [
        "hello@example.com",
        "hello@example.com.mx",
        "hello.world@example.com",
        "hello.world@example.com.mx",
    ]:
        assert validate_email_pattern(should_be_valid)


def test_invalid_email_patterns():
    for should_be_invalid in [
        "hello",
        "hello.world.ai",
        "hello@example",
    ]:
        assert not validate_email_pattern(should_be_invalid)
