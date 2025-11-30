# python-sentiment-analysis
Objectives
The primary goal of this task was to apply fundamental Natural Language Processing (NLP) techniques to unstructured text data to extract meaningful insights regarding public opinion or sentiment.

Preprocess Text Data: Implement a robust text cleaning pipeline, including tokenization, stopword removal, and the linguistic reduction technique of lemmatization, to prepare raw text for analysis.

Perform Sentiment Analysis: Use the TextBlob library to compute quantitative sentiment metrics (Polarity and Subjectivity) for each text entry.

Categorize and Visualize Results: Classify the computed polarity scores into qualitative sentiment categories (Positive, Neutral, Negative) and present the distribution and word frequencies clearly using graphical methods.

Tools and Libraries
This project was developed using Python 3.x and relies on the following core libraries:

pandas: For efficient data handling, loading the CSV file, and structuring the processed results.

nltk (Natural Language Toolkit): Used extensively for text preprocessing, including Tokenization, Stopword Removal, and Lemmatization.

TextBlob: The primary tool for executing Sentiment Analysis, providing polarity and subjectivity scores.

matplotlib & seaborn: Used to generate the Sentiment Distribution bar chart.

wordcloud: Used to generate the visual representation of Word Frequencies



How to Run the
CodeFollow these steps to set up and execute the project code:Clone the Repository:Bashgit clone https://github.com/moradiyazeel-byte/python-sentiment-analysis
cd python-sentiment-analysis
Install Dependencies: Ensure you have Python installed, then install the required libraries:Bashpip install pandas nltk textblob matplotlib seaborn wordcloud
Download NLTK Resources: Open a Python interpreter or run the script once to download necessary NLTK data:Pythonimport nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
Execute the Script: Run the main analysis file (task_3.py). The script reads the data, performs the analysis, and displays the final visualizations (the bar chart and the word cloud).Bashpython task_3.py
📈 Key FindingsThe sentiment analysis provided a clear picture of the overall opinion contained within the sample data.Sentiment CategoryPolarity RangeCount (Example)Percentage (Example)Positive$> 0.1$440%Neutral$-0.1 \le \text{Polarity} \le 0.1$220%Negative$< -0.1$440%Sentiment Distribution: The data exhibited a relatively balanced mix of sentiment, with an equal number of positive and negative texts, indicating polarization within the feedback.Impact of Preprocessing: The use of Lemmatization successfully standardized words like "running," "runs," and "ran" to their base form "run," which ensures accurate word counting and analysis.High-Frequency Terms: The Word Cloud visualization highlighted key terms driving the sentiment, such as 'brilliant,' 'terrible,' 'easy,' and 'waste,' confirming the effectiveness of the stopword removal process.
