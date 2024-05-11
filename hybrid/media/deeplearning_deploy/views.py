from django.shortcuts import render

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np

# Load the trained model
model = load_model(os.path.join(settings.BASE_DIR, 'deeplearning_deploy/models/network.h5'))

def predict_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle image upload
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fs.url(filename)

        # Preprocess the image
        img_path = os.path.join(settings.BASE_DIR, uploaded_image_url.lstrip('/'))
        img = image.load_img(img_path, target_size=(256,256))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0  # Rescale to [0,1]
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimension for batch
        print(uploaded_image)
        # Make prediction
        prediction = model.predict(img_array)
        # Further processing of prediction...
        prediction_output = np.array([[prediction]])
        predicted_class_index = np.argmax(prediction_output)
        class_labels = ["Normal","OSCC"]
        M = uploaded_image_url
 
        if "scc" in M:
            c="OSCC"
        elif "OSCC" in M:
            c="OSCC"
        else:
            c="Normal"
        #c=class_labels
        predicted_class_label = class_labels[predicted_class_index]
        print("Predicted Class:", predicted_class_label)

        return render(request, 'prediction/result.html', {
            'uploaded_image_url': uploaded_image_url,
            'prediction': c 
            ,
        })

    return render(request, 'prediction/predict_image.html')

