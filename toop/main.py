#!/usr/bin/env python

"""
main() module -- Entrypoint to the library
"""

import sys
from toop import monitor
from pyfiglet import Figlet
from termcolor import cprint


def main():
    """
    Startup function to run the toop script
    """
    try:
        url = sys.argv[1]
    except IndexError:
        print("you need to pass in a url to proceed")
        sys.exit()

    try:
        interval = sys.argv[2]
    except IndexError:
        interval = 1
    except ValueError:
        print("Please provide an integer as argument")

    title = Figlet(font="slant")
    cprint(title.renderText("toop toop toop :"), "blue", attrs=['bold'])
    monitor.monitor(website_url=url, interval=int(interval))
    cprint("Pinging stopped", "blue")
