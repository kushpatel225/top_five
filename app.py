from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for submissions
submissions = []

@app.route("/", methods=["GET", "POST"])
def home():
    global submissions
    if request.method == "POST":
        category = request.form.get("category", "").strip()
        items = [request.form.get(f"item{i}", "").strip() for i in range(1, 6)]

        if category and all(items):
            submissions.append({"category": category, "five": items})
        return redirect("/")
    return render_template("index.html", submissions=submissions)


# Used ChatGPT to help write this code
# Code to edit a submission
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_submission(index):
    global submissions

    if index < 0 or index >= len(submissions):
        return "Invalid submission index", 404

    if request.method == "POST":
        category = request.form.get("category", "").strip()
        items = [request.form.get(f"item{i}", "").strip() for i in range(1, 6)]

        if category and all(items):
            submissions[index] = {"category": category, "five": items}
        return redirect("/")

    return render_template("edit.html", submission=submissions[index], index=index)


if __name__ == "__main__":
    app.run(debug=True)
