

If you haven't already installed VS Code, Python, and Flask on your computer, please make sure to install them before starting the project

install VS Code, Python, and Flask:

1.VS Code (Visual Studio Code):

Visit the official website of Visual Studio Code: https://code.visualstudio.com/
Download the installer for your operating system (Windows, macOS, or Linux).
Run the installer and follow the on-screen instructions to complete the installation.

2.Python:

Visit the official Python website: https://www.python.org/
Navigate to the Downloads section and choose the latest version suitable for your operating system.
Download the installer and run it.
During installation, make sure to check the box that says "Add Python to PATH" to ensure Python is easily accessible from the command line.
Follow the installation prompts to complete the process.

3.Flask (assuming you're using Python's package manager, pip):

Once Python is installed, open a command prompt or terminal window.
Type the following command to install Flask: pip install Flask
Press Enter, and pip will download and install Flask and its dependencies.
After installation, you can verify the installation by typing flask --version in the command prompt/terminal.
That's it! Once you've completed these steps, you'll have VS Code, Python, and Flask installed on your computer and ready to use for the project.





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
