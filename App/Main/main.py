# Python Standard Library Dependencies


# External Dependency Imports
from flask import render_template, Blueprint, current_app, Response
import cv2

# Internal Dependency Imports
from App.Data.db_utils import add_document

#######################################################################################
#                                        Notes:                                       #
#                                                                                     #
# Things done in this file:                                                           #
# 1. Define the main blueprint for the application                                    #
# 2. Define the index route for the application                                       #
#                                                                                     #
#######################################################################################

# Define the main blueprint for the application
main_blueprint = Blueprint("main", __name__)

# Defile the utility functions needed in the application routes
def generate_camera_feed():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if success:
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except:
                pass

# Define the application routes
@main_blueprint.route("/")
def index():
    add_document(current_app, "Hello", "world")
    return render_template("index.jinja")

@main_blueprint.route("/scanner")
def scanner():
    return render_template("scanner.jinja")

@main_blueprint.route("/video_feed")
def video_feed():
    return Response(generate_camera_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')