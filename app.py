from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    "models/viral_video_model.pkl"
)

# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# PREDICTION API
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # User inputs
    views = float(data["views"])
    likes = float(data["likes"])
    comments = float(data["comments"])

    category_id = int(data["category_id"])
    publish_hour = int(data["publish_hour"])
    publish_day = int(data["publish_day"])
    publish_month = int(data["publish_month"])

    title_length = int(data["title_length"])
    tag_count = int(data["tag_count"])

    comments_disabled = bool(
        data["comments_disabled"]
    )

    ratings_disabled = bool(
        data["ratings_disabled"]
    )

    video_error = bool(
        data["video_error_or_removed"]
    )

    # =========================
    # CALCULATE FEATURES
    # =========================

    safe_views = max(views, 1)

    like_rate = likes / safe_views

    comment_rate = comments / safe_views

    engagement_rate = (
        likes + comments
    ) / safe_views

    # =========================
    # CREATE MODEL INPUT
    # =========================

    input_data = pd.DataFrame([{
        "views": views,
        "likes": likes,
        "comment_count": comments,
        "like_rate": like_rate,
        "comment_rate": comment_rate,
        "engagement_rate": engagement_rate,
        "category_id": category_id,
        "publish_hour": publish_hour,
        "publish_day": publish_day,
        "publish_month": publish_month,
        "comments_disabled": comments_disabled,
        "ratings_disabled": ratings_disabled,
        "video_error_or_removed": video_error,
        "title_length": title_length,
        "tag_count": tag_count
    }])

    # =========================
    # PREDICTION
    # =========================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    print("INPUT DATA:")
    print(input_data)

    print("PREDICTION:", prediction)
    print("PROBABILITY:", probability)

    result = "Viral" if prediction == 1 else "Not Viral"

    return jsonify({
        "prediction": result,
        "probability": round(
            probability * 100, 2
        )
    })


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(
        debug=True
    )