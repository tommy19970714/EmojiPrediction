import sys
from os import path, makedirs

PATH_TASK = "./Semeval2018-Task2-EmojiPrediction"
PATH_TRIAL = path.join(PATH_TASK, "trial")
PATH_TRAIN = path.join(PATH_TRIAL, "train")
PATH_TEST = path.join(PATH_TRIAL, "test")

TRIAL_TEXT_FILE = path.join(PATH_TRIAL, "us_trial.text")
TRIAL_LABELS_FILE = path.join(PATH_TRIAL, "us_trial.labels")
TRAIN_TEXT_FILE = path.join(PATH_TRIAL, "us_train.text")
TRAIN_LABELS_FILE = path.join(PATH_TRIAL, "us_train.labels")
TEST_TEXT_FILE = path.join(PATH_TEST, "us_test.text")
TEST_LABELS_FILE = path.join(PATH_TEST, "us_test.labels")

def save_tsv(path, filename, text, label, label_max=-1):
    with open(path + filename, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(["text", "label"])
        for text, label in zip(train_text, train_labels):
            if label_max == -1 or int(label) <= label_max:
                writer.writerow([text, label])


if __name__ == '__main__':
    makedirs('data', exist_ok=True)
    path = './data/'
    
    trial_text = open(TRIAL_TEXT_FILE, "r")
    trial_labels = open(TRIAL_LABELS_FILE, "r")
    save_tsv(path, 'trial.tsv', trial_text, trial_labels)
    
#     train_text = open(TRAIN_TEXT_FILE, "r")
#     train_labels = open(TRAIN_LABELS_FILE, "r")
#     save_tsv(path, 'train.tsv', train_text, train_labels)
    
    test_text = open(TEST_TEXT_FILE, "r")
    test_labels = open(TEST_LABELS_FILE, "r")
    save_tsv(path, 'trial.tsv', test_text, test_labels)