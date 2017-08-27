"""Config: Holds all of your app config data."""


class BaseConfig(object):
    """Main config vars."""

    PROJECT = "app"

    DEBUG = True
    # os.urandom(24)
    SECRET_KEY = 'j\xaa{\x13\xc2z\xee\xd2&R\xdb\x11D\xcb\xb0T>Z\xc5\xf8[\x1a\xc9\xcc'
