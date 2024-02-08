import re
import nltk
import numpy as np
import pickle
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def clean_data(text):
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    text = re.sub(r'http\S+', '', text) # removing links
    text = re.sub(r'\\n', ' ', text) # removing \\n
    text = re.sub(r"\s*#\S+", "", text) # removing hash tags
    text = re.sub(r"\s*@\S+", "", text) # removing @
    text = text.lower()
    text = text.split()

    text = [lemmatizer.lemmatize(word) for word in text if word not in stopwords.words('english')]
    text = ' '.join(text)
    return text


model_in = open("classifier.pkl","rb")
classifier=pickle.load(model_in)

scaler_in = open("scaler.pkl","rb")
bog = pickle.load(scaler_in)

laber_in = open("le.pkl","rb")
le = pickle.load(laber_in)

def predict_user_input(tweet):
    cleaned_data = clean_data(tweet)
    x = bog.transform([cleaned_data]).toarray()
    predicted_labels = classifier.predict(x)
    res =  le.classes_[predicted_labels]

    return res