# DeOldify Image Colorization Web App

This is a web application built with Flask that utilizes the DeOldify library to colorize images. DeOldify is a deep learning-based project for colorizing and restoring old images and videos.

## Features

- Upload an image file (png, jpg, jpeg, or gif) to be colorized.
- Adjust the render factor to control the level of detail in the colorized image.
- Option to remove the watermark from the colorized result.
- View the colorized image on the web interface.
- Download the colorized image.

## Dependencies

- Flask: Web framework for Python.
- Pillow (PIL): Python Imaging Library for image processing.
- imageio: Library for reading and writing image data.
- deoldify: Deep learning-based project for image and video colorization.
- Werkzeug: WSGI utility library for Python.
- CUDA Toolkit (optional): Required for GPU acceleration if using NVIDIA GPUs.

## Installation

1. Clone this repository:

  
   git clone https://github.com/jantic/DeOldify.git DeOldify

2.Download the model file:

mkdir models

wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O models/ColorizeArtistic_gen.pth

3.Install dependencies using pip:

pip install -r requirements.txt

pip3 install imageio

pip3 install deoldify "Pillow<10.1.0"

4.Usage
Run the Flask application:

python app.py

Open your web browser and go to http://localhost:5000.

Upload an image file, adjust the render factor and watermark options as desired, then click "Colorize".

Once the colorization process is complete, you can view the colorized image on the web interface and download it using the provided link.
