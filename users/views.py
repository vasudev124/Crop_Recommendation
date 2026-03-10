from django.shortcuts import render, redirect
import numpy as np
import tensorflow as tf
from django.contrib import messages
from .models import User  # Assuming this is a custom user model; change if using Django's built-in User
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        address = request.POST.get('address')

        profile_picture = request.FILES.get('profile_picture')  # Handle file upload

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        user = User(name=name, mobile=mobile, email=email, password=password, age=age, address=address)

        if profile_picture:
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            user.profile_picture = filename

        user.save()

        messages.success(request, 'Registration successful! Please login.')
        return redirect('ulogin')

    return render(request, 'register.html')



def ulogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the username or email
        password = request.POST.get('password')  # Get the password

        # Check if the user exists and the password is correct
        try:
            user = User.objects.get(email=email)
            if user.password == password:  # Be cautious about plain text password comparison
                # Log the user in (you may want to set a session or token here)
                request.session['user_id'] = user.id  # Store user ID in session
                messages.success(request, 'Login successful!')
                return redirect('udashboard')  # Redirect to the index page or desired page
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'ulogin.html')

def udashboard(req):
    return render(req, 'udashboard.html')


# Load the trained model
model = tf.keras.models.load_model('tcn_model.h5')

# Labels (same order as used during training)
labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram',
          'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
          'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

# Function to predict the crop
def predict_crop(n, p, k, temperature, humidity, ph, rainfall):
    # Create an input array
    input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
    input_data = input_data[:, :, np.newaxis]  # Add time dimension

    # Get prediction probabilities
    prediction_probs = model.predict(input_data)
    
    # Find the label with the highest probability
    predicted_label = labels[np.argmax(prediction_probs)]
    confidence = np.max(prediction_probs) * 100

    return predicted_label, confidence

# Handle user input and prediction
def prediction(request):
    if request.method == 'POST':
        # Get user inputs
        n = float(request.POST['nitrogen'])
        p = float(request.POST['phosphorus'])
        k = float(request.POST['potassium'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])

        # Make prediction
        crop, confidence = predict_crop(n, p, k, temperature, humidity, ph, rainfall)

        # Render the result
        return render(request, 'prediction.html', {
            'crop': crop,
            'confidence': f"{confidence:.2f}%",
            'inputs': {
                'nitrogen': n, 'phosphorus': p, 'potassium': k,
                'temperature': temperature, 'humidity': humidity, 'ph': ph, 'rainfall': rainfall
            }
        })

    return render(request, 'prediction.html')


