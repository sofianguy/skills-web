from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application")
def application():
	return render_template("application-form.html")

@app.route("/application-form", methods=["POST"])
def submit():
	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	job_type = request.form.get("jobtype")
	salary_req = request.form.get("salaryreq")

	return render_template("submit.html", firstname=first_name, lastname=last_name, jobtype=job_type, salaryreq=salary_req)

if __name__ == "__main__":
    app.run(debug=True)