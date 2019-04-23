# EmojiPrediction

This repository is aim to improvement the [paper](https://dl.acm.org/citation.cfm?id=3282406)

## Getting Started
To install PyTorch, see installation instructions on the [PyTorch website](pytorch.org).

To install TorchText:

``` bash
pip install torchtext
```

We'll also make use of spaCy to tokenize our data. To install spaCy, follow the instructions [here](https://spacy.io/usage/) making sure to install the English models with:

``` bash
python -m spacy download en
```

You can get the emoji dataset collected in twitter this [link](https://github.com/fvancesco/Semeval2018-Task2-Emoji-Detection/blob/master/dataset/Semeval2018-Task2-EmojiPrediction.zip?raw=true). This dataset is provided by SemEval 2018 Task 2. In order to run these notebook, you must put on thawed `Semeval2018-Task2-EmojiPrediction` folder to current directory.

To shape the dataset:
``` bash
python prepare.py
```

## Reference
https://github.com/bentrevett/pytorch-sentiment-analysis
