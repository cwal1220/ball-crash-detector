import cv2

# 마우스 이벤트 콜백 함수
def select_roi(event, x, y, flags, param):
    global roi, selecting_roi, start_x, start_y, end_x, end_y
    
    # 마우스 왼쪽 버튼을 누를 때
    if event == cv2.EVENT_LBUTTONDOWN:
        selecting_roi = True
        start_x, start_y = x, y
        end_x, end_y = x, y
    
    # 마우스 왼쪽 버튼을 누른 채로 이동할 때
    elif event == cv2.EVENT_MOUSEMOVE:
        if selecting_roi:
            end_x, end_y = x, y
    
    # 마우스 왼쪽 버튼을 뗄 때
    elif event == cv2.EVENT_LBUTTONUP:
        selecting_roi = False
        end_x, end_y = x, y
        
        # 관심 영역을 설정합니다.
        x, y = min(start_x, end_x), min(start_y, end_y)
        w, h = abs(end_x - start_x), abs(end_y - start_y)
        roi = img[y:y+h, x:x+w]
        
        # 평균 색상을 계산합니다.
        mean_color = cv2.mean(roi)

        # 평균 색상을 출력합니다.
        print("Mean Color (BGR): ", mean_color)

        # BGR을 RGB로 변환합니다.
        mean_color_rgb = (mean_color[2], mean_color[1], mean_color[0])

        # RGB 색상을 출력합니다.
        print("Mean Color (RGB): ", mean_color_rgb)

        # 관심 영역을 사각형으로 표시합니다.
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # 이미지와 관심 영역을 출력합니다.
        cv2.imshow('Image', img)
        cv2.imshow('ROI', roi)

# 이미지 파일을 읽어옵니다.
img = cv2.imread('image.jpg')

# 관심 영역을 초기화합니다.
roi = None
selecting_roi = False
start_x, start_y = 0, 0
end_x, end_y = 0, 0

# 마우스 이벤트 콜백 함수를 등록합니다.
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', select_roi)

# 이미지를 출력합니다.
while True:
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord('q'): # 'q' 키를 누르면 종료합니다.
        break

cv2.destroyAllWindows()
