flask-lambda-support
====================

Write Flask applications that support being run in in AWS Lambda behind API Gateway.

This project was forked from:
https://github.com/techjacker/flask-lambda

Improvements:

* Expose original input event from AWS on Flask's request object
* Production-grade logging


Requirements
------------

* Python 3.6+
* Flask 0.10+


Installation
------------

``pip install flask-lambda-support``


Usage
-----

Here is an example of what a Flask app using this library would look like:

.. code-block:: python

    from flask_lambda import FlaskLambda

    app = FlaskLambda(__name__)


    @app.route('/foo', methods=['GET', 'POST'])
    def foo():
       data = {
           'form': request.form.copy(),
           'args': request.args.copy(),
           'json': request.json
       }
       return (
           json.dumps(data, indent=4, sort_keys=True),
           200,
           {'Content-Type': 'application/json'}
       )


    if __name__ == '__main__':
        app.run(debug=True)

You can access the original input event on the Flask request context:

.. code-block:: python

    from flask import request

    assert request.aws_event['input']['httpMethod'] == 'POST'