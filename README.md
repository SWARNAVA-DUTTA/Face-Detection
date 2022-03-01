# Face Detection

<h3> Using Webcam</h3>
 
![image (1)](https://user-images.githubusercontent.com/46235752/156127712-1fa59365-7649-4463-b007-970281a7439a.png)



Below are the steps to implement the code

1. Install Open-CV library
   ```python
   pip install opencv-python
   ```
2. Import the library in your code
   ```python
   import cv2
   ```
3. Load the cascade
   ```python
   face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   ```
4. Capture Video from Webcam 
   ```python
   cap = cv2.VideoCapture(0)
   ```
5. Continuously capture video
   ```python
   while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ```
6. Detect the faces and highlight them.<br/><br/>
   Here we are using **RED** rectangle to highlight the face(s). You can change the colour by changing the colour code **(0,0,255)** <br/>
   Here we are using width of border of rectangle as **2**. You can increase or decrease the width according to your own need.<br/>
    ```python
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display
    cv2.imshow('Detecting Face', img)
    ```
7.  The capture window exits on pressing "Esc"
    ```python
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    ```
8.  Stop capturing video by webcam
    ```python
    cap.release()
    cv2.destroyAllWindows()
    ```


-------------------------------------------------------------------------------------------------------------------------------------


<h3> From Image</h3>


<div float:left>
<img src="https://user-images.githubusercontent.com/46235752/156130238-826b588e-baff-4a79-bccc-10ded866a0a8.png" width="500" height="350">
<img src="https://user-images.githubusercontent.com/46235752/156130691-0cb33337-59a3-4052-9791-1ece1a082344.png" width="500" height="350">
</div>

Below are the steps to implement the code

1. Install Open-CV library
   ```python
   pip install opencv-python
   ```
2. Import the library in your code
   ```python
   import cv2
   ```
3. Load the cascade
   ```python
   face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   ```
4. Get image as input
   ```python
   img = cv2.imread('group_face.jpg')
   ```
5. Detect Faces
   ```python
   # Convert into grayscale
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   # Detect faces
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    ```
6. Print total number of faces found in image
   ```python
   print("Found {0} faces!".format(len(faces)))
   ```
7. Highlight the faces.<br/><br/>
   Here we are using **RED** rectangle to highlight the face(s). You can change the colour by changing the colour code **(0,0,255)** <br/>
   Here we are using width of border of rectangle as **5**. You can increase or decrease the width according to your own need.<br/>
    ```python
    for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
    ```
7.  Save the ouput in device folder
    ```python
    cv2.imwrite('Output.jpg', img)
    cv2.waitKey()
    ```
