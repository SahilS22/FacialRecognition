# FacialRecognition
## Face Detection Using OpenCV
This code uses OpenCV's  Classifier for detecting faces in images. The pre-trained Haar Cascade Classifier detects frontal faces and draws rectangles around them on the input image.

## Features
Face Detection: Detects faces in an image and marks them with green rectangles.

Haar Cascade Classifier: Uses the pre-trained Haar Cascade classifier provided by OpenCV.

Grayscale Conversion: Converts the image to grayscale to improve the accuracy of face detection.

## Install OpenCV

```bash
pip install opencv-python
```

## Add an image
Place the image want to process in the same directory or provide the path in the [image_path] variable.

## Working of code
The Python script works as follows:

Loading the Haar Cascade Classifier: It loads the pre-trained haarcascade_frontalface_default.xml file that is bundled with OpenCV.

Reading the Image: The script reads an image from the specified file path.

Grayscale Conversion: Converts the image to grayscale because Haar Cascade works with single-channel images.

Face Detection: The detectMultiScale() function detects faces in the image.

Drawing Rectangles: For each detected face, a green rectangle is drawn around it.

Displaying the Result: Displays the image with detected faces in a window.

## Output

![image](https://github.com/user-attachments/assets/62465ebb-942b-41d2-8195-8dba9110d84e)

