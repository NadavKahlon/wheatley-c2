import argparse
import threading

from aperture.server.constants import (
    WHEATLY_SERVER_PORT,
    WHEATLY_SERVER_HOST,
    APERTURE_SERVER_BANNER,
    APERTURE_SERVER_INTERACTIVE_BANNER,
)
from aperture.server.server import ApertureServer
from aperture.server.local_shell import LocalServerShell


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aperture Command & Control Server")
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Start the server with a local interactive shell",
    )
    return parser.parse_args()


def start_interactive(args: argparse.Namespace):
    print(APERTURE_SERVER_INTERACTIVE_BANNER)
    server = ApertureServer((WHEATLY_SERVER_HOST, WHEATLY_SERVER_PORT))
    server_thread = threading.Thread(target=server.run, daemon=True)
    server_thread.start()
    LocalServerShell(server).run()
    server.terminate_run()


def start_non_interactive(args: argparse.Namespace):
    print(APERTURE_SERVER_BANNER)
    server = ApertureServer((WHEATLY_SERVER_HOST, WHEATLY_SERVER_PORT))
    try:
        server.run()
    except KeyboardInterrupt:
        return


def start():
    args = parse_args()
    if args.interactive:
        start_interactive(args)
    else:
        start_non_interactive(args)
