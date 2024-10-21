import pyautogui
import platform
import threading
import time

# Detecting the OS to use the correct keyboard input handling
current_os = platform.system()

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

# OS-specific keybinding
if current_os == 'Windows':
    import keyboard

    # Binding Left Shift + Z to toggle the right-click hold (Windows)
    keyboard.add_hotkey('left shift+z', toggle_spam)

    # Keep the script running to listen for key presses
    print("Press Left Shift + Z to start/stop holding the right-click.")
    keyboard.wait()  # Waits indefinitely until program is stopped

elif current_os == 'Darwin':  # Darwin means macOS
    from pynput import keyboard

    # Function to detect key press combinations (macOS)
    def on_press(key):
        global spam_active
        try:
            if key == keyboard.Key.shift and keyboard_controller.pressed_key == 'z':
                toggle_spam()
        except AttributeError:
            pass

    def on_release(key):
        # Reset the key when released (macOS)
        if key == keyboard.Key.shift or key == keyboard.KeyCode.from_char('z'):
            pass  # No need to toggle on release

    # Start listening to key presses on macOS
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    print("Press Left Shift + Z to start/stop holding the right-click.")
