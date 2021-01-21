import time


class TrafficLight:
    _colors = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 6:
            for el in TrafficLight._colors:
                print(el)
                i += 1
                if el == 'red':
                    time.sleep(7)
                elif el == 'yellow':
                    time.sleep(2)
                elif el == 'green':
                    time.sleep(5)


traffic = TrafficLight()
traffic.running()
