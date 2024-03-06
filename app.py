from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from PIL import Image

import imageio
from werkzeug.utils import secure_filename
import os
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer
from flask import send_file

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

device.set(device=DeviceId.GPU0)
colorizer = get_image_colorizer(artistic=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colorize', methods=['POST'])
def colorize():
    render_factor = int(request.form.get('render_factor'))
    watermarked = request.form.get('watermarked') == 'on'

    uploaded_file = request.files['source_image']

    if uploaded_file.filename == '':
        return redirect(url_for('index'))

    if allowed_file(uploaded_file.filename):
        # Save the uploaded file temporarily
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)

        # Colorize the uploaded image and get the colorized image path
        colorized_image_path = colorizer.get_transformed_image(file_path, render_factor=render_factor, watermarked=watermarked)

        # Get the output path for the colorized image
        result_images_dir = 'result_images'
        os.makedirs(result_images_dir, exist_ok=True)

        # Save the colorized image using imageio
        colorized_image_filename = os.path.join(result_images_dir, 'result.png')
        colorized_image_path.save(colorized_image_filename)

        return render_template('result.html', image_filename='result.png')
    else:
        return "Invalid file format. Allowed formats: png, jpg, jpeg, gif."

@app.route('/result_images/<filename>')
def get_result_image(filename):
    return send_from_directory('result_images', filename)

# Add this route to enable downloading of the colorized image
@app.route('/download_result/<filename>')
def download_result(filename):
    return send_file(f'result_images/{filename}', as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('result_images', exist_ok=True)
    app.run(debug=True)
