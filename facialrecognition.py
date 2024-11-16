import cv2

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image (replace with your image path)
image_path = 'image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to grayscale (Haar Cascade works on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with faces outlined
cv2.imshow('Face Detection', image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
