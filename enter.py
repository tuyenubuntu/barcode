from pynput import keyboard

print('Press s or n to continue:')

with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('0'):
        print("YES")
        