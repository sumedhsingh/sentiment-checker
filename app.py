import streamlit as st
import cohere

# Initialize Cohere Client
api_key = "dvECpWrMHpKEIaXvtqPBOsuNCmBFZ8wNiXLuZcZs"
co = cohere.Client(api_key)

# Define Sentiment Analysis Function using text generation
def analyze_sentiment(text):
    response = co.generate(
        model='command-xlarge-nightly',  # Replace with an appropriate model ID if needed
        prompt=f"Please classify the sentiment of the following text as Positive, Negative, or Neutral: '{text}'",
        max_tokens=10,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

# Streamlit App
st.title('Sentiment Analysis Tool')
st.write('Enter text to analyze its sentiment')

user_input = st.text_area("Enter your text here")

if st.button('Analyze Sentiment'):
    if user_input:
        sentiment = analyze_sentiment(user_input)
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write('Please enter some text to analyze')
