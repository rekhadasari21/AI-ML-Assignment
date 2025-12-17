@app.route("/greet",methods=["POST"])
def greet_user():
    data=request.get_json()

    if not data or"name" not in data:
        return jsonify({
            "error":"Please provide a name in JSON format"
        }), 400

    name=data["name"]

    return jsonify({
        "message":f"Hello,{name}"
    }),200
