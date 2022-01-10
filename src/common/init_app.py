import os

import requests
from requests.auth import HTTPBasicAuth


def set_configs():
    app_config = os.environ.get('ENVIRONMENT_API')
    if os.environ.get('ENVIRONMENT') != 'production':
        return

    resp = requests.get('{}/app-config/api/configs?env={}'.format(
        app_config,
        os.environ.get('ENVIRONMENT')),
        auth=HTTPBasicAuth(
            os.environ.get('ENVIRONMENT_USER'),
            os.environ.get('ENVIRONMENT_PASSWORD'))
    )
    configs = resp.json()
    for item in configs:
        os.environ.setdefault(item['key'], item['value'])
