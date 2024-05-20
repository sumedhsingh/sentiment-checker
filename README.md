# Sentiment Analysis Checker
This project utilizes Streamlit, a Python library for building interactive web applications, and the Cohere API for sentiment analysis. It allows users to input text and receive sentiment analysis results in real-time.

# Streamlit
Streamlit is an open-source Python library that makes it easy to create web applications for machine learning and data science projects. It allows developers to build interactive and visually appealing applications using simple Python scripts.

# Cohere API
I integrated the Cohere API for sentiment analysis because it provides powerful natural language processing capabilities. With Cohere, I can analyze the sentiment of text inputs in real-time, categorizing them as positive, negative, or neutral. It's a straightforward and effective way to add sentiment analysis features to my project.

# Sentiment Analysis Checker
The sentiment analysis checker built in this project utilizes the Cohere API to analyze the sentiment of text inputs. Users can enter any text, and the application will provide sentiment analysis results, categorizing the input as positive, negative, or neutral.

# Running the Program
To run the program, follow these steps:

1. Clone the Repository:

    ```
    git clone https://github.com/sumedhsingh/sentiment-checker.git

    cd sentiment-checker
    ```

2. Create and Activate the Virtual Environment (Optional):

   If you prefer to run the program in a virtual environment:
     ```
      python -m venv venv
    
      source venv/bin/activate   # On macOS/Linux
    
      .\venv\Scripts\activate    # On Windows
     ```

3. Install Dependencies:

   ```
    pip install -r requirements.txt
   ```

4. Run the Streamlit App:

   ```
    streamlit run app.py
   ```

5. Access the Application:

Open a web browser and navigate to ```http://localhost:8501``` to access the Sentiment Analysis Checker.

