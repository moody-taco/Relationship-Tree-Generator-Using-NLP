import spacy
from spacy import displacy
from spacy.training import Example
from spacy.util import minibatch, compounding

text = "John and Jerry are cousins with Jacob and Jack. Jack is the brother of Jacob. John is married to Jane. Jane is the mother of Emily"

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Split the string into different sentences
doc = nlp(text)
sentences = list(doc.sents)
print("NER output: ")
displacy.render(doc, style="ent", jupyter=True)

# Extract the Names of persons present in each sentence
for sentence in sentences:
    print("\n\t", sentence)
    persons = []
    for ent in sentence.ents:
       if ent.label_ == 'PERSON':
         persons.append(ent.text)
    if persons:
        print("\t>>> Persons in the sentence: ", persons)

# Load an existing Spacy NER model
nlp = spacy.load("en_core_web_sm")

# Add a new label to the NER model
ner = nlp.get_pipe('ner')
ner.add_label('Relationship')

# Annotate training data with the custom label
train_data = [
    ('John is the father of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('Mary is the mother of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('John is the son of Sarah.', {'entities': [(12, 15, 'Relationship')]}),
    ('Mary is the daughter of Sarah.', {'entities': [(12, 20, 'Relationship')]}),
    ('John is the brother of Sarah.', {'entities': [(12, 19, 'Relationship')]}),
    ('Mary is the sister of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('John is the sibling of Sarah.', {'entities': [(12, 19, 'Relationship')]}),
    ('John is the grandfather of Sarah.', {'entities': [(12, 23, 'Relationship')]}),
    ('Anna is the grandmother of Sarah.', {'entities': [(12, 23, 'Relationship')]}),
    ('John is the grandson of Sarah.', {'entities': [(12, 20, 'Relationship')]}),
    ('Katy is the granddaughter of Sarah.', {'entities': [(12, 25, 'Relationship')]}),
    ('John is the uncle of Sarah.', {'entities': [(12, 17, 'Relationship')]}),
    ('Mary is the aunt of Sarah.', {'entities': [(12, 16, 'Relationship')]}),
    ('John is the nephew of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('Mary is the niece of Sarah.', {'entities': [(12, 17, 'Relationship')]}),
    ('John is the cousin of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('John is the husband of Sarah.', {'entities': [(12, 19, 'Relationship')]}),
    ('Mary is the wife of John.', {'entities': [(12, 16, 'Relationship')]}),
    ('John is the Sarah\'s partner.', {'entities': [(20, 27, 'Relationship')]}),
    ('John is the fiance of Sarah.', {'entities': [(12, 18, 'Relationship')]}),
    ('John is married to Sarah.', {'entities': [(8, 15, 'Relationship')]}),
    ('John is the parent of Sarah.', {'entities': [(12, 18, 'Relationship')]})
]

optimizer = nlp.resume_training()
n_iter = 10
batch_size = 4

# Train the model
for i in range(n_iter):
    losses = {}
    batches = minibatch(train_data, size=compounding(batch_size, 32, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        examples = [Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in zip(texts, annotations)]
        nlp.update(examples, sgd=optimizer, losses=losses)
    print(f'Iteration {i}: Losses: {losses}')


# Access the NER component and print the labels
ner = nlp.get_pipe('ner')
labels = ner.labels
print(labels)

doc = nlp(text)
displacy.render(doc, style="ent", jupyter=True)