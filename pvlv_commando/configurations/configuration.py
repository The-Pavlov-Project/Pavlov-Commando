import configparser as cfg


CONFIG_PATH = 'configs/commando.cfg'


parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

COMMANDS_DIR = parser.get('commands', 'COMMANDS_DIR')


# Languages Handled for messages
ENG = 'eng'
ITA = 'ita'
