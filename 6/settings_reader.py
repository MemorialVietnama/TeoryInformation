# settings_reader.py

import configparser

def read_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['Settings']['WordSize'])
