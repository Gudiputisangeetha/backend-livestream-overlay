from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from utils import get_collection, serialize_doc
from stream_manager import StreamManager
from bson.objectid import ObjectId
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

overlay_col = get_collection("overlays")

# ----- CRUD Endpoints -----
@app.route("/overlays", methods=["POST"])
def create_overlay():
    data = request.json
    result = overlay_col.insert_one(data)
    overlay = serialize_doc(overlay_col.find_one({"_id": result.inserted_id}))
    socketio.emit("overlay_added", overlay)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route("/overlays", methods=["GET"])
def get_overlays():
    overlays = [serialize_doc(o) for o in overlay_col.find()]
    return jsonify(overlays)

@app.route("/overlays/<id>", methods=["PUT"])
def update_overlay(id):
    data = request.json
    overlay_col.update_one({"_id": ObjectId(id)}, {"$set": data})
    overlay = serialize_doc(overlay_col.find_one({"_id": ObjectId(id)}))
    socketio.emit("overlay_updated", overlay)
    return jsonify({"status": "updated"})

@app.route("/overlays/<id>", methods=["DELETE"])
def delete_overlay(id):
    overlay_col.delete_one({"_id": ObjectId(id)})
    socketio.emit("overlay_deleted", {"_id": id})
    return jsonify({"status": "deleted"})

# ----- Livestream Endpoint -----
@app.route("/stream")
def stream():
    rtsp_url = request.args.get("url")
    if not rtsp_url:
        return "RTSP URL is required", 400

    stream_manager = StreamManager(rtsp_url)

    def generate():
        while True:
            frame = stream_manager.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    socketio.run(app, debug=True)
