from flask import Flask, render_template, request
from ai_helper import get_visa_guidance   # this is your scaledown + groq file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        country = request.form.get("country")
        visa_type = request.form.get("visa_type")
        profile = request.form.get("profile")

        # validation
        if not country or not visa_type or not profile:
            result = "⚠️ Please fill all fields."
        else:
            result = get_visa_guidance(country, visa_type, profile)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
