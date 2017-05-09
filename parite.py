def parse_arguments():
    
    if not NOTEBOOK:
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-d","--datafile",help="""CSV file containing pieces of 
            information about the members of parliament""")
        parser.add_argument("-p","--byparty",action='store_true',help="displays a graph for each political party")
        
        return parser.parse_args()
    
    else: ## todo: A enlever. Ici on triche car ArgumentParser est innutilisable dans un notebook
        class foo:
            pass
        o = foo()
        o.__dict__ = {
            'datafile' : "current_mps.csv",
            'byparty' : True,
        }
        return o
    
if __name__ == '__main__':
    args = parse_arguments()    
    launch_analysis(args.datafile, args.byparty)

    
if NOTEBOOK:
    Sauv = SetOfParliamentMember # sauvegarde de la classe