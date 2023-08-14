from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import base64
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def stream_video():
def stream_video():
    cap = cv2.VideoCapture(0)  # Use the appropriate camera index or video file

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            frame_data = base64.b64encode(buffer).decode('utf-8')

            socketio.emit('video_frame', frame_data, broadcast=True)
    except Exception as e:
        print("Error in stream_video:", e)


if __name__ == '__main__':
    video_thread = Thread(target=stream_video)
    video_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
