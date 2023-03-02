from flask import Flask, jsonify, render_template, request, flash
import model
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = "T0to_na_p4s_d0rm1"

@app.route("/", methods = ['GET'])
def home():
    return render_template('home.html')

def no_body(message):
    message = {
        "message" : message
    }
    return jsonify(message), 400

@app.route("/application", methods=["GET"])
def application():
    return render_template("application.html")

@app.route("/resultats", methods=["POST"])
def resultats():
    user_id = int(request.form["user_id"])
    filter_liked_items = "filter_liked_items" in request.form
    if "number_items" in request.form:
        number_items = int(request.form["number_items"])
    else:
        number_items = 5

    recommendations = model.recommend(user_id, number_items, filter_liked_items)
    recommendations = [int(i) for i in recommendations] 

    for n in recommendations:
        flash(n, "article")

    return render_template("resultats.html")

@app.route("/api", methods=["POST"])
def api():
    if not request.is_json:
        return no_body("Pas de fichier json dans le corps de la requête.")

    json_data = request.json
    if "user_id" not in json_data.keys():
        return no_body("Le corps de la requête n'a pas de champs 'user_id'.")

    user_id = json_data["user_id"]

    if "filter_liked_items" in json_data.keys():
        filter_liked_items = json_data["filter_liked_items"]
    else:
        filter_liked_items = False

    if "number_items" in json_data.keys():
        number_items = json_data["number_items"]
    else:
        number_items = 5


    recommendations = model.recommend(user_id, number_items, filter_liked_items)
    recommendations = [int(i) for i in recommendations] 

    return jsonify({"ids" : recommendations})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))