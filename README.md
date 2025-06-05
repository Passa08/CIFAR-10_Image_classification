# CIFAR-10 Image Classification Project

A web-based application for image classification using the CIFAR-10 dataset and deep learning. This project uses Django for the web interface and a CNN model trained on the CIFAR-10 dataset to classify images into 10 different categories.

## Features

- Upload and classify images in real-time
- Web-based user interface
- Support for CIFAR-10 categories:
  - Airplane
  - Automobile
  - Bird
  - Cat
  - Deer
  - Dog
  - Frog
  - Horse
  - Ship
  - Truck

## Technologies Used

- Python 3.x
- Django
- TensorFlow/Keras
- HTML/CSS
- Bootstrap

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/Passa08/CIFAR-10_Image_classification.git
cd CIFAR-10_Image_classification
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` in your web browser to use the application.

## Project Structure

```
mini_project/
├── classifier/           # Main classification app
├── myproject/           # Project configuration
│   ├── config/         # Django settings
│   ├── imageapp/       # Image handling application
│   └── manage.py       # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Usage

1. Navigate to the home page
2. Click on the "Choose File" button to select an image
3. Click "Upload" to submit the image for classification
4. View the classification results and confidence score

## Model Information

The project uses a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. The model architecture is designed to recognize and classify images into 10 different categories with high accuracy.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- Passang Dorji