from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/add_stamp', methods = ['POST'])
def add_stamp():
    return 'Done', 201

@main.route('/stamps')
def stamps():
    stamps = []
    return jsonify({'stamps' : stamps})