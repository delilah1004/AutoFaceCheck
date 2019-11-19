# 카메라 테스트 파일
import cv2

class VideoCamera(object):
    def __init__(self):
        
        # 화면 캡쳐
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # 프레임 생성
    def get_frame(self):
        ret, frame = self.video.read()
        return frame

if __name__ == "__main__":
    cam = VideoCamera()
    while True:
        frame = cam.get_frame()

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    print('finish')
