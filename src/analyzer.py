from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER analyzer once (it loads a better dictionary)
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes text using VADER, which is better at understanding 
    context and social media style language.
    """
    # Get the polarity scores
    scores = analyzer.polarity_scores(text)
    
    # VADER gives a 'compound' score from -1 (Most Negative) to +1 (Most Positive)
    polarity = scores['compound']
    
    # We can use stricter thresholds now because VADER is more sensitive
    if polarity >= 0.05:
        sentiment = "Positive"
    elif polarity <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return {
        "text": text,
        "polarity": polarity,
        "breakdown": scores, # VADER also shows us exactly how much pos/neg it found
        "sentiment": sentiment
    }