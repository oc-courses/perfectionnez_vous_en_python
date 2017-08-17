#! /usr/bin/env python3
# coding: utf-8

import argparse
import logging as lg

import analysis.csv as c_an
import analysis.xml as x_an

lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-e", "--extension", help="""Kind of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-p","--byparty", action='store_true', help="""displays
        a graph for each political party""")
    parser.add_argument("-i","--info", action='store_true', help="""information about
        the file""")
    parser.add_argument("-n","--displaynames", action='store_true', help="""displays
        the names of all the mps""")
    parser.add_argument("-s","--searchname", help="""search for a mp name""")
    parser.add_argument("-I","--index", help="""displays information about the Ith mp""")
    parser.add_argument("-g","--groupfirst", help="""displays a graph groupping all the 'g'
        biggest political parties""")
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile!')
    except Warning as e:
        lg.warning(e)
    else:
        if args.extension == 'xml':
            x_an.launch_analysis(datafile)
        elif args.extension == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info, args.displaynames,
                           args.searchname, args.index, args.groupfirst)
    finally:
        lg.info('#################### Analysis is over ######################')

if __name__ == '__main__':
    main()
