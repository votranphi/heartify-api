import os

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Model paths
    MODEL_PATH = os.environ.get('MODEL_PATH', './model/heart_cnn_lstm_model.keras')
    SCALER_PATH = os.environ.get('SCALER_PATH', './model/scaler.save')