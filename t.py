import numpy as np
import cv2
from pyzbar import pyzbar

RED = (0, 0, 255)
THICKNESS = 2
FONT = cv2.FONT_HERSHEY_DUPLEX
FONT_SCALE = 1
TEXT_THICKNESS = 1
windowName = 'Barcode scanner'
def readBarcode(frame):
    # 1
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        # 2
        points = barcode.polygon
        x, y, w, h = barcode.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img=frame, pts=[pts], isClosed=True, 
                      color=RED, thickness=THICKNESS)
        # 3
        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        # 4
        cv2.putText(img=frame, text=barcodeData, org=(x, y),   fontFace=FONT, 
                    fontScale=FONT_SCALE, color=RED, thickness=TEXT_THICKNESS)
        # 5
        with open(f"lastRecognizedBarcode.txt", mode ='w') as file:
            file.write(f"Last recognized barcode information \n"
                       f"Data: {barcodeData} \n" 
                       f"Type: {barcodeType}")
        print (barcodeData)
    return frame

def main():
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    # 2
    while ret:
        ret, frame = camera.read()
        frame = readBarcode(frame)
        cv2.imshow(windowName, frame)
        keyCode = cv2.waitKey(1)
        if keyCode & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
            break
    # 3
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()