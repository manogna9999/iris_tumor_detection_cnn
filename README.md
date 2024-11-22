Iris Tumor Detection using CNN

This project is a web-based application designed to detect tumors in the iris region of medical images. Built with Django and Python, it provides a robust interface for medical professionals to analyze images and retrieve results efficiently.

Features

- Efficient Classification: Uses pre-trained or traditional machine learning models for classification.
- Django Framework: Provides a clean, modular backend and an intuitive frontend.
- Image Upload: Supports single or batch image uploads.
- Results Dashboard: Displays predictions, including detailed results and confidence levels.

Tech Stack

- Backend: Python 
- Web Framework: Django
- Frontend: HTML, CSS, JavaScript 
- Database: SQLite/PostgreSQL (configurable)
  
Prerequisites

Ensure you have the following installed:

1. Python (>= 3.8)
2. Django (>= 4.0)
3. Required Python Libraries (`requirements.txt` includes all dependencies)

Installation

1. Clone the Repository:
    git clone https://github.com/manogna9999/iris-tumor-detection.git
    cd iris-tumor-detection
   
2. Set Up a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
    pip install -r requirements.txt
   
4. Apply Migrations:
    python manage.py migrate
   
5. Run the Development Server:
    python manage.py runserver
    Access the application at `http://127.0.0.1:8000/`.

Usage

1. Image Upload:
   - Navigate to the upload page.
   - Upload iris images for tumor detection.

2. Run Analysis:
   - Submit the uploaded images for processing.
   - The system returns a classification (e.g., *tumor detected* or *no tumor*).

3. View Results:
   - Analyze results with confidence scores.

Dataset

The project uses publicly available iris datasets or custom datasets. Ensure images are preprocessed (e.g., resized, grayscale conversion).

Future Enhancements

- Integration of REST API for external application support.
- Deployment to cloud services for real-time accessibility.
- Addition of advanced image preprocessing techniques.
