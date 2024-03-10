from rhdzmota.wrappers.sentry import SentrySDKConfig


def main():
    SentrySDKConfig.configure_with_defaults()

    # This should trigger an error
    div_result = 1 / 0


if __name__ == "__main__":
    main()
