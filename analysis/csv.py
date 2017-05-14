import os

def launch_analysis(data_file):

    # If data_file is an absolute path, then the folder "data" is ignored
    # and path_to_file will equals data_file
    # If not, "data" will be append at the beginning of the path
    path_to_file = os.path.join("data", data_file)

    file_name = os.path.basename(path_to_file)
    directory = os.path.dirname(path_to_file)
    print("Opening data file {} from directory '{}'".format(file_name,directory))

    with open(path_to_file,"r") as f:
       preview = f.readline() # read first line

    print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
