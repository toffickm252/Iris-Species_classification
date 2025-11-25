# Iris-Species_classification

This project demonstrates Iris flower species classification using a Support Vector Machine (SVM) model trained on the Iris dataset. It includes data preprocessing, model training, evaluation, and a Streamlit web app for predictions.

## Features
- SVM model trained on sepal length and width features.
- Model evaluation with accuracy, classification report, and confusion matrix.
- Interactive Streamlit app for real-time predictions.
- Saved model for easy deployment.

## Installation
1. Clone the repository:
git clone https://github.com/toffickm252/Iris-Species_classification.git
cd Iris-Species_classification


2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate # On Windows


3. Install dependencies:
pip install -r requirements.txt


## Usage
### Training and Evaluation
Run the Jupyter notebook [`src/cleaning.ipynb`](src/cleaning.ipynb ) to load data, train the model, evaluate it, and save it.

### Deployment
Run the Streamlit app: streamlit run app.py

Open the app in your browser and input sepal length/width to predict the species.

## Project Structure
- [`src/cleaning.ipynb`](src/cleaning.ipynb ): Notebook for data loading, training, and evaluation.
- [`streamlit-app/app.py`](streamlit-app/app.py ): Streamlit app for predictions.
- [`models/svm_model.pkl`](models/svm_model.pkl ): Saved trained model.
- [`requirements.txt`](requirements.txt ): List of dependencies.

## Dependencies
- scikit-learn
- streamlit
- numpy
- pandas
- matplotlib
- joblib

## Contributing
Feel free to submit issues or pull requests.

## License
MIT License.