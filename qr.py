import qrcode
# Dữ liệu bạn muốn mã hóa thành QR code
data = "Hello, this is a QR code!"
# Tạo đối tượng QR code
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
# Thêm dữ liệu vào QR code
qr.add_data(data)
qr.make(fit=True)
# Tạo hình ảnh QR code
img = qr.make_image(fill_color="black", back_color="white")
# Lưu hình ảnh vào một tệp
img.save("my_qrcode.png")
# Hiển thị hình ảnh
img.show()