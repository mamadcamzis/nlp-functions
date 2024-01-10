import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize wikipedia"""
    print(f"Finding any  wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Gets text blob object and returns"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and return back phrases"""
    text = search_wikipedia(name)
    summary = summarize_wikipedia(text)
    blob = get_text_blob(summary)
    phrases = blob.noun_phrases
    return phrases
