"""Represent Hebrew sentences as embeddings
using the Hebrew BERT model
then, given a sentence and a threshold, find the most similar sentences
"""

import torch
import torch.nn.functional as F
from transformers import BertModel, BertTokenizerFast


class BERTEncoder:
    def __init__(self, model_name="onlplab/alephbert-base", embed_method="mean"):
        self.embed_method = embed_method
        self.tokenizer = BertTokenizerFast.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.model.eval()

    def get_embedding(self, sentence):
        tokens = self.tokenizer(
            sentence, return_tensors="pt", padding=True, truncation=True
        )

        with torch.no_grad():
            output = self.model(**tokens)

            if self.embed_method == "mean":
                embeddings = output.last_hidden_state.mean(dim=1)
            elif self.embed_method == "cls":
                embeddings = output.last_hidden_state[:, 0, :]
            else:
                raise ValueError("method should be 'mean' or 'cls'")

        return embeddings

    def get_similarity(self, embedding1, embedding2):
        return F.cosine_similarity(embedding1, embedding2).item()

    def get_most_similar_sentences(self, sentence, sentences, threshold):
        sentence_embedding = self.get_embedding(sentence)
        embedding = self.get_embedding(sentences)

        # calculate similarity
        similarities = F.cosine_similarity(sentence_embedding, embedding).numpy()

        # filter by threshold
        similar_sentences = (
            (s, sim) for s, sim in zip(sentences, similarities) if sim > threshold
        )

        return similar_sentences


def example():

    encoder = BERTEncoder(embed_method="cls")

    sentences = [
        "הכלב רץ בגינה",
        "החתול ישן על הספה",
        "הכלב והחתול ישנים על הספה",
        "הכלב רואה את החתול",
        "החתול רואה את הכלב",
    ]

    # test very long sentence
    long_sentence = "החתול רץ בגינה והכלב רואה אותו ומתחיל לרדוף אחריו ואז החתול קופץ על העץ והכלב נשאר מתחת לעץ ומשם החתול רואה את הכלב ומתחיל לצחוק עליו ואז הכלב מבין שהוא נתפס ומתחיל לנבות ולהתלונן ואז החתול קופץ מהעץ ונמלט מהכלב והכלב נשאר מתוסכל ומתבוכח ומתחיל לרדוף אחרי החתול והחתול מתחיל לרוץ ולרוץ ולרוץ והכלב מאחוריו וכך הם רצים ורצים עד שהם מתעייפים ונפלים מהרצפה"
    sentences.append(long_sentence)

    sentence = "החתול רץ בגינה"

    threshold = 0.5

    similar_sentences = encoder.get_most_similar_sentences(
        sentence, sentences, threshold
    )

    for s, similarity in similar_sentences:
        print(f"{s} - similarity: {similarity}")


if __name__ == "__main__":
    example()
