# Churn Prediction in the Automotive Industry
A repository containing code and data for a churn prediction project in the automotive service business.

### Introduction to project and results

The automotive retail business is under pressure. The industry relies heavily on recurring aftersales service revenues to make a profit.
The goal of this project is to help a large european automotive retail and service company to reduce its churn rate (= the ratio of
customers who switch away from one supplier to another in a given period) by building _a predictive model to identify customers 
that are about to churn._ The project was a successful prototype for a model that was later implemented by the companys Data Science team. I used this project as capstone for Udacity's Machine Learning Nanodegree. 

The project was designed to answer 3 questions:

1) Can customer churn be predicted? (Yes, the model achieves a reasonable F1-score of 0.82 over all)
2) What are main drivers for churn? (Top 3: car age, duration of relationship / recency, distance home to branch)
3) What can be done to prevent churn? (This question is addressed in the blogpost only, see notebook 4.)

The project proposal and final report for the full project can be found in the `reports` section. A subsequent [blogpost](https://medium.com/@raph_91654/predict-churn-retain-your-customers-39cc62c322ed) summarizes the results. In the `rescources` section you'll find some interesting papers concerning churn prediction with Machine Learning.

### Install

This project requires **Python 3.x** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [seaborn](http://seaborn.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [tqdm](https://pypi.org/project/tqdm/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

### Code

The main code is split-up into 4 Jupyter notebooks, numbered 1 to 4:
1. `1-prep_get geo distances.ipynb`: feature engineering: calculate geo distances from customer adresses to their service branch
2. `2-EDA_cleaning.ipynb`: EDA and cleaning of features
3. `3-modelling_evaluation.ipynb`: modelling with 5 different classifiers, experimentation with PCA and tuning, result evaluation
4. `4-end_to_end_run.ipynb`: this is a concise rework of the earlier steps for the best performing Gradient Boosting Classifier. Because of more targeted data preparation the results here are better than in the version from notebook 3.

In this project I started to outsource functions for cleaning and EDA into collections of functions that would later form my `codebook`(see the repository of the same name.) For this project they are still stored in some .py files in the main folder. 

### Data

The cleaned dataset `churnDataWithDisctances.csv` used for modelling consists of approximately 50,000 data points (=cars), with each datapoint having 43 features. (This set is a pre-cleaned version of the original dataset, given to me by a large european automotive retail group, see notebooks 1 and 2 for cleaning steps.)

**Target Variable**
- `target_event`: customer status ('CHURN', 'ACTIVE')

**Features**
- `NUM_CONSEC_SERVICES`: number of consequtive service events for a car
- `SUM_INVOICE_AMOUNT`: sum of invoice amount that have been charged for all service events
- `NUM_EVENTS`: total number of service visits
- `LAST_MILEAGE`: mileage recorded at last visit
- `MEAN_MILEAGE_PER_MNTH`: calculated mean mileage per month 
- `age_mnth`: a car's age in months
- `INSPECTION_INTERVAL_UID`: timespan a car has to show up for mandatory service in months
- `LIST_PRICE`: car price
- `CAR_BRAND_UID`: car brand
- `FUEL_TYPE_UID`: fuel type
- `GEAR_TYPE_UID`: gear type
- `WHEEL_DRIVE_UID`: wheel drive type
- `NUMBER_OF_DOORS`: number of doors
- `GEAR_COUNT`: gear count
- `BASE_MARGIN`: base margin for dealer
- `SALES_TYPE`: car model
- `PERSON_LANGUAGE_UID`: language of car owner
- `PERSON_STATE`: address state of car owner
- `PERSON_ADDRESS_COUNT`:number of addresses in CRM-system for car owner
- `ownerAge`: age of car owner
- `REGION_UID`: address region of car owner
- `PARTNER_LANGUAGE_UID`: language of garage branch the car is affiliated with
- `IS_PREFERRED_PARTNER`: branch type (company internal use)
- `IS_DEALER`: branch type (company internal use)
- `PARTER_STATE`: address state of garage branch
- `PARTNER_ADDRESS_COUNT`:number of addresses in CRM-system for garage branch
-  ... 13 categorical socio-demografic features that have been bougth from third party supplier ...
- `dist_metres` (sic!): distance in meters from customer home address to garage branch (travel by car)
- `duration_days`: duration of customer relationship from first to last recorded service visits
