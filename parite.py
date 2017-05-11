#/bin/bash
import os
import argparse
import analysis as an
    
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of 
        information about the members of parliament""")
    return parser.parse_args()
    
if __name__ == '__main__':
    args = parse_arguments()    
    an.launch_analysis(args.datafile)