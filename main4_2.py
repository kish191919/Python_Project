# Import the qrcode library to generate QR codes
import qrcode

# Specify the file path to the text file containing QR code data
file_path = r"4_QR_Code/qr_list.txt"

# Open the text file for reading with UTF-8 encoding
with open(file_path, encoding="UTF8") as f:
    # Read all lines from the text file into a list
    read_lines = f.readlines()

    # Iterate through each line in the list
    for line in read_lines:
        # Remove leading and trailing whitespace from the line
        line = line.strip()
        
        # Print the cleaned line
        print(line)

        # Set the QR code data to the cleaned line
        qr_data = line

        # Generate a QR code image based on the QR code data
        qr_img = qrcode.make(qr_data)

        # Specify the path to save the QR code image with the data as its name
        save_path = r"4_QR_Code/" + qr_data + ".png"
        
        # Save the QR code image to the specified path
        qr_img.save(save_path)
