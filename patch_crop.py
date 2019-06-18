import cv2
import pinyin
import os
global img
global point1, point2
global count
def on_mouse(event, x, y, flags, param):
    global img, point1, point2, count
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 2)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 2)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        count +=1
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 2)
        cv2.imshow('image', img2)
        min_x = min(point1[0],point2[0])
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]
        write_path = name+"_"+str(int(frame/fps))+str(count)+'.jpg'
        print(write_path)
        cv2.imwrite(write_path, cut_img)


if __name__ == '__main__':
    video_path = "G:/红绿灯灯盘数据提取/白天/生态城8个路口下午正装视频/和风路和畅路/和畅和风北向南枪定1_云存储_C26R0P954_15-00-00_15-30-00/和畅和风北向南枪定1_云存储_C26R0P954_15-00-00_15-30-00_1.mp4"
    direction = os.path.basename(video_path).split(".")[0]
    name = pinyin.get(direction, format='strip')
    global img
    vid = cv2.VideoCapture(video_path)
    fps = vid.get(5)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    while(True):
        count = 0
        ret, img = vid.read()
        frame = vid.get(1)
        if not ret:
            break
        cv2.setMouseCallback('image', on_mouse)
        cv2.imshow('image', img)
        key = cv2.waitKey(1)
        if key == 32:
            cv2.waitKey(0)