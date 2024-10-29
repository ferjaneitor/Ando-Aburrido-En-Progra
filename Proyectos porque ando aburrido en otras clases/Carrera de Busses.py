import random
import os

def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def draw_bus(position):
    """Draw the bus at the specified position."""
    limit = 170
    print("|   " + (" " * position) + "_________________   " + (" " * (limit - position)) + "|   ")
    print(" |  " + (" " * position) + "|____|_____|____|___" + (" " * (limit - position)) + " |  ")
    print("  | " + (" " * position) + "|                 |)" + (" " * (limit - position)) + "  | ")
    print("   |" + (" " * position) + "|~~~@~~~~~~~~~@~~~|)" + (" " * (limit - position)) + "   |")

def bus_race():
    """Simulate the bus race."""
    bus1_position = 0
    bus2_position = 0
    border_line = "-" * 200
    Limit = 170

    while bus1_position < Limit and bus2_position < Limit:
        clear_screen()
        print(" ██████  █████  ██████  ██████  ███████ ██████   █████      ██████  ███████     ██████  ██    ██ ███████ ███████ ███████ ")
        print("██      ██   ██ ██   ██ ██   ██ ██      ██   ██ ██   ██     ██   ██ ██          ██   ██ ██    ██ ██      ██      ██     ")
        print("██      ███████ ██████  ██████  █████   ██████  ███████     ██   ██ █████       ██████  ██    ██ ███████ █████   ███████")
        print("██      ██   ██ ██   ██ ██   ██ ██      ██   ██ ██   ██     ██   ██ ██          ██   ██ ██    ██      ██ ██           ██")
        print(" ██████ ██   ██ ██   ██ ██   ██ ███████ ██   ██ ██   ██     ██████  ███████     ██████   ██████  ███████ ███████ ███████")
        print("")
        print(border_line)
        draw_bus(bus1_position)
        print(border_line)
        draw_bus(bus2_position)
        print(border_line)
        
        if random.randint(1, 100) % 2 == 0:
            bus1_position += 1
        else:
            bus2_position += 1

    
    if bus1_position >= Limit:
        print("")
        print("██████  ██    ██ ███████      ██     ██     ██ ██ ███    ██ ███████ ")
        print("██   ██ ██    ██ ██          ███     ██     ██ ██ ████   ██ ██     ")
        print("██████  ██    ██ ███████      ██     ██  █  ██ ██ ██ ██  ██ ███████")
        print("██   ██ ██    ██      ██      ██     ██ ███ ██ ██ ██  ██ ██      ██ ")
        print("██████   ██████  ███████      ██      ███ ███  ██ ██   ████ ███████")
        print("")
    else:
        print("")
        print("██████  ██    ██ ███████     ██████      ██     ██ ██ ███    ██ ███████ ")
        print("██   ██ ██    ██ ██               ██     ██     ██ ██ ████   ██ ██     ")
        print("██████  ██    ██ ███████      █████      ██  █  ██ ██ ██ ██  ██ ███████")
        print("██   ██ ██    ██      ██     ██          ██ ███ ██ ██ ██  ██ ██      ██ ")
        print("██████   ██████  ███████     ███████      ███ ███  ██ ██   ████ ███████ ")
        print("")


bus_race()