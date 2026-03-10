# Crop Recommendation System

A Django-based web application that provides crop recommendations using Machine Learning models (SVM and TCN). The system analyzes soil and climate parameters to suggest the most suitable crops for a given environment.

## 📋 Features

- **Admin Dashboard**: Secure admin panel for system management
- **User Authentication**: User registration and login system
- **ML-Based Predictions**: 
  - **SVM Model**: Support Vector Machine for crop classification
  - **TCN Model**: Temporal Convolutional Network for advanced predictions
- **Interactive Web Interface**: Clean and responsive UI with HTML/CSS/JavaScript
- **Model Performance Metrics**: Real-time display of accuracy, precision, recall, and F1-score
- **User Profiles**: Profile management with picture upload capability
- **Contact & About Pages**: Information pages for users

## 🛠️ Technologies Used

- **Backend**: Django 4.2
- **Machine Learning**: 
  - scikit-learn (SVM, model evaluation)
  - TensorFlow/Keras (TCN model)
  - NumPy & Pandas (Data processing)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Additional**: Bootstrap, Bootstrap Icons, Swiper.js, AOS (Animate on Scroll)

## 📁 Project Structure

```
crop/
├── admins/                      # Admin app
│   ├── views.py                # Admin views (dashboard, SVM, TCN models)
│   ├── models.py               # Admin models
│   ├── urls.py                 # Admin URL routing
│   └── migrations/             # Database migrations
├── users/                       # User app
│   ├── views.py                # User registration/login views
│   ├── models.py               # User model (custom user profile)
│   └── migrations/             # Database migrations
├── crop/                        # Main Django project settings
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── assets/                      # Frontend assets
│   ├── static/                 # Static files
│   │   ├── css/               # Stylesheets
│   │   ├── js/                # JavaScript files
│   │   ├── img/               # Images
│   │   ├── vendor/            # Third-party libraries
│   │   └── forms/             # Contact forms
│   └── templates/             # HTML templates
│       ├── index.html         # Home page
│       ├── about.html         # About page
│       ├── contact.html       # Contact page
│       ├── alogin.html        # Admin login
│       ├── dashboard.html     # Admin dashboard
│       ├── svm.html           # SVM prediction page
│       ├── tcn.html           # TCN prediction page
│       ├── ulogin.html        # User login
│       ├── register.html      # User registration
│       └── udashboard.html    # User dashboard
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database
├── Crop_recommendation.csv      # Training dataset
├── tcn_model.h5               # Pre-trained TCN model
├── mhp.ipynb                   # Jupyter notebook (model training/analysis)
└── myvenv/                      # Python virtual environment
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone or navigate to the project directory**:
   ```bash
   cd d:\Project\12\CROP_RECOMMENDTION\crop
   ```

2. **Create and activate virtual environment** (optional but recommended):
   ```bash
   # Windows
   python -m venv myvenv
   myvenv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install django pandas scikit-learn tensorflow numpy scipy
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Open your browser and navigate to `http://localhost:8000`

## 📖 Usage

### Admin Access
- Navigate to `/alogin` to access the admin login page
- Default credentials: 
  - Username: `admin`
  - Password: `admin`
- From the dashboard, you can access:
  - **SVM Model**: View crop predictions using Support Vector Machine
  - **TCN Model**: View crop predictions using Temporal Convolutional Network

### User Access
- **Registration**: Navigate to the registration page to create a new account
  - Required fields: Name, Mobile, Email, Password, Age, Address, Profile Picture
- **Login**: Use your registered email and password to log in
- **Dashboard**: Access your personalized user dashboard after login

### Model Predictions
The system provides crop recommendations based on the following input parameters:
- **N** (Nitrogen content in soil)
- **P** (Phosphorus content in soil)
- **K** (Potassium content in soil)
- **Temperature** (Average temperature)
- **Humidity** (Air humidity percentage)
- **pH** (Soil pH level)
- **Rainfall** (Average rainfall)

## 🤖 Machine Learning Models

### SVM Model
- **Algorithm**: Support Vector Machine with RBF kernel
- **Training Data**: Crop_recommendation.csv
- **Features**: 7 soil and climate parameters
- **Output**: Recommended crop labels
- **Metrics**: Accuracy, Precision, Recall, F1-Score

### TCN Model
- **Algorithm**: Temporal Convolutional Network (Deep Learning)
- **Framework**: TensorFlow/Keras
- **Model File**: tcn_model.h5 (pre-trained)
- **Advantages**: Better for sequential/temporal patterns
- **Evaluation**: Weighted average metrics for multi-class classification

## 📊 Dataset

The project uses `Crop_recommendation.csv` containing:
- Soil nutrients (N, P, K)
- Environmental factors (temperature, humidity, rainfall, pH)
- Target variable (Crop label)

## 🔧 Configuration

### Important Settings in `settings.py`:
- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Add your domain/IP addresses
- **INSTALLED_APPS**: Contains `admins` and `users` apps
- **Database**: SQLite3 (change to PostgreSQL/MySQL for production)

## ⚠️ Security Notes

- **Default Credentials**: Change admin password in production
- **Plain Text Passwords**: Current implementation stores passwords as plain text. Use Django's built-in hashing for production
- **Session Management**: Implement proper authentication and authorization
- **CSRF Protection**: Ensure CSRF tokens are included in forms
- **Secret Key**: Change `SECRET_KEY` in settings.py for production

## 🚨 Known Issues & TODO

- [ ] Implement proper password hashing (use Django's built-in authentication)
- [ ] Add CSRF token validation for all forms
- [ ] Implement email verification for registration
- [ ] Add error handling for missing CSV or model files
- [ ] Optimize model loading (currently loads on each request)
- [ ] Add logging and monitoring
- [ ] Implement pagination for large datasets
- [ ] Add API endpoints for programmatic access

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/about` | About page |
| GET | `/contact` | Contact page |
| GET/POST | `/alogin` | Admin login |
| GET | `/dashboard` | Admin dashboard |
| GET/POST | `/svm` | SVM model predictions |
| GET/POST | `/tcn` | TCN model predictions |
| GET/POST | `/register` | User registration |
| GET/POST | `/ulogin` | User login |
| GET | `/udashboard` | User dashboard |

## 📦 Dependencies

Key packages and their versions:
- Django==4.2
- pandas>=1.3.0
- scikit-learn>=0.24.0
- tensorflow>=2.10.0
- numpy>=1.21.0
- scipy>=1.7.0
- keras>=2.10.0

## 👥 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

For issues, questions, or suggestions:
- Contact page: Navigate to `/contact`
- Email support through the contact form

## 🎯 Future Enhancements

- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Real-time weather API integration
- [ ] Advanced analytics dashboard
- [ ] Historical prediction tracking
- [ ] Recommendation explanations (LIME/SHAP)
- [ ] Crop price predictions
- [ ] Pest and disease detection
- [ ] Farmer community forum

---

**Last Updated**: February 2026

**Version**: 1.0.0
