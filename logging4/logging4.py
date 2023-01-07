import datetime

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

_level2name = {
    CRITICAL: "CRITICAL",
    ERROR: "ERROR",
    WARNING: "WARNING",
    INFO: "INFO",
    DEBUG: "DEBUG",
    NOTSET: "NOTSET"
}


class Logger(object):
    def __init__(self, name="logger"):
        self.name = name
        self.channel = dict()
        self.time_fmt = '%Y-%m-%d %H:%M:%S'

    def add_channel(self, filename, level, formatter='[[msg]]'):
        self.channel[filename] = [level, formatter]

    def del_channel(self, filename):
        del self.channel[filename]

    def clear_channel(self):
        self.channel.clear()

    def __print(self, msg, level):
        for filename, (level_, formatter) in self.channel.items():
            if level >= level_:
                text = msg \
                    .replace('[[time]]', datetime.datetime.now().strftime(self.time_fmt)) \
                    .replace('[[name]]', self.name) \
                    .replace('[[level_name]]', _level2name.get(level, "LEVEL_" + str(level))) \
                    .replace('[[msg]]', msg)
                if isinstance(filename, str):
                    with open(filename, "a") as f:
                        print(text, file=f, flush=True)
                else:
                    print(text, file=filename, flush=True)

    def debug(self, msg):
        self.__print(msg, DEBUG)

    def info(self, msg):
        self.__print(msg, INFO)

    def warning(self, msg):
        self.__print(msg, WARNING)

    def error(self, msg):
        self.__print(msg, ERROR)

    def critical(self, msg):
        self.__print(msg, CRITICAL)
