from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import urllib.request
import urllib.parse
from django.conf import settings
from django.contrib.auth import authenticate, login
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')

def alogin(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        print("hello")
        print(username,password)
        # Check if the provided credentials match
        if username == 'admin' and password   == 'admin':
            messages.success(req, 'You are logged in.')
            return redirect('dashboard')  # Redirect to the admin dashboard page
        else:
             messages.error(req, 'You are trying to log in with wrong details.')
             return redirect('dashboard')  # Redirect to the login page (named 'admin' here)

    # Render the login page if the request method is GET
    return render(req, 'alogin.html')

def dashboard(req):
    return render(req, 'dashboard.html')

def svm(request):
    # Default values to show on the page
    context = {
        'accuracy': None,
        'precision': None,
        'recall': None,
        'f1': None,
    }

    if request.method == 'POST':
        # Load dataset
        file_path = 'crop_recommendation.csv'
        data = pd.read_csv(file_path)

        # Features and target
        X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        y = pd.factorize(data['label'])[0]  # Encode labels

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train SVM model
        svm_model = SVC(kernel='rbf', random_state=42)
        svm_model.fit(X_train, y_train)

        # Predictions
        y_pred = svm_model.predict(X_test)

        # Evaluate the model
        context['accuracy'] = f"{accuracy_score(y_test, y_pred):.4f}"
        context['precision'] = f"{precision_score(y_test, y_pred, average='weighted'):.4f}"
        context['recall'] = f"{recall_score(y_test, y_pred, average='weighted'):.4f}"
        context['f1'] = f"{f1_score(y_test, y_pred, average='weighted'):.4f}"

    return render(request, 'svm.html', context)

def tcn(request):
    # Load dataset
    file_path = 'crop_recommendation.csv'
    data = pd.read_csv(file_path)

    # Features and target
    X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].values
    y = data['label']

    # Encode target variable
    y, labels = pd.factorize(y)

    # Reshape the input for TCN (add a time dimension)
    X = X[:, :, np.newaxis]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load the trained model (ensure the path matches your setup)
    model_path = 'tcn_model.h5'
    tcn_model = tf.keras.models.load_model(model_path)

    # Evaluate the model
    y_pred_probs = tcn_model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)

    # Compute metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Pass results to the HTML template
    return render(request, 'tcn.html', {
        'accuracy': f"{accuracy:.4f}",
        'precision': f"{precision:.4f}",
        'recall': f"{recall:.4f}",
        'f1': f"{f1:.4f}"
    })



