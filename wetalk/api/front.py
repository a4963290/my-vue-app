# -*- coding: utf-8 -*-
"""
    wetalk.api.front
    ~~~~~~~~~~~~~~~~

    :license: LICENSE_NAME, see LICENSE for more details.
"""

from flask import jsonify,session,request
from threading import Lock

from . import api
from wetalk import socketio
from flask_socketio import emit,disconnect
thread = None
thread_lock = Lock()

@api.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello Vue!')


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(2)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()

@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})
