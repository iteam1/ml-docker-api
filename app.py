from flask import Flask, request
import numpy as np
import os
import cv2
from keras.models import load_model

# Config
model_file = "models/cat_dog_classifier.hdf5"
width_size = 150
height_size = 150

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

# Load model
model = load_model(model_file)

@app.route('/',methods =['GET'])
def home():
	return "wellcome to ML-server"

@app.route('/predict', methods=['POST'])
def index():
	try:
		if request.method == 'POST':
			image = request.files['file']
			if image:
				# Lưu file
				path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
				image.save(path_to_save)

				# preprocessing
				frame = cv2.imread(path_to_save)
				# Xử lý file
				frame = cv2.resize(frame,(width_size,height_size),interpolation=cv2.INTER_AREA)
				# Convert thành tensor
				frame = np.expand_dims(frame, axis=0)  # Used for single images [1,w,h]
				# Đưa vào model
				prediction_prob = model.predict(frame)[0][0]
				# Xét kết quả
				if prediction_prob < 0.5: # 0-0.5: cat, else dog
					output = "cat"
				else:
					output = "dog"

				return "Prediction: " + output + " Prob: " + str(prediction_prob)
		else:
			return "We only accept POST with image file"
	except Exception as ex:
		print(ex)
		return "Error: " + str(ex)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 8080)
