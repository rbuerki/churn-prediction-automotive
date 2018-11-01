# blogPost-Churn
A repository containing code and data for a churn prediction project in the automotive service business.

It is a stringent revision of a bigger project done by myself and is basis for a blog publication on Medium. 
To write such an article is a task in Udacity's Data Science program. The article can be found [here]
(https://medium.com/@raph_91654/predict-churn-retain-your-customers-39cc62c322ed). It contains the main findings in 5 min read.

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

Template code is provided in the `blog_automotiveChurn.ipynb` notebook file. 
It requires the `churnData.csv` dataset file to run. 

### Run

In a terminal or command window, navigate to the top-level project directory (the one that contains this README) 
and run one of the following commands:

```bash
ipython notebook finding_donors.ipynb
```  
or
```bash
jupyter notebook finding_donors.ipynb
```

This will open the iPython Notebook software and project file in your browser.

### Data

The dataset consists of approximately 50,000 data points (=cars), with each datapoint having 43 features. 
This dataset is a pre-cleaned version of the original dataset given to me by a large european automotive retail group.

**Target Variable**
- `target_event`: customer status ('CHURN', 'ACTIVE')

**Features**
- `NUM_CONSEC_SERVICES`: number of consequtive service events for a car
- 'SUM_INVOICE_AMOUNT': sum of invoice amount that have been charged for all service events
- 'NUM_EVENTS': total number of service visits
- 'LAST_MILEAGE': mileage recorded at last visit
- 'MEAN_MILEAGE_PER_MNTH': calculated mean mileage per month 
- 'age_mnth': a car's age in months
- 'INSPECTION_INTERVAL_UID': timespan a car has to show up for mandatory service in months
- 'LIST_PRICE': car price
- 'CAR_BRAND_UID': car brand
- 'FUEL_TYPE_UID': fuel type
- 'GEAR_TYPE_UID': gear type
- 'WHEEL_DRIVE_UID': wheel drive type
- 'NUMBER_OF_DOORS': number of doors
- 'GEAR_COUNT': gear count
- 'BASE_MARGIN': base margin for dealer
- 'SALES_TYPE': car model
- 'PERSON_LANGUAGE_UID': language of car owner
- 'PERSON_STATE': address state of car owner
- 'PERSON_ADDRESS_COUNT':number of addresses in CRM-system for car owner
- 'ownerAge': age of car owner
- 'REGION_UID': address region of car owner
- 'PARTNER_LANGUAGE_UID': language of garage branch the car is affiliated with
- 'IS_PREFERRED_PARTNER': branch type (company internal use)
- 'IS_DEALER': branch type (company internal use)
- 'PARTER_STATE': address state of garage branch
- 'PARTNER_ADDRESS_COUNT':number of addresses in CRM-system for garage branch
-  ... 13 categorical socio-demografic features that have been bougth from third party supplier ...
- 'dist_metres' (sic!): distance in meters from customer home address to garage branch (travel by car)
- 'duration_days': duration of customer relationship from first to last recorded service visits
