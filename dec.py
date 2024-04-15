import cv2
import numpy as np
from pyzbar.pyzbar import decode
# Đọc hình ảnh chứa QR code
img = cv2.imread("my_qrcode.png")
# Chuyển đổi hình ảnh sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Sử dụng thư viện pyzbar để giải mã QR code
decoded_objects = decode(gray)
for obj in decoded_objects:
# In ra dữ liệu từ QR code
    print(f"Data: {obj.data.decode('utf-8')}")
# Vẽ hình chữ nhật xung quanh QR code
    points = obj.polygon
if len(points) == 4:
    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
cv2.polylines(img, [hull], True, (0, 255, 0), 2)
# Hiển thị hình ảnh với vùng chứa QR code
cv2.imshow("QR Code", img)
cv2.waitKey(0)
cv2.destroyAllWindows()