import os


def bearerOSEnv():
    return f"Bearer {os.environ['TwitterBearer']}"
