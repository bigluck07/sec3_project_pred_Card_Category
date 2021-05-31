from flask import Blueprint, request, redirect, url_for, Response
from credit_card.models import user_model
from credit_card.models.user_model import get_user, User, delete_user, get_user1

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['POST'])
def add_user():
    username = request.form.get('username', None)
    age = request.form.get('age', None)
    gender = request.form.get('gender', None)
    dependent = request.form.get('dependent', None)
    Edu_Level = request.form.get('Edu_Level', None)
    marige = request.form.get('marige', None)
    income = request.form.get('income', None)

    # if username is None:
    #   return "need infomation", 400
    # elif get_user(username) == True:
    #   return redirect(url_for('main.user_index')), 200
    # elif get_user(username) == False:
    #   raw_user = {'username':username, 'age':age, 'gender':gender, 'dependent':dependent, 'Edu_Level':Edu_Level, 'marige':marige, 'income':income}
    #   user_model.add_user(raw_user)
    #   return redirect(url_for('main.user_index', msg_code=0), code=200)
    # user_model.add_user(raw_user) # user_model에 raw_user받아서 add_user해라
    # return redirect(url_for('main.user_index', msg_code=0), code=200)
    user_raw = {'username':username, 'age':age, 'gender':gender, 'dependent':dependent, 'Edu_Level':Edu_Level, 'marige':marige, 'income':income}
    if not username:
      # no username key
      return "Needs username", 400
    elif not user_raw:
      # username doesn't exist on Twitter
      return redirect(url_for('main.user_index'), code=400)
    elif not user_model.get_one_user(target_name=username):
      # username not in db -> add user & add tweets
      user_model.add_user(user_raw)
      return redirect(url_for('main.user_index', msg_code=3), code=200)
    else:
      return redirect(url_for('main.user_index', msg_code=3), code=200)


@bp.route('/user/')
@bp.route('/user/<int:user_id>')
def delete_user(user_id=None):
  """
  delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.

   요구사항:
    - HTTP Method: `GET`
    - Endpoint: `api/user/<user_id>`

  상황별 요구사항:
    -  `user_id` 값이 주어지지 않은 경우:
      - 리턴값: 없음
      - HTTP 상태코드: `400`
    - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
      - 리턴값: 없음
      - HTTP 상태코드: `404`
    - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
      - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
      - HTTP 상태코드: `200`
    """
  if user_id == None:
    return "", 400
  elif get_user1(user_id) == None:
    return "", 404
  else:
    user_model.delete_user(user_id)
  return redirect(url_for('main.user_index', msg_code=3), code=200), 200
