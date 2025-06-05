import pyautogui
import keyboard
import time

def move_mouse_square(size=50, delay=0.1):
    start_x, start_y = pyautogui.position()

    # Define square pattern
    pattern = [
        (size, 0),
        (0, size),
        (-size, 0),
        (0, -size)
    ]

    print("Mouse Jiggler started. Press ENTER to stop.")
    while not keyboard.is_pressed('enter'):
        for dx, dy in pattern:
            pyautogui.moveRel(dx, dy, duration=0.1)
            time.sleep(delay)
            if keyboard.is_pressed('enter'):
                break

    print("Mouse Jiggler stopped.")

if __name__ == "__main__":
    input("Press ENTER to start jiggling...")
    move_mouse_square()
