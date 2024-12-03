from flask import Flask, render_template, request, jsonify
import pandas as pd
import nltk

app = Flask(__name__)

# Load and preprocess the data
df = pd.read_csv('data/combined_glassdoor_job_reviews.csv')
# You could add additional preprocessing here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    job_title = request.form['job_title']
    location = request.form['location']
    review_query = request.form['review_query']

    # Filter job titles and locations first
    results = df[(df['job_title'].str.contains(job_title, case=False)) &
                 (df['location'].str.contains(location, case=False))]

    # More filter, if providing more information from reviews
    if review_query:
        results = results[(results['pros_clean'].str.contains(review_query, case=False)) |
                          (results['cons_clean'].str.contains(review_query, case=False))]

    return render_template('results.html', results=results.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)