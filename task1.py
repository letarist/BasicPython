from time import sleep


class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        while i < 3:
            print("светофор переключается ")
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1
#        else:
#            while i >= 3:
#                if i == 0:
#                    sleep(7)
#                elif i == 1:
#                    sleep(2)
#                elif i == 2:
#                    sleep(7)
#                i -= 1


TrafficLight = TrafficLight()
TrafficLight.running()
