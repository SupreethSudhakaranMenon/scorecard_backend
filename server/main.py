from flask import Flask, jsonify, request
import json
from flask import Response


# import flask_cors

from scorecard_backend.views.ConfigurationOperations import getByConfigId, getAllConfigurationFromDB, saveAConfiguration
from scorecard_backend.views.CriteriaOperations import getByCriteriaId, getAllCriteriaFromDB, saveCriteria
from scorecard_backend.views.FeatureOperations import getByFeatureId, getAllFeaturesFromDB, saveAFeature

app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resources={r"/feature/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'Hello World'
#
# Feature
# operations
@app.route('/feature/getByFeatureId', methods=['POST'])
def getSingleFeature():
    return json.dumps(getByFeatureId(int(request.json['id'])).__dict__), 200, {'ContentType': 'application/json'}
    # return Response(json.dumps(getByFeatureId(int(request.json['id'])).__dict__), mimetype='application/json')

@app.route('/feature/getAllFeatures')
def getAllFeatures():
    return Response(json.dumps(getAllFeaturesFromDB()),  mimetype='application/json')

@app.route('/feature/saveFeature',  methods=['POST'])
def saveTheFeature():
    # feature, value, data, category, status
    data = request.json
    print(request.json['id'])
    values = (data['feature'],data['value'],data['data'],data['category'],data['status'])
    return saveAFeature(data['id'],data['feature'],data['value'],data['data'],data['category'],data['status'])


#
# configuration
# operations
@app.route('/config/getByConfigId', methods=['POST'])
def getSingleConfiguration():
    return json.dumps(getByConfigId(int(request.json['id'])).__dict__), 200, {'ContentType': 'application/json'}

@app.route('/config/getAllConfig')
def getAllConfiguration():
    return Response(json.dumps(getAllConfigurationFromDB()),  mimetype='application/json')

@app.route('/config/saveConfig',  methods=['POST'])
def saveTheConfiguration():
    # feature, value, data, category, status
    data = request.json
    # print(request.json['id'])
    return saveAConfiguration(data['id'],data['feature'],data['category'],data['product'],str(data['weightage']),data['greenmax'],data['greenmin'],
    data['ambermax'],data['ambermin'],data['redmax'],data['redmin']);


#criteria
@app.route('/criteria/getAllCriterias')
def getAllCriteria():
    return Response(json.dumps(getAllCriteriaFromDB()),  mimetype='application/json')

@app.route('/criteria/getByCriteriaId', methods=['POST'])
def getSingleCriteria():
    return json.dumps(getByCriteriaId(int(request.json['id'])).__dict__), 200, {'ContentType': 'application/json'}

@app.route('/criteria/saveCriteria',  methods=['POST'])
def saveTheCriteria():
    # feature, value, data, category, status
    data = request.json
    # print(request.json['id'])
    # values = (data['feature'],data['value'],data['data'],data['category'],data['status'])
    return saveCriteria(None,data['feature'],data['category'],data['product'],data['datasource'],data['keyvalue'], data['sqlapi'])

# main driver function
if __name__ == '__main__':
    app.run()