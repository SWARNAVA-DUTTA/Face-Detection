import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('group_face.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Print Total number of faces found
print("Found {0} faces!".format(len(faces)))

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)  # (0,0,255) is the colour code for RED
                                                                # 5 is the width of border of rectangle

# Save the output
cv2.imwrite('Output.jpg', img)
cv2.waitKey()
