import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load both datasets
df1 = pd.read_csv('data/glassdoor_job_reviews_1.csv')  # Update with your actual file name
df2 = pd.read_csv('data/glassdoor_job_reviews_2.csv')

# Combine the datasets (assuming they have the same structure)
combined_df = pd.concat([df1, df2], ignore_index=True)

# Drop duplicate entries if there are any
combined_df.drop_duplicates(inplace=True)

# Save the combined dataset
combined_df.to_csv('data/combined_glassdoor_job_reviews.csv', index=False)

# Drop rows with missing values in important columns
df.dropna(subset=['pros', 'cons', 'company_name', 'job_title'], inplace=True)

# Example of text preprocessing
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [w for w in tokens if w.isalnum() and w not in stop_words]
    return " ".join(filtered_tokens)

# Apply preprocessing to 'pros' and 'cons'
df['pros_clean'] = df['pros'].apply(preprocess_text)
df['cons_clean'] = df['cons'].apply(preprocess_text)

# Save the cleaned dataset for further use
df.to_csv('data/cleaned_glassdoor_job_reviews.csv', index=False)

