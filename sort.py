
import copy
import logging
from logging import info
import random
#import matplotlib.pyplot as plt
#import matplotlib.animation as ani

log = True

def bubble_sort(array):

    info("\n\tBubble Sort")
    info("\nStart\t\t\t  {0}\n".format(array))

    swaps = 0

    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                info("Compare {0:2d} & {1:2d}  Swap     {2}".format(array[j], array[j+1], array))
            else: 
                info("Compare {0:2d} & {1:2d}  No Swap  {2}".format(array[j], array[j+1], array))
            
    info("\nSwaps {0}".format(swaps))
    info("\nFinish\t\t\t  {0}".format(array))
    return array
    
def insertion_sort(array):

    info("\n\tInsertion Sort")
    info("\nStart\t\t\t  {0}\n".format(array))

    swaps = 0

    for i in range(len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            swaps += 1
            info("Compare {0:2d} & {1:2d}  Swap     {2}".format(array[j-1], array[j], array))
            j -= 1
    
    info("\nSwaps {0}".format(swaps))
    info("\nFinish\t\t\t  {0}".format(array))
    return array

def main():
    if log == True:
        logging.basicConfig(format='%(message)s', level=logging.INFO)

    original = []

    for i in range(10):
        original.append(random.randrange(100))
    
    #original = [5, 4, 3, 2, 1]

    dc = copy.deepcopy(original)
    bubble_sort(dc)

    dc = copy.deepcopy(original)
    insertion_sort(dc)
    
    #print ordered

if __name__ == '__main__':
    main()
