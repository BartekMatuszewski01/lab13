from textblob import TextBlob


def hello(name: str):
    return f"Hello {name}"


def extractc_sentiment(text: str):
    text = TextBlob(text)

    return text.sentiment.polarity


def contain_word(word: str, text: str) -> bool:
    return word in text

