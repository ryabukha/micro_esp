
from machine import Pin
import time


class Button():
    '''
    class Button
    '''

    flags_btn_deb = False
    flags_btn_flag = True
    flags_btn_state = False
    flags_isPress_f = False
    flags_oneClick_f = True
    flags_hold_flag = False
    btn_counter = 0
    flags_isRelease_f = False
    flags_step_flag = True
    flags_isOne_f = False
    btn_timer = time.ticks_ms()
    flags_tickMode = False
    counter_flag = True
    last_counter = 0
    flags_counter_flag = True
    timeout = 500
    flags_isHolded_f = False
    flags_hold_flag = True

    def __init__(self, pin=5, click_timeout=300, debounce=60, step_timeout=400):
        self.pin = pin
        self.debounce = debounce
        self.click_timeout = click_timeout
        self.step_timeout = step_timeout
        self.btn = Pin(pin, Pin.IN)

    def tick(self):
        # read pin
        self.flags_btn_state = self.btn.value()
# нажатие
        if self.flags_btn_state and not self.flags_btn_flag:
            if not self.flags_btn_deb:
                self.flags_btn_deb = True
                self.btn_timer = time.ticks_ms()
            else:
                if time.ticks_ms() - self.btn_timer >= self.debounce:
                    self.flags_btn_flag = True
                    self.flags_isPress_f = True
                    self.flags_oneClick_f = True
        else:
            self.flags_btn_deb = False
# otpuskaem
        if not self.flags_btn_state and self.flags_btn_flag:
            self.flags_btn_flag = False
            if not self.flags_hold_flag:
                self.btn_counter = self.btn_counter + 1
            self.flags_hold_flag = False
            self.flags_isRelease_f = True
            self.btn_timer = time.ticks_ms()
            self.flags_step_flag = False
            if self.flags_oneClick_f:
                self.flags_oneClick_f = False
                self.flags_isOne_f = True
        # hold
        if self.flags_btn_flag and self.flags_btn_state and time.ticks_ms() - self.btn_timer >= self.timeout and not self.flags_hold_flag:
            self.flags_hold_flag = True
            self.btn_counter = 0
            self.last_counter = 0
            self.flags_isHolded_f = True
            self.flags_step_flag = True
            self.flags_oneClick_f = False
            self.btn_timer = time.ticks_ms()

        if time.ticks_ms() - self.btn_timer >= self.click_timeout and self.btn_counter > 0:
            self.last_counter = self.btn_counter
            self.btn_counter = 0
            self.flags_counter_flag = True

    def setTickMode(self, tickMode):
        self.flags_tickMode = tickMode

    def isSingle(self):
        if self.flags_tickMode:
            self.tick()
        if self.flags_counter_flag and self.last_counter == 1:
            self.flags_counter_flag = False
            return True
        else:
            return False

    def isDouble(self):
        if self.flags_tickMode:
            self.tick()
        if self.flags_counter_flag and self.last_counter == 2:
            self.flags_counter_flag = False
            return True
        else:
            return False

    def isTriple(self):
        if self.flags_tickMode:
            self.tick()
        if self.flags_counter_flag and self.last_counter == 3:
            self.flags_counter_flag = False
            return True
        else:
            return False

    def isPress(self):
        if self.flags_isPress_f:
            self.flags_isPress_f = False
            return True
        else:
            return False

    def state(self):
        if self.flags_tickMode:
            self.tick()
        return self.flags_btn_state

    def main(self):
        while True:
            self.tick()
            if self.isPress():
                print("Is pressed")
            if self.isDouble():
                print("is Double")
            if self.isSingle():
                print("is Single")
            if self.state():
                print("state True")
