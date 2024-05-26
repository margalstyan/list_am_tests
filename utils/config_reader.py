import codecs
import configparser

config = configparser.ConfigParser()
with codecs.open('../config.properties', 'r', 'utf-8') as f:
    config.read_file(f)


def get_config_value(key, section='DEFAULT'):
    return config.get(section, key)
