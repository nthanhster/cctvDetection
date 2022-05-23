# import libraries
from vidgear.gears import CamGear
import cv2

def vid_youtube(url="https://youtu.be/rOxE2Q6kOxE"):
    stream = CamGear(source=url, stream_mode=True, logging=True).start() # YouTube Video URL as input
    # cap = cv2.VideoCapture()
    # infinite loop
    while True:

        frame = stream.read()
        # read frames

        # check if frame is None
        if frame is None:
            #if True break the infinite loop
            break

        # do something with frame here

        cv2.imshow("Output Frame", frame)
        # Show output window

        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break

    cv2.destroyAllWindows()
    # close output window

    # safely close video stream.
    stream.stop()


if __name__ == "__main__":
    vid_youtube(url="https://youtu.be/rOxE2Q6kOxE")
