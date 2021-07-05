import os 
import sys
import time


#last line deletion
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
    
    
###DEMO###
print("this line will delete in 5 seconds")
time.sleep(2)
delete_last_line()