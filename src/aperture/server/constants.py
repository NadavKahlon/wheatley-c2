from importlib.metadata import version

import IPython

APERTURE_SERVER_VERSION = version("aperture")
APERTURE_SERVER_BANNER = (
    f"\n"
    f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    f"┃ Aperture Command & Control Server ┃\n"
    f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n"
    f"Software version: {APERTURE_SERVER_VERSION}\n"
)
APERTURE_SERVER_INTERACTIVE_BANNER = (
    f"\n"
    f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    f"┃ Aperture Command & Control Server ┃\n"
    f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n"
    f"Software version: {APERTURE_SERVER_VERSION}\n"
    f"Powered by IPython {IPython.__version__}\n"
)

WHEATLY_SERVER_HOST = "127.0.0.1"
WHEATLY_SERVER_PORT = 0x3333
