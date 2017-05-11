#/bin/bash
import os
import argparse
import analysis as an
#import pdb
import logging as lg
    
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of 
        information about the members of parliament""")
    return parser.parse_args()
    
if __name__ == '__main__':
    try:
        args = parse_arguments()
        # pdb.set_trace()    
        an.launch_analysis(args.datafile)
    except:
        lg.critical('You should use a -d flag and indicate the original file.')
    finally:
        print('------------------ End of analysis -----------------')
