from flask import Flask, jsonify, request
from hypothenuse import hypothenuse
from test_hypothenuse import TestHypothenuse
from speed import TestSpeed, speed
from flask_cors import CORS, cross_origin
import unittest

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return 'Hello, World!'

#region Hypothenuse
@app.route('/hypothenuse', endpoint=' calculate_hypothenuse')
def calculate_hypothenuse():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    th = TestHypothenuse()
    test_methods = [name for name in dir(th) if name.startswith('test_hypothenuse')]
    
    for test_name in test_methods:
        test_method = getattr(th, test_name)
        try:
            test_method()
            print(f'{test_name}: PASS')
        except AssertionError:
            return f'{test_name}: FAIL', 400
        except Exception as e:
            return f'{test_name}: ERROR: {str(e)}', 400

    return f'The hypothenuse is: {hypothenuse(a, b)}'

@app.route('/hypothenuse/test/<int:test_number>', endpoint='hypothenuse_test')
def test_hypothenuse(test_number):
    th = TestHypothenuse()
    test_methods = [name for name in dir(th) if name.startswith('test_hypothenuse_route')]
    
    if 0 < test_number <= len(test_methods):
        test_name = test_methods[test_number - 1]
        test_method = getattr(th, test_name)
        
        try:
            test_method()
            return f'{test_name}: PASS'
        except AssertionError:
            return f'{test_name}: FAIL'
        except Exception as e:
            return f'{test_name}: ERROR: {str(e)}'
    else:
        return 'Invalid test number', 404
#endregion

#region Speed
@cross_origin
@app.route('/speed')
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

@cross_origin
@app.route('/speed/tests')
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