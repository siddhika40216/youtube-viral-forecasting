# YouTube Viral Video Forecasting

A machine learning project that predicts whether a YouTube video is likely to become viral based on its early performance, publishing information, and basic video metadata.

## Project Overview

The project uses historical YouTube trending data to study the relationship between a video's early performance and its eventual view count.

For each video, the first available trending record is used as the early performance information. The maximum views reached by that video in the available dataset are then used to define the final outcome.

Videos falling in the top 25% based on maximum views are labelled as **Viral**.

The project includes data preprocessing, feature engineering, machine learning model comparison, and a Flask-based web application for prediction.

## Dataset

The project uses the US YouTube Trending Videos dataset.

Files used:

- `USvideos.csv`
- `US_category_id.json`

The dataset contains information about:

- Video ID
- Trending date
- Publishing time
- Category
- Views
- Likes
- Dislikes
- Comments
- Title
- Tags
- Video status

## Project Workflow

1. Load and clean the YouTube trending dataset.
2. Convert date and time columns into usable features.
3. Group records by `video_id`.
4. Select the first trending record as the early performance snapshot.
5. Find the maximum views reached by each video.
6. Define the top 25% of videos by maximum views as viral.
7. Create engagement and metadata features.
8. Train multiple classification models.
9. Compare the models using evaluation metrics.
10. Save the selected model.
11. Use the trained model through a Flask web application.

## Features Used

The final model uses:

- Current views
- Current likes
- Current comments
- Like rate
- Comment rate
- Engagement rate
- Category ID
- Publishing hour
- Publishing day
- Publishing month
- Comments disabled
- Ratings disabled
- Video error or removed
- Title length
- Number of tags

The rate-based features are calculated automatically from the views, likes, and comments provided by the user.

## Machine Learning Models

The following classification models were trained and compared:

- Logistic Regression
- Random Forest
- Gradient Boosting

The final model is selected based on F1 Score on the test dataset.

## Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The detailed evaluation and model comparison are available in the notebook.

## Web Application

The project includes a Flask web application with an HTML, CSS, and JavaScript frontend.

The user provides:

- Current views
- Current likes
- Current comments
- Category
- Publishing information
- Title length
- Number of tags
- Video settings

The application calculates the required derived features and sends them to the trained machine learning model.

The result displays:

- Prediction: Viral / Not Viral
- Viral probability

## Project Structure

```text
youtube-viral-forecasting/
│
├── data/
│   ├── USvideos.csv
│   └── US_category_id.json
│
├── models/
│   ├── viral_video_model.pkl
│   └── features.pkl
│
├── notebooks/
│   └── data_understanding.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

```
## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- HTML
- CSS
- JavaScript
- Joblib

## How to Run

### 1. Clone the repository

```bash
git clone < https://github.com/siddhika40216/youtube-viral-forecasting >
cd youtube-viral-forecasting
```
### 2. Install the required packages

pip install -r requirements.txt

### 3. Run the Flask application

python app.py

### 4. Open the application

Open the following address in your browser:
http://127.0.0.1:5000


## Limitations

The project is based on historical US YouTube trending data, so the model learns patterns present in that dataset.

The viral label is defined using the top 25% of maximum views in the dataset. Therefore, the prediction represents the project's definition of virality and should not be interpreted as an exact prediction of future views.

## Future Improvements

- Use newer YouTube datasets.
- Include additional early engagement signals.
- Experiment with time-based train/test splitting.
- Use more detailed category information.
- Add more analysis to the prediction results.

## Contributions

Contributions to this project are welcome. If you find any issues or have any suggestions for improvement, please open an issue or a pull request on this repository.
