from flask import Flask, request, render_template
import cv2
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import module1, module2, module3, module4, module5, module6

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['image']
        image = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        original_image = image.copy()  # Save the original image
        operation = request.form.get('operation')
        value = float(request.form.get('value'))

        if operation == 'rotate':
            image = module1.rotate_image(image, value)
        elif operation == 'flip':
            image = module2.flip_image(image, value)
        elif operation == 'zoom':
            image = module3.zoom_image(image, value)
        elif operation == 'resize':
            image = module4.resize_image(image, value)
        elif operation == 'blur':
            image = module5.blur_image(image, value)
        elif operation == 'space':
            image = module6.space_image(image, value)

        _, buffer = cv2.imencode('.jpg', original_image)
        original_image = base64.b64encode(buffer).decode('utf-8')

        _, buffer = cv2.imencode('.jpg', image)
        image = base64.b64encode(buffer).decode('utf-8')

        return render_template('index.html', original_image=original_image, image=image)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
