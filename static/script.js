document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const data = {

            views: Number(
                document.getElementById("views").value
            ),

            likes: Number(
                document.getElementById("likes").value
            ),

            comments: Number(
                document.getElementById("comments").value
            ),

            category_id: Number(
                document.getElementById("category_id").value
            ),

            publish_hour: Number(
                document.getElementById("publish_hour").value
            ),

            publish_day: Number(
                document.getElementById("publish_day").value
            ),

            publish_month: Number(
                document.getElementById("publish_month").value
            ),

            title_length: Number(
                document.getElementById("title_length").value
            ),

            tag_count: Number(
                document.getElementById("tag_count").value
            ),

            comments_disabled:
                document.getElementById(
                    "comments_disabled"
                ).checked,

            ratings_disabled:
                document.getElementById(
                    "ratings_disabled"
                ).checked,

            video_error_or_removed:
                document.getElementById(
                    "video_error_or_removed"
                ).checked
        };

        try {

            const response = await fetch(
                "/predict",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(data)
                }
            );

            const result = await response.json();

            const resultBox =
                document.getElementById("result");

            const predictionText =
                document.getElementById("predictionText");

            const probability =
                document.getElementById("probability");

            resultBox.classList.remove("hidden");

            predictionText.textContent =
                "Prediction: " + result.prediction;

            probability.textContent =
                result.probability + "%";
            const progressBar =
            document.getElementById("progressBar");

            progressBar.style.width =
            result.probability + "%";

        } catch (error) {

            alert(
                "Something went wrong. Please make sure the Flask server is running."
            );

        }

    });