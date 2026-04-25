from flask import Flask, request, jsonify

app = Flask(__name__)


def _get_json_body():
    data = request.get_json(silent=True)
    if data is None:
        return None, (jsonify({"error": "Request body must be valid JSON"}), 400)
    return data, None


@app.route("/echo", methods=["GET", "POST"])
def echo():
    data, err = _get_json_body()
    if err:
        return err
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
