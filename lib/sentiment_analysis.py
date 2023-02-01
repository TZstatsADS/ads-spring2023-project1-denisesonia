def Sentiment_Analysis(sentence):
    sentAnalyzer = SentimentIntensityAnalyzer() 
    sentiment = sentAnalyzer.polarity_scores(sentence)
    if sentiment['compound'] >= 0.05:
        return "positive"
    elif sentiment['compound'] <= -0.05 :
        return "negative"
    else:
        return "neutral"