from flask import Flask , request 
from flask_restful import Resource , Api, reqparse 
import json , time 

app = Flask (__name__) 
api = Api(app)
 
parser = reqparse.RequestParser() 
parser.add_argument('date')
parser.add_argument('age')
 
class day(Resource): 
	def post(self): 
		args = parser.parse_args() 
		date = args['date'] 
		age = args['age'] 
		return {"birthdate":date,"Age":age} 
api.add_resource(day,'/birthdate') 

if __name__ == '__main__': 
	app.run(host='0.0.0.0',port=5500)
