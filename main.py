# represent Hebrew sentences as embeddings
# using the Hebrew BERT model

# then, given a sentence and a threshold, find the most similar sentences

import torch
import torch.nn.functional as F
from transformers import BertModel, BertTokenizerFast

alephbert_tokenizer = BertTokenizerFast.from_pretrained('onlplab/alephbert-base')
alephbert = BertModel.from_pretrained('onlplab/alephbert-base')

alephbert.eval()

# get the embeddings of a sentence
def get_embedding(sentence):
    tokens = alephbert_tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        output = alephbert(**tokens)
    embeddings = output.last_hidden_state.mean(dim=1)
    return embeddings

# get the similarity between two embeddings
def get_similarity(embedding1, embedding2):
    return F.cosine_similarity(embedding1, embedding2).item()

# get the most similar sentences to a given sentence
def get_most_similar_sentences(sentence, sentences, threshold):
    sentence_embedding = get_embedding(sentence)
    similar_sentences = []
    for s in sentences:
        embedding = get_embedding(s)
        similarity = get_similarity(sentence_embedding, embedding)
        if similarity > threshold:
            similar_sentences.append((s, similarity))
    return similar_sentences

# example

sentences = [
    "הכלב רץ בגינה",
    "החתול ישן על הספה",
    "הכלב והחתול ישנים על הספה",
    "הכלב רואה את החתול",
    "החתול רואה את הכלב"
]

sentence = "החתול רץ בגינה"

threshold = 0.5

similar_sentences = get_most_similar_sentences(sentence, sentences, threshold)

for s, similarity in similar_sentences:
    print(f"{s} - similarity: {similarity}")
