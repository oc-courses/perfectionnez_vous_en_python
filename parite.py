def parse_arguments():
    
    if not NOTEBOOK:
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-d","--datafile",help="""CSV file containing pieces of 
            information about the members of parliament""")
        parser.add_argument("-p","--byparty", action='store_false', help="""displays 
            a graph for each political party""")
        parser.add_argument("-i","--info", action='store_false', help="""information about
            the file""")
        parser.add_argument("-n","--displaynames", action='store_false',help="""displays 
            the names of all the mps""")
        parser.add_argument("-s","--searchname", help="""search for a mp name""")
        parser.add_argument("-I","--index", help="""displays information about the Ith mp""")
        parser.add_argument("-g","--groupfirst", help="""displays a graph groupping all the 'g' 
            biggest political parties""")
        
        return parser.parse_args()
    
    else: ## todo: A enlever. Ici on triche car ArgumentParser est innutilisable dans un notebook
        class foo:
            pass
        o = foo()
        o.__dict__ = {
            'datafile' : "current_mps.csv",
            'byparty' : False,
            'info' : True,
            'displaynames' : True,
            'searchname' : "Dark Vador",
            'index': 0,
            'groupfirst' : 3,
        }
        return o
    
if __name__ == '__main__':
    args = parse_arguments()    
    launch_analysis(args.datafile, args.byparty, args.info, args.displaynames,
                   args.searchname, args.index, args.groupfirst) ##todo: faire du packing/unpacking pour tous ces arguments?