# Lyrical Sentiment Analysis
![Python Version](https://img.shields.io/badge/Python-3.7.6-red)
![Tensorflow Version](https://img.shields.io/badge/tensorflow-2.3.0-lime)
![Keras Version](https://img.shields.io/badge/keras-2.4.3-orange)
![Pypi Version](https://img.shields.io/badge/pypi-20.0.2-yellow)
![Mediapipe](https://img.shields.io/badge/mediapipe-blue)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## Overview
Lyrical Sentiment Analysis in Python using Natural Language Processing(NLP) with the help of [Mediapipe](https://developers.google.com/mediapipe). This project focuses on sentiment analysis of song lyrics to identify positive and negative sentiments, employing advanced NLP and machine learning techniques. We have incorporated Google's MediaPipe framework specifically for enhancing the processing capabilities of our BERT model, previously leveraging only TensorFlow and Transformers from Hugging Face.

## Key Features
- **Data Collection**: Scraping the top songs from various online databases.
- **Preprocessing**: Standardizing data by removing special characters and tokenizing text.
- **Sentiment Analysis**: Using BERT model enhanced with MediaPipe for improved feature extraction and faster processing.
- **Visualization**: Displaying data insights through interactive charts and graphs.

## MediaPipe Integration
MediaPipe offers state-of-the-art machine learning solutions for media processing. In this project, we use MediaPipe to optimize our BERT model, enhancing its ability to process and analyze lyrical content efficiently. This integration allows for real-time analysis and increased accuracy in sentiment classification.

## Requirements
 To start the scraping process we need to get the requirement for the scarping.
 ```
pip install -r requirements.txt
```

To update the webdriver after we import all the required files with the command bellow:

```
pip install --upgrade webdriver-manager
```

## Installation


## Usage


## Contributors
- [Josue Cortez](https://github.com/jgcortez)
- [Pratham Gupta](https://github.com/prathamgupta36)
- [Shashank Navad](https://github.com/shashnavad)
- [Ryan Skabelund](https://github.com/ryan-skabelund)
- [Race Musgrave](https://github.com/R-a-c-e)
- [Tanooj Reddy Seelam](https://github.com/TanoojSeelam)

## Acknowledgements
- Arizona State University, School of Computing and Augmented Intelligence
- TensorFlow, Hugging Face for the initial model frameworks
- Google MediaPipe for the enhanced processing tools

## References
- [MediaPipe](https://google.github.io/mediapipe/)
- [TensorFlow](https://www.tensorflow.org/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
