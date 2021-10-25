import sys
import time
import textwrap
color = {
    "Purple": '\033[95m',
    "Cyan": '\033[96m',
    "DarkCyan": '\033[36m',
    "Blue": '\033[94m',
    "Green": '\033[92m',
    "Yellow": '\033[93m',
    "Red": '\033[91m',
    "Bold": '\033[1m',
    "Underline": '\033[4m',
    "End": '\033[0m'
}


def c_and_under(col, r):  # This colors and underlines a string
    s = f'{color[col]}{color["Underline"]}{r}{color["End"]}'
    return s


def pscr(s, n=True):
    st = textwrap.fill(s, 100, replace_whitespace=False, drop_whitespace=False)
    for x in st:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.005)
    if n is True:
        sys.stdout.write("\n")


def pscr_slow(s, n=True):
    st = textwrap.fill(s, 100, replace_whitespace=False, drop_whitespace=False)
    for x in st:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.15)
    if n is True:
        sys.stdout.write("\n")


def pscr_rock(s, n=True):
    st = textwrap.fill(s, 100, replace_whitespace=False, drop_whitespace=False)
    for x in st:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.06)
    if n is True:
        sys.stdout.write("\n")
