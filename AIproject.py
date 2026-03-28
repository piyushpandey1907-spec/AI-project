import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# 1. Setup the Brain (VADER is specialized for social media/chat text)
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

class SentimentEngine:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        # Calculate the polarity scores
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']
        
        # Human-friendly logic for the final result
        if compound >= 0.05:
            res, emoji = "POSITIVE", "🟢"
        elif compound <= -0.05:
            res, emoji = "NEGATIVE", "🔴"
        else:
            res, emoji = "NEUTRAL ", "🟡"
            
        return res, emoji, compound

def main():
    engine = SentimentEngine()
    
    print("="*50)
    print("🤖 AI SENTIMENT ANALYZER (Type 'exit' to stop)")
    print("="*50)

    while True:
        user_input = input("\n💬 Enter text to analyze: ").strip()

        if user_input.lower() in ['exit', 'quit', 'stop']:
            print("\n👋 Goodbye! Project terminated.")
            break

        if not user_input:
            print("⚠️ Please enter some actual text.")
            continue

        # Process the input
        label, emoji, score = engine.get_sentiment(user_input)

        # Output formatting
        print(f"{'-'*50}")
        print(f"Result  : {emoji} {label}")
        print(f"Score   : {score:.4f} (Range: -1 to 1)")
        print(f"{'-'*50}")

if __name__ == "__main__":
    main()