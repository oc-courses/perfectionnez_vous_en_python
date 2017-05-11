from lxml import etree  

def get_report():
    
    report = """
        <CompteRendu>
            <MetaDonnees>
                <DateSeance>12 oct 2029</DateSeance>
            </MetaDonnees>
            <Contenu>
                <paragraphe>
                    <Orateur>
                        <NOM>Monsieur Gentil</NOM>
                    </Orateur>
                    <Texte>
                        Je suis gentil, et vous êtes méchant!
                    </Texte>
                </paragraphe>
                <paragraphe>
                    <Orateur>
                        <NOM>Monsieur Mechant</NOM>
                    </Orateur>
                    <Texte>
                        Je suis méchant oui, mais j'assume!
                    </Texte>
                </paragraphe>
            </Contenu>
            <UneAutreBalise>
                Blablabla 1
            </UneAutreBalise>
            <EncoreUneAutreBalise>
                Blablabla 2
                <br/>
                Blablabla 3
                <italic>
                    Blablabla 4
                </italic>
            </EncoreUneAutreBalise>
        </CompteRendu>
    """

    return report
       
def search():
        
    report_str = get_report()
    
    report = etree.XML(report_str)
        
    # A report should always have 2 children:
    # - a 'MetaDonnees' tag
    # - a 'Contenu' tag
    # In case it would contain more than these 2 children, we collect these
    # other parts in the list *other_parts (which will normally always be an empty list)
    metadata, content, *other_parts = report 
    
    print("Date : {}".format(metadata.find("DateSeance").text))
    
    for paragraph in content.iterchildren():
        speaker = paragraph[0]
        text = paragraph[1]
        
        print("-" * 80)
        print("New paragraph. Speaker : {}".format(speaker.find("NOM").text))
        print(text.text)
    
    print("-" * 80)
    
    for other_part in other_parts:
        print("Other parts were found :")
        for text in other_part.itertext():
            print(text)
    
        
if __name__ == '__main__': 
    search()