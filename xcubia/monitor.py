import requests
import os


def monitor(website_url):

    try:
        req = requests.get(website_url)

        if req.status_code == 200:
            message = "LIVE!🔴"
        else:
            message = "DOWN!⚫️"
    except Exception as error:
        message = f'Error : {error}'
    finally:
        title = '-title {!r}'.format(f'Status for {website_url}:')
        message = '-message {!r}'.format(message)
        os.system(
            'terminal-notifier {}'.format(' '.join([message, title])))
