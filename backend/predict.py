import sys
import joblib
import nltk
# Load the saved model
model = joblib.load('personality_model.pkl')

# Get the input text from Node.js
input_text = sys.argv[1]

# Preprocessing function
def preprocess_text(text):
    import re
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    nltk.download('stopwords')
    nltk.download('wordnet')
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    text = re.sub(r'\W', ' ', text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Preprocess input text
processed_text = preprocess_text(input_text)

# Make a prediction
prediction = model.predict([processed_text])

# Print the result (will be sent back to Node.js)
print(prediction[0])
