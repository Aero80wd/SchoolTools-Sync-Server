from enum import Enum
import datetime
class LogLevel(Enum):
    ALL = 1
    INFO = 3
    WARNING = 4
    ERROR = 5
    CRITICAL = 6
class LogLevelColor:
    ALL = '\033[0m'
    CRITICAL = '\033[34m'
    WARNING = '\033[33m'
    ERROR = '\033[31m'
    INFO = '\033[32m'
def log(loglevel,*types):
    time_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(eval(f"LogLevelColor.{loglevel.name}"),end='')
    print(f"[{time_string}] ",end='')
    for type in types:
        print(type,end=' ')
    print()
