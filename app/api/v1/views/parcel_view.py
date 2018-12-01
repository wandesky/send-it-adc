from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.parcel_model import Parcel

parcels = Blueprint('parcels', __name__)

@parcels.route('/', methods=['GET'])
def get_parcels():
    return "Testing the app from parcels"

@parcels.route('/', methods=['POST'])
def post_parcel():
    req_data = request.get_json()
    # parcel_id = req_data['id'] the id will be dynamically generated
    parcel_placedBy = req_data['placedBy']
    parcel_weight = req_data['weight']
    parcel = Parcel(parcel_placedBy, parcel_weight)

    response = parcel.post_parcel()
    return response, 201