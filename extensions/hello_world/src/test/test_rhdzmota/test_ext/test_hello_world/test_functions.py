from rhdzmota.ext.hello_world.functions import hello


def test_hello_world_recipients():
    recipient_a = "Alice"
    recipient_b = "Bob"
    for recipient in [recipient_a, recipient_b]:
        output = hello(recipient=recipient)
        assert output.endswith(f"{recipient}!")
