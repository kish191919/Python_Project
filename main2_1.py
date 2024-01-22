import socket

# Connect to an external site (in this case, 'www.google.com') using a socket with SSL (port 443),
# and determine the internal IP address based on the local socket's connection information.
in_address = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_address.connect(('www.google.com', 443))

# Get the internal IP address by resolving the hostname of the local machine.
# in_address = socket.gethostbyname(socket.gethostname())

# Print the internal IP address of the local machine obtained from the socket's connection information.
print(in_address.getsockname()[0])