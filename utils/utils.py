import configparser
import logging


def default_logger():
    format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, filename='test.log', filemode='a')
    logger = logging.getLogger('test_logger')
    return logger


def read_config_file(path_ini):
    conf_dict = {}
    conf = configparser.RawConfigParser()
    conf.read(path_ini)
    for section in conf.sections():
        tmp = {opt: val for opt, val in conf.items(section)}
        conf_dict[section] = tmp

    return conf_dict
