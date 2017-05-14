import os
import logging as lg

def launch_analysis(data_file):

    # this will render an error if data_file is empty.
    path_to_file = os.path.join("data", data_file)

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
        lg.error(e)
    except:
        print('Another error')

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
