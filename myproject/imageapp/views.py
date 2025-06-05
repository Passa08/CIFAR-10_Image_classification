from django.shortcuts import render
from django.conf import settings
from .models import ImagePrediction
from .forms import ImageUploadForm
import numpy as np
from PIL import Image
import os

# CIFAR-10 class labels
CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def preprocess_image(image):
    # Resize image to 32x32 pixels
    img = image.resize((32, 32))
    # Convert to array and normalize
    img_array = np.array(img) / 255.0
    # Add batch dimension
    return np.expand_dims(img_array, axis=0)

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            instance = form.save(commit=False)
            
            try:
                # Import TensorFlow and load model only when needed
                import tensorflow as tf
                MODEL_PATH = os.path.join(settings.BASE_DIR, 'cifar10_cnn_model.h5')
                model = tf.keras.models.load_model(MODEL_PATH)
                
                # Open and preprocess the image
                img = Image.open(request.FILES['image'])
                img = img.convert('RGB')  # Convert to RGB if not already
                processed_img = preprocess_image(img)
                
                # Make prediction
                predictions = model.predict(processed_img)
                predicted_class = CLASSES[np.argmax(predictions[0])]
                confidence = float(np.max(predictions[0]) * 100)
                
                # Save prediction results
                instance.prediction = predicted_class
                instance.confidence = confidence
            except Exception as e:
                instance.prediction = "Error: Could not process image"
                instance.confidence = 0.0
            
            instance.save()
            
            return render(request, 'imageapp/result.html', {
                'image_prediction': instance,
                'form': ImageUploadForm()
            })
    else:
        form = ImageUploadForm()
    
    return render(request, 'imageapp/index.html', {'form': form})
