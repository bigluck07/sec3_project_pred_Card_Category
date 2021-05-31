import os
import csv
from sklearn.linear_model import LogisticRegression
from category_encoders import TargetEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import pandas as pd
import numpy as np
from credit_card.models.user_model import get_user

# 예측모델
CSV_FILEPATH = os.path.join(os.getcwd(), 'twit_app', 'BankChurners.csv')
def predict_card(username):
    data = pd.read_csv('BankChurners.csv')
    columns = ['Card_Category', 'Customer_Age', 'Gender', 'Dependent_count', 'Education_Level', 'Marital_Status', 'Income_Category']
    A_data = data[columns]
    label = A_data['Card_Category']
    p_data = A_data.drop('Card_Category', axis=1)
    def make_num(col):
        for i in range(0, 10127):
            if col[i] == 'Platinum':
                col[i] = '3'
            elif col[i] == 'Silver':
                col[i] = '2'
            elif col[i] == 'Gold':
                col[i] = '1'
            else:
                col[i] = '0'
        return col
    make_num(label)
    Lasbel_en = LabelEncoder()
    p_data['Gender'] = Lasbel_en.fit_transform(p_data['Gender'].values)
    p_data['Education_Level'] = Lasbel_en.fit_transform(p_data['Education_Level'].values)
    p_data['Marital_Status'] = Lasbel_en.fit_transform(p_data['Marital_Status'].values)
    p_data['Income_Category'] = Lasbel_en.fit_transform(p_data['Income_Category'].values)

    X_train, X_test, y_train, y_test = train_test_split(p_data, 
                                                        label, 
                                                        test_size = 0.2, 
                                                        shuffle = True, 
                                                        random_state = 2)
    X_train, X_val, y_train, y_val = train_test_split(X_train, 
                                                        y_train, 
                                                        test_size = 0.25, 
                                                        shuffle = True, 
                                                        random_state = 2)

    Ensemble_pipe = make_pipeline(
        TargetEncoder(min_samples_leaf=4, smoothing=500.0), 
        SimpleImputer(strategy='mean'), 
        StandardScaler(), 
        RandomForestClassifier(random_state=2, max_depth=6, max_features=0.29, n_jobs=-1, n_estimators=233)
    )
    Ensemble_pipe.fit(X_train,y_train)
    user = get_user(username)
    ex = {'Customer_Age':[0, user.age], 'Gender':[0, user.gender], 'Dependent_count':[0, user.dependent]
      , 'Education_Level':[0, user.Educ_Level], 'Marital_Status':[0, user.marige], 'Income_Category':[0, user.income]}
    ex = pd.DataFrame(data=ex)
    prediction = Ensemble_pipe.predict_proba(ex)[1]

    print(f"Prediction Results {prediction[0]}")
    return prediction

def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'User does not exist',
            'warning'
        ),
        (
            'Unable to retrieve tweets',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }


