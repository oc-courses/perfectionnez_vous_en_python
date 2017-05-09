import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
# The following line is a bit magical: it makes matplolib graph
# more beautiful by modifying the default style
import seaborn as sns

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


# def launch_analysis(data_file, by_party = False):
#     sopm = SetOfParliamentMember("All MPs")
#     sopm.data_from_csv(os.path.join("data",data_file))
#     sopm.display_chart()
    
#     if by_party:
#         for party, s in sopm.split_by_political_party().items():
#             s.display_chart()