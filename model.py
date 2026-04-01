import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("dataset.csv")

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X_vec = vectorizer.fit_transform(X)
model = LogisticRegression(class_weight='balanced')

model.fit(X_vec, y)

# SAVE BOTH
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained & saved")