# 📄 sec3_project_pred_Card_Category
- 카드회사의 데이터로 해당데이터들을 통해 어떤 고객이 이탈을할지 예측하는 데이터였으나, 데이터를 통해 카드유형을 예측하는 모델을 만들고, 이를 웹에서 고객이 개인정보를 기입하는 경우, 자신이 발급받을 수 있는 카드의 유형을 확인할 수 있는 서비스를 제작하여 배포하고자 한다.

- 데이터에서 몇몇 칼럼을 뽑아 해당 특성을 통해 카드를 새롭게 발급받을때 카드의 등급을 예측하는 모델을 만들었다

## 📃 Data
- 해당데이터는 Credit Card customers Predict Churning customers데이터 입니다.
- https://www.kaggle.com/sakshigoyal7/credit-card-customers
- URL이 https://leaps.analyttica.com/home 인 웹 사이트에서이 데이터 세트를 얻었습니다.

## 🔠 Columns
- 특성설명
    - Customer_age: 고객연령
    - Gender: 고객성별
    - Deendent_count: 부양가족 수
    - Education_Level: 교육수준
    - Marital_Status: 결혼상태
    - Income_Category : 연소득

## 🖥️ Model
```
LabelEncoder() # 카테고리들의 범주화
Ensemble_pipe = make_pipeline(
    TargetEncoder(),
    SimpleImputer(),
    StandardScaler(), 
    RandomForestClassifier(random_state=2)
)
RandomizedSearchCV() # 최적의 파라미터값을 찾음
```


# 💻 Heroku
- 해당 레포의 헤로쿠 링크입니다.
- https://sec3-proj-tintin.herokuapp.com/

# 🏠 Home
- 해당 웹의 서비스를 설명하고, 사용할 수 있도록 만들어진 기본 페이지입니다.

# 🧍 User
- 사용자가 자신의 정보를 입력하여 데이터베이스에 저장하는 기능을 가진 페이지입니다.
- 사용자는 자신의 정보를 입력 후, 데이터베이스에 저장하여 Predict페이지에서 자신의 결과값을 확인할 수 있습니다.
- 결과값 확인후 User페이지로 돌아와서 자신의 정보를 삭제할 수 있습니다.

# 💳 Predict
- 사용자가 자신의 이름을 입력하여 데이터베이스의 정보를 불러온 후, 카드의종류를 예측하는 기능을 가능 페이지입니다.
- 사용자는 자신의 이름을 입력하고 자신이 발급받게될 카드의 종류의 예상, 즉 결과값을 확인할 수 있습니다.
- 이후 User페이지로 돌아가 자신의 정보를 삭제할 수 있습니다.

# 🖼️ Schema
- 해당 데이터베이스에서 사용되는 테이블의 스키마입니다.
<img width="359" alt="스크린샷 2021-06-02 오후 12 07 16" src="https://user-images.githubusercontent.com/73811590/120418226-14b9cc00-c39b-11eb-8bb7-6e6cf6360bb0.png">

