#!/usr/bin/python3

#Imported needed libraries.
import psutil
import os
import shutil
import winshell


message = {}

def check_cpu_usage():
     #Checks current CPU usage
     usage = psutil.cpu_percent(1)
     if usage > 80:
          message['cpu_usage'] = "CPU usage is over 80%! Current CPU usage is: {}%".format(usage)
          print("CPU usage is over 80%! Current CPU usage is: {}%".format(usage))
     else:
          print("Current CPU usage is: {}%".format(usage))

def check_disk_usage(disk):
     #Checks current disk usage
     du = shutil.disk_usage(disk)
     free = du.free / du.total * 100
     if free > 20:
          print("Available disk space is: {:.2f}%".format(free))
     else:
          print("Available disk space is less than 20%! Available disk space is: {:.2f}%".format(free))

def check_available_memory():
     #Checks current ram usage
     available_memory = psutil.virtual_memory().available/(1024*1024)
     if available_memory > 500:
          print("Available memory is {:.2f} MB.".format(available_memory)) 
     else:
          print("Available memory is less than 500 MB! Current reading is {:.2f} MB.".format(available_memory))  

def empty_temp_folder():
     path = "C:/Users/reave/AppData/Local/Temp"
     # Creates a list of files and directories in Temp folder
     dir = os.listdir(path)
     # Checks to see if Temp folder is already empty
     if len(dir) == 0:
          print("Temp folder is already empty!")
     else:
          # For loop for each file or directory in Temp folder
          for filename in os.listdir(path):
               # Getting the file path by combind Path and filename
               file_path = os.path.join(path, filename)
               # Using try and except block to handle exceptions
               try:
                    # Checking to see if it is a file or symbolic link  
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                         #Removes it
                         os.remove(file_path)
                    # Checking to see if it is a directory 
                    elif os.path.isdir(file_path):
                         #Deletes entire directory
                         shutil.rmtree(file_path)
               except Exception as e:
                     # Print exception/errors
                     print("Failed to delete {}s. Reason: {}s".format(file_path, e))
          print("Temp folder has been cleaned up!")


def empty_recycling_bin():
     # Using try and except block to handle exceptions
     try:   
     # Calling the built-in function to delete
     # the data inside Recycle-Bin
          winshell.recycle_bin().empty(confirm=False,
          show_progress=False, sound=True)
  
          # Print that the deletion in successful
          print("Recycle Bin is emptied now!")
  
     except:
          # Printing that the Recyclce-Bin is already Empty!
          print("Recycle Bin is already empty!")

# Call each function
check_cpu_usage()
check_disk_usage(os.path.realpath('/'))
check_available_memory()
empty_recycling_bin()
empty_temp_folder()

