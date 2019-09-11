import sys
import os
from xcubia import monitor


def main():
    try:
        url = sys.argv[1]
    except IndexError:
        print("you need to pass in a url to proceed")
        sys.exit()

    print("Started...")
    monitor.monitor(website_url=url)
    print("Stopped")
