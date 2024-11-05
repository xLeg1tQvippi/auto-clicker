import keyboard, mouse, time

def change():
    global work
    work = not work
    print(work)
if __name__ == '__main__':
    hot_key = '`'
    cps = 1
    print(f'1 - to change hotkey | default: {hot_key}\n2 - set click speed | default: {cps} cps.\n0 - exit')
    config = input('>>>')
    while True:
        if config == '1': hot_key = input(f'input hotkey for turning on clicker: (default: {hot_key}\n>>>')
        if config == '2': cps = float(input(f'input CPS: (default: {cps}cps)'))
        if config == '0': break
        print('1 - to change hotkey\n2 - set click speed\n0 - exit')
        config = input('>>>')
    work = False
    keyboard.add_hotkey(hot_key, change)
    print(f'autoclicker started!\npress "{hot_key}" to run clicker.')
    while True:
        if work:
            mouse.click()
            time.sleep(cps)