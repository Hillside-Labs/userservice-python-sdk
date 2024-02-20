from userup import Client, config, types


def main():
    config.base_url = "http://localhost:9001/api/"
    user_id = 1
    c = Client(config.base_url)

    c.track(
        user_id,
        types.Click,
        {
            "target": "#some-id",
            "element": {
                "a": {
                    "href": "/foo/bar/baz",
                }
            },
        },
    )


if __name__ == "__main__":
    main()
