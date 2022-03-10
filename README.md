# CORE Skills Data Science Springboard - Day 12 - Special Data Types: Natural Language Processing

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/core-skills/12-text-processing.git/master)

# Overview

## Aims
1. Gain a practical understanding of traditional and modern natural language processing techniques.
2. Develop an intuition for knowledge graphs and ontologies.
3. Familiarisation with basic text handling and processing such as lemmatisation, stemming, etc.
4. Gain intuition towards word vectors and their applications in natural language processing.
5. Develop an understanding of supervised learning using modern tools such as HuggingFace.
6. Develop an understanding of unsupervised learning using latent topic models.

## Schedule

|          AWST | AEST          | Agenda                                                 |
| -------------:|:------------- | ------------------------------------------------------ |
| 07:30 - 07:45 | 09:30 - 09:45 | Q&A, Issues & Announcements |
| 07:45 - 09:15 | 09:45 - 11:15 | 12.0 Overview of NLP  |
| 09:15 - 09:30 | 11:15 - 11:30 | *Morning Tea*                                          |
| 09:30 - 11:00 | 11:30 - 13:00 | 12.1/2 Fundamentals of NLP |
| 11:00 - 11:45 | 13:00 - 13:45 | *Lunch*                                                |
| 11:45 - 13:15 | 13:45 - 15:15 | 12.3 Supervised Learning                   |
| 13:15 - 13:30 | 15:15 - 15:30 | *Afternoon Tea*                                        |
| 13:30 - 14:30 | 15:30 - 16:30 | 12.4 Unsupervised Learning                     |
| 14:30 - 14:55 | 16:30 - 16:55 | **Closeout & Feedback** |
| 14:55 - 15:00 | 16:55 - 17:00 | **Menti Feedback** |
| 15:00 - 15:00 | 17:00 - 17:00 | **Closeout**|

<!---
## Instructions for setting up interactive Google Colab notebooks

The following steps assume that you have access to a google account (e.g. have a gmail email).

#### Copying the code repository from Github
1. Go to https://github.com/core-skills/12-text-processing and click on the green button 'clone or download'. Download the repository .zip file and unzip.
2. You should now have a folder with the following structure:
    ```
    12-text-processing
    └──  data
            └──  reviews_data.txt.gz
            └──  walden.txt
            └──  wamex_xml.zip
    └──  handouts
            └──  coreskills-week-12-nlp.pptx
    └──  notebooks
            └──  12.1-An introduction to the NLTK.ipnyb
            └──  12.2.1-Gensim word vector visualisation.ipynb
            └──  12.2.2-WordEmbeddings.ipynb
            └──  12.3-LDA-GSWA.ipynb
            └──  12.4-PytorchSentimentAnalysis.ipynb
    └──  .DS_Store
    └──  LICENSE
    └──  README.md
    └──  environment.yml
    ```

#### Download embedding data
1. Download the embedding data 'glove.6B.100d.txt' from the following Google Drive link https://drive.google.com/open?id=1L9bYIEd6jBTW3P4yWMnyVT178lUp5Mx9
2. Place this file into `12-text-processing/data` folder in the structure shown above.

#### Copy the `12-text-processing` folder into Google Drive
1. Copy the entire folder `12-text-processing` into your Google Drive `My Drive`. The path at the top of the drive should look like `My Drive > 12-text-processing master`.

#### Ensuring that Google Colab notebooks function correctly
1. In your Google Drive, go to the folder `My Drive/12-text-processing/notebooks`. Open the first notebook `12.1-An introduction to the NLTK.ipynb` by right clicking on it's name and selecting `Open With > Google Colaboratory`. This will open a new tab in your browser.
2. With the notebook open, get familiar with 'mounting' your Google Drive to the notebook (We'll need to do this for the majority of the notebooks to ensure we can access the data). For this particular notebook, this is done in the first cell under the heading `Loading text data`.
3. Press `shift + enter` to execute the cell or click on the 'play' button on the upper left hand side of the cell. This will prompt you to follow a URL and get an activation code to permit mounting the drive. Once you'd done this it will not be required again, and will permit you to access files on your Google Drive.
--->

### Resources mentioned in the course
1. [Cere for Transforming Maintenance Through Data Science (CTMTDS)](https://www.maintenance.org.au/)
2. [CTMTDS - Theme 1 Support the Maintainer (Wei & Tyler; NLP-TLP)](https://www.maintenance.org.au/category/rt1)
3. [UWA - Natural & Technical Language Processing Group](https://nlp-tlp.org/)
4. [Industrial Ontologies - Maintenance Working Group](https://www.industrialontologies.org/?page_id=92)
5. [Interactive word2vec (embedding) visualisation tool](https://ronxin.github.io/wevi)
6.  [HuggingFace 🤗](https://huggingface.co/)
7.  [HuggingFace 🤗 Notebooks](https://github.com/huggingface/transformers/tree/master/notebooks)
8.  [Allen Institute of Artificial Intelligence (AI2) - Demos](https://demo.allennlp.org/reading-comprehension/bidaf-elmo)
9.  [GPT-3 Language Model Demos](https://beta.openai.com/examples)
### Dependencies used in the notebooks
1. [Spacy - Industrial Strength Natural Language Processing](https://spacy.io/)
2. [Gensim - Topic Modelling for Humans](https://radimrehurek.com/gensim/)
3. [NLTK - Natural Language Toolkit](https://www.nltk.org/)
4. [PyTorch - Binary Cross Entropy Loss (BCELoss)](https://pytorch.org/docs/stable/nn.html#bceloss)
5. [PyTorch - Recurrent Neural Network (RNN) module](https://pytorch.org/docs/stable/nn.html#rnn)
6. [CUDA framework for GPU training](https://developer.nvidia.com/cudnn)
7. [CUDA supported GPUs](https://developer.nvidia.com/cuda-gpus)