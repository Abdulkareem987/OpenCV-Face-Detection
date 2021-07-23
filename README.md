# OpenCV-Face-Detection
 
This is a live streaming web app with face detection using Python and OpenCV

The application opens on a web browser once the user runs app.py and uses the web cam to start live streaming and detecting faces by putting a blue rectangle around it.

The app uses openCV cascades to detect faces during live streaming a video or seeing a picture.

List of files:

Cascades folder: this folder contains all the cascades of OpenCV that can be used to detect faces, eyes, smiles and more.

Templates folder: this folder contains the HTML templates that run on the browser and style the page that shows the live feed.

main.py: this is a python code that when run uses the computer's web cam to start a live feed and detect faces in the feed.

app.py: this page is for the python code that creates the web app and renders the html templates to run on the browser.

camera.py: this is a page for the python code that connect the live detection code with the web app.

## Notes:

1- To use the web app, run the app.py file, and to run the code locally run the main.py.

2- Make sure the project folder is on the same disk as python