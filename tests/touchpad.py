import threading
import time
import os


class TouchpadHack:
    def __init__(self):
        self.__disabled = False
        self.__condition = threading.Condition()
        self.__disabled_until_time = time.monotonic()

        threading.Thread(target=self.timeoutThread).start()

    def timeoutThread(self):
        while True:
            with self.__condition:
                self.__condition.wait()
            os.system("xinput disable 8")
            print("disable")
            while time.monotonic() < self.__disabled_until_time:
                time.sleep(self.__disabled_until_time - time.monotonic())
            os.system("xinput enable 8")
            print("enable")

    def inputReadThread(self):
        f = open("/dev/input/event2", "rb")
        while True:
            # We read events here from the keyboard and then just ignore them.
            # The only thing we care about is that an event happens.
            event = f.read(100)
            with self.__condition:
                self.__condition.notify()
                self.__disabled_until_time = time.monotonic() + 0.5


TouchpadHack().inputReadThread()