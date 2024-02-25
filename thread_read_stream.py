import cv2 as cv
import threading, queue, os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"

def start_stream(video_url, frame_queue):
    print("Start stream")
    cap = cv.VideoCapture(video_url)
    status, frame = cap.read()
    frame_queue.put(frame)

    while status:
        status, frame = cap.read()
        try:
            frame_queue.put(frame, timeout=1)
        except:
            print("Stop stream no more consumers")
            cap.release()
            break;
            

def get_stream_thread(video_url):
    frame_queue=queue.Queue(50)
    p1=threading.Thread(target=start_stream, args=(video_url,frame_queue,))
    p1.start()
    while True:        
           if frame_queue.empty() !=True:
            frame=frame_queue.get()
            image = cv.imencode('.jpg', frame)[1]
            
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + image.tobytes() + b'\r\n\r\n')
            
            
if __name__=='__main__':
    get_stream_thread() # todo add args
