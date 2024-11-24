import matplotlib.pyplot as plt
from scripts.read_and_preprocess_data import prepare_dataset
from scripts.train_model import construct_model


path_dataset_csv = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/data_set.csv"
dataset_path_raw = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/raw"


def create_model():
    data_set = prepare_dataset()
    data_set.to_csv(path_dataset_csv,index=False)
    history = construct_model(path_dataset_csv,dataset_path_raw,data_set)

    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.legend()
    plt.show()