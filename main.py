#  (C) Copyright  2024 DigitalLab.  Confidential computer software.
#  Valid license from DigitalLab required for possession, use or copying.
#  Consistent with FAR 12.211 and 12.212, Commercial Computer Software,
#  Computer Software Documentation, and Technical Data for Commercial Items are
#  licensed to the U.S. Government under vendor's standard commercial license.

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
