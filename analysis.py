import os
import logging as lg

def launch_analysis(data_file):
    
    # If data_file is an absolute path, then the folder "data" is ignored
    # and path_to_file will equals data_file
    # If not, "data" will be append at the beginning of the path
    path_to_file = os.path.join("data",data_file)
    
    file_name = os.path.basename(path_to_file)
    directory = os.path.dirname(path_to_file)
    print("Opening data file {} from directory '{}'".format(file_name,directory))
    
    try:
        with open(path_to_file,"r") as f:
            preview = f.readline()
        print("Yeah! We managed to read the file. Here is a preview:")
        print(preview)
        
    except FileNotFoundError as e:
        print("Ow :( The file was not found. Here is the original message of the exception :")
        # e is a FileNotFoundError, which is also an Exception (by inheritance).
        # print(e) prints the error message (which is a string) of this Exception.
        lg.error(e)