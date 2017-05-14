import argparse
import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-e", "--extension", help="""King of of file to analyse. Is it a CSV of an XML?""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    if args.extension == 'xml':
        x_an.launch_analysis(args.datafile)
    elif args.extension == 'csv':
        c_an.launch_analysis(args.datafile)

#import pdb
# import logging as lg
#     
# def parse_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-d","--datafile",help="""CSV file containing pieces of
#         information about the members of parliament""")
#     return parser.parse_args()
#
# if __name__ == '__main__':
#     try:
#         args = parse_arguments()
#         # pdb.set_trace()
#         an.launch_analysis(args.datafile)
#     except:
#         lg.critical('You should use a -d flag and indicate the original file.')
#     finally:
#         print('------------------ End of analysis -----------------')
