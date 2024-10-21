import pyautogui
import keyboard
import threading

# Initializing control variables
spam_active = False

# Function to hold right-click
def hold_right_click():
    while spam_active:
        pyautogui.mouseDown(button='right')  # Hold the right-click down
    pyautogui.mouseUp(button='right')  # Release the right-click when stopped

# Function to toggle holding on and off
def toggle_spam():
    global spam_active
    spam_active = not spam_active
    if spam_active:
        print("Right-click hold started.")
        threading.Thread(target=hold_right_click).start()
    else:
        print("Right-click hold stopped.")

# Binding Left Shift + Z to toggle the right-click hold
keyboard.add_hotkey('left shift+z', toggle_spam)

# Keep the script running to listen for key presses
print("Press Left Shift + Z to start/stop holding the right-click.")
keyboard.wait()  # Waits indefinitely until program is stopped
