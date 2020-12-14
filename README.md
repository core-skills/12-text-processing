# CORE Skills Data Science Springboard - Day 12 - Special Data Types: Natural Language Processing

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/core-skills/12-text-processing.git/master)

# Overview

## Aims
1. Gain a practical understanding of traditional and modern natural language processing techniques.
2. Develop an intuition for knowledge graphs and ontologies.
3. Familiarisation with basic text handling and processing such as lemmatisation, stemming, etc.
4. Gain intuition towards word vectors and their applications in natural language processing.
5. Develop an understanding of unsupervised learning using latent topic models
6. Develop an understanding of supervised learning using modern tools such as PyTorch for sentiment analysis.

## Schedule

|          AWST | AEST          | Agenda                                                 |
| -------------:|:------------- | ------------------------------------------------------ |
| 07:30 - 07:45 | 09:30 - 09:45 | Q&A, Issues & Announcements                            |
| 07:45 - 09:15 | 09:45 - 11:15 | **Session 1: Handling Text and Basic Text Processing** |
| 09:15 - 09:30 | 11:15 - 11:30 | *Morning Tea*                                          |
| 09:30 - 11:00 | 11:30 - 13:00 | **Session 2: Word Embeddings**                         |
| 11:00 - 11:45 | 13:00 - 13:45 | *Lunch*                                                |
| 11:45 - 13:15 | 13:45 - 15:15 | **Session 3: Unsupervised Learning**                   |
| 13:15 - 13:30 | 15:15 - 15:30 | *Afternoon Tea*                                        |
| 13:30 - 14:45 | 15:30 - 16:45 | **Session 4: Supervised Learning**                     |
| 14:45 - 15:00 | 16:45 - 17:00 | **Closeout**                                           |

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

## Miscellaneous links
Additional information pertaining to chat based discussions and material within the workshop:
1. Centre for Transforming Maintenance Through Data Science (CTMTDS): https://www.maintenance.org.au/
2. CTMTDS - Theme 1 Support the Maintainer (Wei & Tyler; NLP): https://www.maintenance.org.au/category/rt1
3. Industrial Ontologies - Maintenance Working Group: https://www.industrialontologies.org/?page_id=92
4. Aquila exploratory data analysis tool: http://agent.csse.uwa.edu.au/aquila
5. Spacy - Industrial Strength Natural Language Processing: https://spacy.io/
6. Gensim - Topic Modelling for Humans: https://radimrehurek.com/gensim/
7. NLTK - Natural Language Tool Kit: https://www.nltk.org/
8. Interactive word2vec (embedding) visualisation tool: https://ronxin.github.io/wevi/
9. PyTorch - Binary Cross Entropy Loss (BCELoss): https://pytorch.org/docs/stable/nn.html#bceloss
10. PyTorch - Recurrent Neural Network (RNN) module: https://pytorch.org/docs/stable/nn.html#rnn
11. CUDA framework for GPU training: https://developer.nvidia.com/cudnn
12. CUDA supported GPUs: https://developer.nvidia.com/cuda-gpus
13. Automatic Summarization (NLP/NLG): https://en.wikipedia.org/wiki/Automatic_summarization
14. Industrial Ontologies - Maintenance Working Group: https://www.industrialontologies.org/?page_id=92
15. Example of embeddings drawing powerful insights into COVID19 research: https://www.kaggle.com/tarunpaparaju/covid-19-dataset-gaining-actionable-insights
