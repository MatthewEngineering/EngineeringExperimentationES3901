# pic = bytes([1,2,3,4,5])
# open("image_bytes.txt","w")


# Write bytes to a text file
data = b'Hello, World!'
data = bytearray([1,2,3,65])
print(data)

# Open the file in binary mode
with open('image.txt', 'wb') as file:
    # Write the bytes to the file
    file.write(data)

# Read the bytes back from the text file
read_data = b''

# Open the file in binary mode
with open('image.txt', 'rb') as file:
    # Read the contents of the file
    read_data = file.read()

# Print the read bytes
print(read_data)