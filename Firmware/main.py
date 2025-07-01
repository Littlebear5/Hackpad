import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

productiveBoard = KMKKeyboard()

macros = Macros()
productiveBoard.modules.append(macros)

PINS = [
    board.D5,   # SW1 or left tab
    board.D6,   # SW2 or copy
    board.D7,   # SW3 or right tab
    board.D8,   # SW4 or paste
    board.D9,   # SW5 or alt tab
    board.D10   # SW6 or cut
]

productiveBoard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

productiveBoard.keymap = [
    [
        KC.Macro(Press(KC.LCTL), Press(KC.LSFT), Tap(KC.TAB), Release(KC.LCTL), Release(KC.LSFT)),
        KC.Macro(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)),
        KC.Macro(Press(KC.LCTL), Tap(KC.TAB), Release(KC.LCTL)),
        KC.Marco(Press(KC.LCTL), Tap(KC.V), Release(KC.LCTL)),
        KC.Macro(Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT)),
        KC.Macro(Press(KC.LCTL), Tap(KC.X), Release(KC.LCTL))
    ]
]

if __name__ == '__main__':
        productiveBoard.go()