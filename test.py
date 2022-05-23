import pafy
import cv2




url = "https://youtu.be/rOxE2Q6kOxE"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)
while True:
    grabbed, frame = capture.read()
    print(type(grabbed))
    print(type(frame))
     # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break



    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        break

cv2.destroyAllWindows()



