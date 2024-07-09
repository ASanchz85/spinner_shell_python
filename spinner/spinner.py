import sys
import time
import os

# Spinner frames
spinner_frames = ["|", "/", "-", "\\"]


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_terminal_size():
    rows, columns = os.popen("stty size", "r").read().split()
    return int(rows), int(columns)


def print_spinner(center_x, center_y, duration):
    start_time = time.time()
    spinner_index = 0

    # Hide the cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while (time.time() - start_time) < duration:
            # Move cursor to the center position
            sys.stdout.write(f"\033[{center_y};{center_x}H")
            # Print spinner frame
            sys.stdout.write(spinner_frames[spinner_index])
            sys.stdout.flush()
            # Update spinner frame
            spinner_index = (spinner_index + 1) % len(spinner_frames)
            # Sleep for a bit to animate the spinner
            time.sleep(0.1)
    finally:
        # Show the cursor again
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        # Clear the spinner after completion
        sys.stdout.write(f"\033[{center_y};{center_x}H ")
        sys.stdout.flush()


def main(duration=5):
    duration = duration

    # Get the terminal size
    clear_screen()

    rows, columns = get_terminal_size()

    # Calculate the center position
    center_x = columns // 2
    center_y = rows // 2

    # Print spinner
    print_spinner(center_x, center_y, duration)


if __name__ == "__main__":
    main()
