# Relationship-Tree-Generator-Using-NLP
This project takes a simple sentence as an input and generates a relationship tree based on the mentioned relationships in the string.

## Running the code:
The code is split into TWO main parts: NLP and Visualization. To run the code, we can just excute each cell in order and it should work. make sure to pip install all the mentioned packages.

## Potential Alternative:
Since I was unaware of the NER in Spacy, I added it later to the code. From my observation it is a very powerful tool and can be super beneficial in this project.
I tried to train it on my relationships dataset but it would misclassify data. I have done some basi operation to lay the foundation if someone wants to improve on this method.

## Limitations:
> The dataset is very limited but since it is a list, it can be easily updated.
> Problems with the main approach are that it cannot handle compound sentences very well and it takes any proper noun as a name of a person.
> Observable limitations of the NER approach were that it had a very limited number of names and it misclassified the custom trained label
