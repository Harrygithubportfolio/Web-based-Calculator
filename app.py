from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            expression = request.form.get("expression")
            result = eval(expression)
        except Exception as e:
            result = "Error"
        return render_template("calculator.html", result=result, expression=expression)

    return render_template("calculator.html", result=None, expression="")

if __name__ == "__main__":
    app.run(debug=True)
