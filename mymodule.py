import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
# The following line is a bit magical: it makes matplolib graph
# more beautiful by modifying the default style
import seaborn as sns

import pprint

class SetOfParliamentMember:
    def __init__(self, name):
        self.name = name
        
    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")
        
    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe
        
    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]
        
        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps
        
        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]
        
        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f%%"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()
        
    def split_by_political_party(self):
        result = {}
        data = self.dataframe
        
        # These 2 syntaxes are equivalent : data.parti_ratt_financier and data['parti_ratt_financier']
        all_parties = data["parti_ratt_financier"].dropna().unique()
            
        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMember('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset
        
        return result

    def __str__(self):
        names = [] ## todo: remplacer à la fin par une compréhension
        for row_index, mp in self.dataframe.iterrows(): ##todo: ici il y a du packing/unpacking
            names += [mp.nom]
        return str(names) # Python knows how to convert a list into a string
    
    def __repr__(self):
        return "Set of {} MPs".format(len(self.dataframe))
    
    def __len__(self):
        return self.number_of_mps
    
    def __contains__(self, mp_name):
        return mp_name in self.dataframe["nom"].values
    
    def __getitem__(self, index):
        try:
            result = dict(self.dataframe.ix[index])
        except:
            if index < 0:
                raise Exception("Please select a positive index")
            elif index >= len(self.dataframe):
                raise Exception("There are only {} MPs!".format(len(self.dataframe)))
            else:
                raise Exception("Wrong index")
        return result
    
    def __add__(self, other):
        if not isinstance(other, SetOfParliamentMember):
            raise Exception("Can not add a SetOfParliamentMember with an object of type {}".format(type(other)))
        
        df1, df2 = self.dataframe, other.dataframe ##todo: ici il y a du packing/unpacking
        df = df1.append(df2)
        df = df.drop_duplicates()
        
        s = SetOfParliamentMember("{} - {}".format(self.name, other.name))
        s.data_from_dataframe(df)
        return s
    
    def __radd__(self, other): ## todo: l'implementation de cette méthode ne suit à mon avis pas les bonnes pratiques
        return self
    
    def __lt__(self, other):
        return self.number_of_mps < other.number_of_mps
    
    def __gt__(self, other):
        return self.number_of_mps > other.number_of_mps
    
    # The following 2 methods are a way to simulate a calculated attribute 
    # (attribute 'number_of_mps' is calculated from attribute 'seld.dataframe')
    # There is a much better way to do it, using decorator '@property'
    def __getattr__(self, attr):
        if attr == "number_of_mps": ##todo: faire la version avec @property
            return len(self.dataframe)
        
    def __setattr__(self, attr, value):
        if attr == "number_of_mps":
            raise Exception("You can not set the number of MPs!") 
        self.__dict__[attr] = value ## todo: c'est l'occasion de parler de __dict__ dans le cours ;)

def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMember("All MPs")
    sopm.data_from_csv(os.path.join("data",data_file))
    sopm.display_chart()
    
    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

if NOTEBOOK: # bah oui, dans la case précédente on a jarté du code (pour lisibilité), faut bien le remettre à un moment!
    SetOfParliamentMember.__init__                 = Sauv.__init__
    SetOfParliamentMember.data_from_csv            = Sauv.data_from_csv
    SetOfParliamentMember.data_from_dataframe      = Sauv.data_from_dataframe
    SetOfParliamentMember.display_chart            = Sauv.display_chart
    SetOfParliamentMember.split_by_political_party = Sauv.split_by_political_party
    Sauv = SetOfParliamentMember