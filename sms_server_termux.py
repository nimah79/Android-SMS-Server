#!flask/bin/python

'''
Android SMS server
Termux version
By NimaH79
NimaH79.ir
'''

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
import os

app = Flask(__name__, static_url_path='')
api = Api(app)


class sendSms(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'phone',
            type=str,
            required=True,
            help='No phone number provided')
        self.reqparse.add_argument(
            'text',
            type=str,
            required=True,
            help='No text provided')
        super(sendSms, self).__init__()

    def get(self):
        return {'message': 'you should use POST method'}, 405

    def post(self):
        args = self.reqparse.parse_args()
        os.system('termux-sms-send -n ' + args['phone'] + ' ' + args['text'])
        return {'message': 'success'}


api.add_resource(sendSms, '/sendSMS', endpoint='sendSMS')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
