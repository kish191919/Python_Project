import itertools
import zipfile
import os

# Change the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define a function to unzip a password-protected ZIP file
def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len + 1):
        
        # Generate all possible combinations of characters from 'passwd_string' with lengths from 'min_len' to 'max_len'
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                # Try to extract the ZIP file using the current password attempt
                zFile.extractall(pwd=passwd.encode())
                print(f"The password is {passwd}")
                return 1
            except:
                pass

# The characters that can be used in the password attempts
passwd_string = "0123456789"

# Open the ZIP file to be unlocked
zFile = zipfile.ZipFile(r'6_Password/password1234.zip')

# Minimum and maximum password lengths to try
min_len = 1
max_len = 5

# Call the 'un_zip' function to attempt to unzip the file
unzip_result = un_zip(passwd_string, min_len, max_len, zFile)
