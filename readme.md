# Quora Duplicate Question Detection

## Problem Statement
Quora faced a challenge in identifying duplicate questions. For instance, questions like "What are ways to reset a password" and "How can I reset my password" were treated as separate questions. This separation led to fragmented responses and a lack of proper attention to the questions.

To address this issue, I proposed a machine learning solution utilizing an NLP framework.

## Demo
![Demo](https://github.com/abhishekiiitbh2903/Quora_Duplicate_Question_Pairs/blob/main/duplicate-question-pair-finder-google-chrome-2024-08-01-15-58-12_Fx2qcFqs%20(online-video-cutter.com).gif)

## Solution Overview
This project leverages advanced feature engineering and a heuristic approach to create handcrafted features that enhance the accuracy of duplicate question detection. 

## Models Tried
- **Gaussian Naive Bayes**
- **Random Forest Classifier**
- **XGBoost Classifier**

## Performance Metrics
The performance of the models was evaluated using the following metrics:
- **Accuracy**
- **Confusion Matrix**
- **ROC Curve**

## Results
Although the XGBoost classifier showed a slight upper hand in accuracy, it had a higher rate of false positives, which is critical to minimize in this use case. Therefore, the Random Forest classifier was preferred as it performed better in reducing false positives.



## Author
This project is authored by Abhishek Singh, a final-year CSE undergraduate at IIIT Bhagalpur.

## Contributions
I am open to legitimate pull requests and will merge them if they add valuable improvements to the project.
