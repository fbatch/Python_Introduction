import time
from termcolor import colored


class TrafficLight:
    __color = 'Private attr'

    def running(self, color):
        if color == 'red':
            print(colored('RED', 'red'))
            time.sleep(7)
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
            print(colored('GREEN', 'green'))
            time.sleep(5)
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
        if color == 'yellow':
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
            print(colored('GREEN', 'green'))
            time.sleep(5)
            print(colored('RED', 'red'))
            time.sleep(7)
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
        if color == 'green':
            print(colored('GREEN', 'green'))
            time.sleep(5)
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
            print(colored('RED', 'red'))
            time.sleep(7)
            print(colored('YELLOW', 'yellow'))
            time.sleep(2)
        if color != 'green' and color != 'red' and color != 'yellow':
            print('Enter a valid color!')


a = TrafficLight()
a.running('red')
