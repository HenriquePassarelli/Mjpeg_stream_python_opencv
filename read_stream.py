import cv2 as cv
import sys


def get_stream(video_url):
    cap = cv.VideoCapture(video_url)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame

        if cv.waitKey(1) == ord('q'):
            break
        cv.imshow('frame', gray) # to use the original color change the "gray" to "frame"
    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    get_stream(sys.argv[1])
