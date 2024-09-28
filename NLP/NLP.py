import nltk
import pandas as pd

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
path = "/home/krish/Documents/Programming Languages/Python/NLP/twitter_data.csv"
df = pd.read_csv(path,encoding='latin-1')
df.head()