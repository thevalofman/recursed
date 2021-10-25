import sys
import flags
from textmod import pscr


def demo():
    pscr("That's where this demo ends. Press enter to quit.")
    while True:
        i = input().lower()
        if i == "":
            sys.exit()


def move(r):
    # <editor-fold desc="Den">
    if r == "den":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("K for kitchen\nH for hall\nS for stay put")
                continue
            elif i in ("k", "h"):
                flags.s_loop_counter = 0
                return i
            elif i == "s":
                pscr(f"Time passes. You stare at the ceiling fan, at the ancient, faded throw pillows beside you,"
                     f" at the broken radio on the coffee table. You listen to someone moving around in the"
                     f" kitchen, then to the birds fighting for the right to sit upon the corpse of a tree in the"
                     f" arboreal graveyard that is the backyard. You find yourself once more considering going to"
                     f" the kitchen or the hall, but there's no reason why you can't stay here. What do you do?")
                while True:
                    pscr(">", False)
                    i = input().lower()
                    if i == "options":
                        pscr("K for kitchen\nH for hall\nS for stay put")
                        continue
                    elif i in ("k", "h"):
                        flags.s_loop_counter = 0
                        return i
                    elif i == "s":
                        while True:
                            flags.s_loop_counter += 1
                            if flags.s_loop_counter < 15:
                                pscr("You continue sitting. Nothing continues happening. What do you do?")
                            elif flags.s_loop_counter == 15:
                                pscr(
                                    "Time slowly marches by. The fan treads on ceaselessly, never seeming to"
                                    " understand that it is bound to its circular path for all its life. What do"
                                    " you do?")
                            elif flags.s_loop_counter < 25:
                                pscr("You continue sitting. Nothing continues happening. What do you do?")
                            elif flags.s_loop_counter == 25:
                                pscr(
                                    "You consider trying to repair the radio before remembering that you know"
                                    " nothing about electronics. You return to staring at the fan. What do you do?")
                            elif flags.s_loop_counter < 100:
                                pscr("You continue sitting. Nothing continues happening. What do you do?")
                            elif flags.s_loop_counter == 100:
                                pscr(
                                    "You pass out. Your mother shakes you awake, telling you that it's time to sing"
                                    " Happy Birthday. Your father walks in from the kitchen with the cake, and you"
                                    " all sing Happy Birthday to your grandfather. Cake is served, laughs are had."
                                    " You leave when your grandfather starts nodding off. And with that, Saturday"
                                    " is over, along with the game. Next time, consider playing instead of hitting"
                                    " 's' literally 100 times. Press enter to quit.")
                                while True:
                                    pscr(">", False)
                                    i = input().lower()
                                    if i == "":
                                        sys.exit()
                            while True:
                                pscr(">", False)
                                i = input().lower()
                                if i == "options":
                                    pscr("K for kitchen\nH for hall\nS for stay put")
                                    continue
                                elif i in ("k", "h"):
                                    return i
                                elif i == "s":
                                    break
    # </editor-fold>
    # <editor-fold desc="Kitchen">
    if r == "kitchen":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("D for den")
                continue
            elif i == "d":
                return "d"
    # </editor-fold>
    # <editor-fold desc="Hall">
    if r == "hall":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("B for bathroom")
                if flags.times_visited_kitchen > 0 or flags.times_visited_library > 0:
                    pscr("L for library")
                else:
                    pscr("R for door on right")
                pscr("D for den")
                continue
            elif i in ("b", "d"):
                return i
            elif i in "l" and (flags.times_visited_kitchen > 0 or flags.times_visited_library > 0):
                return i
            elif i in "r" and (flags.times_visited_kitchen == 0 or flags.times_visited_library == 0):
                return i
    # </editor-fold>
    # <editor-fold desc="Bathroom">
    if r == "bathroom":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("W to wash hands\nH for hall")
                continue
            elif i == "w":
                if flags.hands_washed is False:
                    pscr("You wash your hands, with soap. You'll be eating cake later, might as well get clean now.")
                    flags.hands_washed = True
                    continue
                else:
                    pscr("Your hands are already clean, no need to waste water and soap.")
                    continue
            elif i == "h":
                return "h"
    # </editor-fold>
    # <editor-fold desc="Library">
    if r == "library":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("P to pick up the book\nH for hall")
                continue
            elif i in ("p", "h"):
                return i
    # </editor-fold>

    # <editor-fold desc="Camp">
    if r == "camp":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("N for north exit\nS for south exit\nE for east exit")
                continue
            elif i in ("n", "s", "e"):
                return i
    # </editor-fold>
    # <editor-fold desc="North">
    if r == "north":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("C for camp\nE for east side")
                continue
            elif i in ("c", "e"):
                return i
    # </editor-fold>
    # <editor-fold desc="South">
    if r == "south":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("C for camp\nE for east side")
                continue
            elif i in ("c", "e"):
                return i
    # </editor-fold>
    # <editor-fold desc="East">
    if r == "east":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("C for camp\nN for north side\nS for south side")
                continue
            elif i in ("c", "n", "s"):
                return i
    # </editor-fold>

    # <editor-fold desc="Chambers">
    if r == "chambers":
        if flags.attack is False:
            while True:
                pscr(">", False)
                i = input().lower()
                if i == "options":
                    pscr("G for Great Gathering Hall\nT for Training Arena")
                    continue
                if i in ("g", "t"):
                    return i
        else:
            while True:
                pscr(">", False)
                i = input().lower()
                if i == "options":
                    pscr("E for Hall of the Grand Elder Drake")
                    continue
                if i == "e":
                    return i
    # </editor-fold>
    # <editor-fold desc="Training Arena">
    if r == "training":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("G for gathering hall\nC for chambers")
                continue
            elif i in ("g", "c"):
                return i
    # </editor-fold>
    # <editor-fold desc="Escape">
    if r == "escape":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("L for left\nR for right")
                continue
            elif i in ("l", "r"):
                return i
    # </editor-fold>
    # <editor-fold desc="Escape 2">
    if r == "escape_2":
        while True:
            pscr(">", False)
            i = input().lower()
            if i == "options":
                pscr("L for left\nR for right\nS for straight ahead")
                continue
            elif i in ("l", "r", "s"):
                return i
    # </editor-fold>
