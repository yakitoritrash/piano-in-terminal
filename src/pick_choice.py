import sys, tty, termios

def pick_choice(options):
    print("Pick a choice:")
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    current_index = 0;
    try:
        while (True):
            for option in options:
                if current_index == options.index(option):
                    print(f"> {option}");
                else:
                    print(f"  {option}");
            key = sys.stdin.read(1)
            if key == "j":
                if current_index == 0:
                    current_index += 1
                else:
                    current_index -= 1;
            elif key == "k":
                if current_index == 0:
                    current_index += 1;
                else:
                    current_index -= 1;
            elif key == "\n" or key == "\r":
                return options[current_index]

            sys.stdout.write(f"\033[{len(options)}A")
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        print()
