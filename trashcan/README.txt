This project consists of 3 ipynb that are numbered 1, 2, 3:

1) data preparation
2) EDA
3) Cleaning / Preprocessing, Modelling and Evaluation

Only 2 and 3 are relevant for the project evaluation. The first contains data preparation that is out of scope.

Generic plot functions for EDA are saved to a file called 'funEDA.py'. Generic cleaning functions that can be reused 
on any given dataset, were directly written in a separate file 'funCleaning.py'. Cleaning functions that are specific 
to this dataset were first written in the EDA ipynb and then saved to a separate file 'funChurn.py' for later reload 
during preprocessing.

Libraries used in this project:

import numpy as np
import pandas as pd
import datetime
from tqdm import tqdm, tqdm_notebook
import funCleaning, funEDA, funChurn  # files with helper functions, provided
import matplotlib.pyplot as plt
import seaborn
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import cross_validate, StratifiedKFold, GridSearchCV, StratifiedShuffleSplit, learning_curve
from sklearn.feature_selection import SelectFromModel, RFECV
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.metrics import make_scorer, fbeta_score, average_precision_score,  roc_curve, roc_auc_score, \
    precision_recall_curve, confusion_matrix
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier