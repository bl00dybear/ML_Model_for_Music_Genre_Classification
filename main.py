from scripts.read_and_preprocess_data import prepare_dataset
from scripts.train_model import construct_model


path_dataset_csv = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/data_set.csv"
dataset_path_raw = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/raw"

#data_set = prepare_dataset()
#data_set.to_csv(path_dataset_csv,index=False)

construct_model(path_dataset_csv,dataset_path_raw)