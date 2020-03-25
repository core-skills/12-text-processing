# CORE Skills Data Science Springboard - Day 12 - Special Data Types: Natural Language Processing

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/core-skills/12-text-processing.git/master)

# Overview

## Aims
1. Gain a practical understanding of traditional and modern natural language processing techniques.
2. Develop an intuition for knowledge graphs and ontologies.
3. Familiarisation with basic text handling and processing such as lemmatisation, stemming, etc.
4. Gain intuition of word vectors and their applications in natural language processing.
5. Develop an understanding of unsupervised learning using latent topic models
6. Develop an understanding of supervised learning using modern tools such as PyTorch for sentiment analysis.

## Schedule

| Start | End   | Agenda                           |
| -----:|:----- | -------------------------------- |
| 08:30 | 08:45 | Q&A, Issues & Announcements      |
| 08:45 | 10:00 | **Session 1: Handling Text**        |
| 10:00 | 10:30 | *Morning Tea*                    |
| 10:30 | 12:00 | **Session 2: Basic Text Processing**            |
| 12:00 | 13:00 | *Lunch*                          |
| 13:00 | 14:30 | **Session 3: Unsupervised Learning**           |
| 14:30 | 15:00 | *Afternoon Tea*                  |
| 15:00 | 16:30 | **Session 4: Supervised Learning** |
| 16:30 | 16:45 | **Closeout**                   |

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
