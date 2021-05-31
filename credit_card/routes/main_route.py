from flask import Blueprint, render_template, request
from credit_card.models.user_model import get_users, User
from credit_card.utils import main_funcs

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/user')
def user_index():
    """
    사용자의 정보를 받아주세요
    """
    msg_code = request.args.get('msg_code', None)
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    user_list = get_users()
    
    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)


@bp.route('/predict')
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
        }

    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    return render_template('predict.html')
    # json_dict = request.get_json()
    # username = request.form.get('username', None)
    # user_info = User.query.filter(User.username == username).first()

    # try: 
    #     users = {
    #             "id": [user_info.user_id],
    #             "username": [user_info.username]
    #             }    
    # except:
    #     users = []

    # if request.method == "POST":
    #     try:
    #         result = main_funcs.predict_card(user_info)
    #     except:
    #         result, compare_text = None
    #     prediction = {'result':result}
        
    # return render_template('predict.html', users=users, prediction=prediction), 200
