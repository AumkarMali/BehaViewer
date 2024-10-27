# BehaViewer

## Description

This project uses machine learning, specifically the HistGradientBoostingClassifier, to predict a user’s Internet Service Provider based on their demographic and device details. By training on a JSON dataset, the model learns to categorize users into specific groups based on key attributes. This can help large organizations to make better economical decisions about thier websites and products. 

## Tech Stack

#### Programming Languages
* Python
* HTML
* CSS
* JavaScript


#### Libraries And Frameworks
* React
* CSS TailWind
* Json
* Flask 
* Panada (Panada.DataFrame)

## Functions

#### Main Function

The main function gets all  of the user data from the JSON file

#### Gradient Boosting Classifier Function

The gradientBoostingClassifier function uses HistGradientBoostingClassifier. The HistGradientBoostingClassifier is an advanced implimentation of the Gradient boosting alogrithm. It is provided by Scikit-Learn library. It uses histogram based techniques to enhance the efficiency and scalibity of gradient boosting. This is why the HistGradientBoostingClassifier is extremely suitable for large datasets. Gradient boosting models are used in a wide range of predictive modeling and machine learning tasks. While on one hand the GradientBoostingClassifiers struggle to handle large datasets due to its memory consumption. The HistGradientBoostingClassifier can handle large datasets with ease making it more useful for big data applications.

## Web Development and Data

#### Flask App

a python web framework, was used as it provides useful tools and features allowing to create web applicaitons in python very easily.

#### Panadas.DataFrame

* The numeric features for the device brand and plan of each user is based on mappings which are created using the panda data frames.
* Feeding the user data to the panda data frames makes the predictions for the provider.
* The panda.DataFrame creates a chart using the data given, just like the example provided below from our database:




#### Machience Learning

* 





## Design

Image of the user interface, we can put our website picture

## Features


## Installation
Fork the project
Clone the project
Follow the instructions in the console
Navigate to the project directory cd Telus-User-Data-System
Install the dependencies npm install
Run the project npm start









## Liabraries 

## Framworks

Flask app is a small and lightweight Python web framework. It provides useful tools and features allowing the developer to create web applicaitons in python very easily.  

The panda data frame creates a chart using the data given

The numeric features for the device brand and plan of each user is based on mappings which are created using the panda data frames

Feeding the user data to the panda data frames makes the predictions for the provider.

A feature matrix is a grid that lists important product features and compares them amongst each other to determine their relative value. The array "userDataQueries" is used as a feature matrix for the machine learning model. Classes (provider the customer will choose) is what is being predicted.

NaN represents the missing or undefined data which is handeled by the HistGradientBoostingClassifier.

New user data points are stored in Json and the same process of mapping is repeated with these data points. The predicted_class models the prediction of what the new user point (aka the new provider) will be. 

predicted_provider gives the [0] provider. Meaning the 1st (top) provider will be given out of a list of possible providers.
