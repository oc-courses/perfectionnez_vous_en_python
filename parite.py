#/bin/bash
import os
import argparse
if not NOTEBOOK:
    import mymodule
    
def parse_arguments():
    
    if not NOTEBOOK:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d","--datafile",help="""CSV file containing pieces of 
            information about the members of parliament""")
        return parser.parse_args()
    
    else: ## todo: A enlever. Ici on triche car ArgumentParser est innutilisable dans un notebook
        class foo:
            pass
        o = foo()
        o.__dict__ = {
            'datafile' : "current_mps.csv"
        }
        return o
    
if __name__ == '__main__':
    args = parse_arguments()    
    launch_analysis(args.datafile)