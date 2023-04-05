from flask import Flask, jsonify, request
from hypothenuse import TestHypothenuse, hypothenuse
from flask_cors import CORS, cross_origin
from speed import TestSpeed, speed
import unittest

app = Flask(__name__)

CORS(app)

@app.route('/')
@cross_origin
def index():
    return 'Hello, World!'

#region Hypothenuse
@app.route('/hypothenuse')
@cross_origin
def calculate_hypothenuse():
    a = request.args.get('a', default=3, type=float)
    b = request.args.get('b', default=4, type=float)

    isJson = request.args.get('isJson', default=False, type=lambda v: v.lower() == 'true')

    if isJson:
        return jsonify({
            'a': a,
            'b': b,
            'hypothenuse': hypothenuse(a, b)
        })
    else:
        return f'The hypothenuse is: {hypothenuse(a, b)}'


@app.route('/hypothenuse/test')
@cross_origin
def test_hypothenuse():
    th = TestHypothenuse()
    results = {}
    for name in dir(th):
        if name.startswith('test_hypothenuse'):
            try:
                getattr(th, name)()
                results[name] = 'PASS'
            except AssertionError:
                results[name] = 'FAIL'
            except Exception as e:
                results[name] = 'ERROR: ' + str(e)
    return jsonify(results)
#endregion



#region Speed
@app.route('/speed')
@cross_origin
def calculate_speed():
    gravity = request.args.get('gravity', default=9.81, type=float)
    height = request.args.get('height', default=10, type=float)

    isJson = request.args.get('isJson', default=False, type=lambda v: v.lower() == 'true')

    if isJson:
        return jsonify({
            'gravity': gravity,
            'height': height,
            'speedInMeters': speed(gravity, height),
            'speedInKilometers': speed(gravity, height) * 3.6,
        })
    else:
        return f'The speed is: {speed(gravity, height)}'

@app.route('/speed/tests')
@cross_origin
def test_speed():
    ts = TestSpeed()
    results = {}
    for name in dir(ts):
        if name.startswith('test_speed'):
            try:
                getattr(ts, name)()
                results[name] = 'PASS'
            except AssertionError:
                results[name] = 'FAIL'
            except Exception as e:
                results[name] = 'ERROR: ' + str(e)
    return jsonify(results)
#endregion

if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/speed/tests')
# def run_speed_tests():
#     ts = TestSpeed()
#     speedLoader = unittest.TestLoader().loadTestsFromModule(ts)
#     speedResults = unittest.TextTestRunner(verbosity=2).run(speedLoader)
#     return str(speedResults)