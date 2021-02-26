import os


def bearerOSEvn():
    return f"Bearer {os.environ['TwitterBearer']}"
