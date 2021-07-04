from stegano import lsb
image = "E:/doitwithpython/Codes/test.jpg"
new_image="data_hidden1.png"


msg="I am the king"

#Hide the message

lsb.hide(image, message=msg).save(new_image)

#to reveal hidden message

message = lsb.reveal(new_image)
print("Hidden message:", message)