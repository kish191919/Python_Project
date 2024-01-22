# pip install qrcode               => QR Code
# Import the 'qrcode' library to generate QR codes.
import qrcode

# Define the data you want to encode in the QR code.
qr_data = "www.linkedin.com"

# Generate a QR code image using the 'qrcode.make()' function.
qr_img = qrcode.make(qr_data)

# Define the path where you want to save the generated QR code image.
# In this case, it's saved in a directory named '4_QR_Code' with the data as the filename.
save_path = r"4_QR_Code/" + qr_data + '.png'

# Save the generated QR code image to the specified path.
qr_img.save(save_path)