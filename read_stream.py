import cv2 as cv
import sys

def get_stream(video_url):
    cap = cv.VideoCapture(video_url)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        status, frame = cap.read()

        # if frame is read correctly ret is True
        if not status:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # create gray scale for the frame
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if cv.waitKey(1) == ord('q'):
            break


        image = cv.imencode('.jpg', frame)[1]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image.tobytes() + b'\r\n\r\n')

        # prompt the opencv preview with a gray scale frame
        # cv.imshow('frame', gray)
    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    get_stream(sys.argv[1])
