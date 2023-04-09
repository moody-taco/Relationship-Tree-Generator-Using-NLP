import csv
import spacy
import pandas as pd
from IPython.display import display, HTML

relationships = [
        'Father', 'Mother', 'Son', 'Daughter', 'Brother', 'Sister', 'Sibling', 
        'Grandfather', 'Grandmother', 'Grandson', 'Granddaughter',
        'Uncle', 'Aunt', 'Nephew', 'Niece', 'Cousin', 'Husband', 'Wife',
        'Partner', 'Fiance', 'Married', 'Parent'
    ]

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Define the function to extract the names
def extract_names(text):
    global superdf
    # Parse the text with spaCy
    doc = nlp(text)
    
    # Loop through each sentence in the text
    for sent in doc.sents:
        sentence = sent.text.strip()
        sent_names = []
        sent_positions = []
        names_and = []
        df = pd.DataFrame(columns=['Member1', 'Member2', 'Relationship'])
        member1 = []
        member2 = []
        relation = []
        a = 0
        flag = 0
        

        # Loop through each token in the sentence
        for i, token in enumerate(sent):
            # Check if the token is a proper noun and its title is capitalized
            for rel in relationships:
                if rel.lower() in token.text.lower():
                    relation.append(rel)
                    flag = 1
            if token.pos_ == "PROPN" and token.text.istitle():
                # Add the name to the list of names and its position to the list of positions
                sent_names.append(token.text)
                a = a+1
                sent_positions.append(str(i+1))

                if flag == 0:
                  member1.append(token.text)
                else:
                  member2.append(token.text)

                # Find the names that are separated by "and"
                if a > 1 and (sent_names[a-2]+" and " + sent_names[a-1] in sentence):
                    names_and.append(sent_names[a-2])
                    names_and.append(sent_names[a-1])
        
        for mem1 in member1:
          for mem2 in member2:
            temp = [mem1, mem2, relation[-1]]
            df.loc[len(df.index)] = temp 
          
        # Merge all the dataframes:
        frames = [superdf, df]
        superdf = pd.concat(frames, ignore_index=True)

        # If names were found in the sentence, print them along with the sentence and their positions
        if sent_names:
            print(f"Sentence: {sentence}")
            print(f"Names: {', '.join(sent_names)}")
            print(f"Names separated by and: {', '.join(names_and)}")
            print(f"Relations: {', '.join(relation)}")
            print(f"Position: {', '.join(sent_positions)}\n")
            display(df)

text = "John and Jerry are cousins with Jacob and Jack. Jack is the brother of Jacob. John is married to Jane. Jane is the mother of Emily"
superdf = pd.DataFrame(columns=['Member1', 'Member2', 'Relationship'])
extract_names(text)

display(superdf)
# saving the dataframe
superdf.to_csv('family_tree.csv', index = False)