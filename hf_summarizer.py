#pip install transformers torch huggingface_hub
from transformers import pipeline # type: ignore

summarizer = pipeline("summarization")
