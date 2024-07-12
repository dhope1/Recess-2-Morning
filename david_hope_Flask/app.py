from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


# Create WildConservation Species list

species_list = [
    {"species_name": "Elephant", "habitat": "Africa"},
    {"species_name": "Lion", "habitat": "Africa"},
    {"species_name": "Giraffe", "habitat": "Africa"},
    {"species_name": "Tiger", "habitat": "Africa"},
    {"species_name": "Bat", "habitat": "Africa"},
    {"species_name": "Penguin", "habitat": "Africa"},
    {"species_name": "Seal", "habitat": "Antarctica"},
    {"species_name": "Eagle", "habitat": "Antarctica"},
    {"species_name": "Falcon", "habitat": "Antarctica"},
    {"species_name": "Ostrich", "habitat": "Antarctica"},
]


@app.route("/")  # decorator that maps url to index functions
def index():
    return render_template("index.html", species_list=species_list)


@app.route("/add", methods=["GET", "POST"])
def add_species():
    if request.method == "POST":
        species_name = request.form["species_name"]
        habitat = request.form["habitat"]
        species_list.append({"species_name": species_name, "habitat": habitat})
        return redirect(url_for("index"))
    return render_template("add_species.html")


if __name__ == "__main__":
    app.run(debug=True)
