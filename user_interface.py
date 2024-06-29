import numpy as np
import pandas as pd
import requests
import streamlit as st
import torch
import torch.nn.functional as F
from PIL import Image, ImageFile
from transformers import logging

ImageFile.LOAD_TRUNCATED_IMAGES = True
logging.set_verbosity_error()

from embaddings.encoder import BERTEncoder

media_df = pd.read_parquet("./data/media_cleaned.pqt")
encoder = BERTEncoder(embed_method="cls")
embeddings = torch.load("./data/media_hebrew_embeddings.pt")


# Your image search function here
def search_images(
    query: str,
    encoder: BERTEncoder,
    embeddings: torch.Tensor,
    data: pd.DataFrame,
    threshold: float,
) -> pd.Series:

    sentence_embedding = encoder.get_embedding(query).to(torch.float16)
    similarities = F.cosine_similarity(sentence_embedding, embeddings).numpy()

    cond = similarities > threshold
    results = data.loc[cond, ["url", "tags"]].copy()
    results["similarity"] = similarities[cond]

    results = results.sort_values("similarity", ascending=False)

    return results


def image_from_url(url: str):
    img = Image.open(requests.get(url, stream=True).raw)
    return img.resize((img.width // 10, img.height // 10))


def main():
    results: pd.DataFrame
    # Set page title
    st.title("Kaleidoo Text-to-Image Search Engine 📸🔍")

    # Text input for search query
    query = st.text_input("Enter your search query:", key="search_input")

    # Slider for threshold
    threshold = st.slider(
        "Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.01
    )

    with st.form(key="search_form"):
        submit_button = st.form_submit_button(label="Search")

    if (
        submit_button or query
    ):  # This condition checks for both button click and Enter key
        results = search_images(query, encoder, embeddings, media_df, threshold)

        if not results.empty:
            # Display results in a grid
            cols = st.columns(3)
            for idx, result in enumerate(results.itertuples()):
                with cols[idx % 3]:
                    img = image_from_url(result.url)
                    st.image(
                        img,
                        use_column_width=True,
                        caption=f"Similarity: {result.similarity:.2f}\nTags: {', '.join(result.tags)}",
                    )
        else:
            st.error("No results found")


if __name__ == "__main__":
    main()
