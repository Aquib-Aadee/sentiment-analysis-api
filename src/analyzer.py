from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes the sentiment of a given text string.
    Returns a dictionary with the polarity score and human-readable sentiment.
    """
    # TextBlob processes the linguistic structure of the text
    blob = TextBlob(text)
    
    # Polarity is a mathematical score from -1.0 (very negative) to 1.0 (very positive)
    polarity = blob.sentiment.polarity
    
    # Translate the math into a category
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return {
        "text": text,
        "polarity": round(polarity, 2),
        "sentiment": sentiment
    }