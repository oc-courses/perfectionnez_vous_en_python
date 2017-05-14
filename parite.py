#! /usr/bin/env python3
# coding: utf-8
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
