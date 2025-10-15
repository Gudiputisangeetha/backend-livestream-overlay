import cv2

class StreamManager:
    def __init__(self, rtsp_url):
        self.cap = cv2.VideoCapture(rtsp_url)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
