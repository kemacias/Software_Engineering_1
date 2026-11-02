# Kate Macias
# Software engineering 1
# Fall 2026
#

import sys
import datetime

class TimeLogger:
    def isotime(self):
        return datetime.datetime.now().isoformat()

    def event(self, s):
        print(f"{self.isotime()}: {s}")

    def warning(self, s):
        print(f"{self.isotime()}: WARNING: {s}")

class Logger:
    def event(self, s):
        print(s)

    def warning(self, s):
        print(s, file=sys.stderr)

def pick_logger():
    choice = input("Pick a logger, 1 or 2: ").strip()
    if choice == "1":
        return Logger()
    else:
        return TimeLogger()

class Divider:
    def __init__(self, logger=None):
        if logger is None:
            logger = pick_logger()
        self.logger = logger

    def divide(self, a, b):
        if b == 0:
            self.logger.warning("division by zero")
            return None
        self.logger.event(f"dividing {a} by {b}")
        return a / b

d = Divider()

d.divide(1, 2)
d.divide(10, 5)
d.divide(99, 0)
