from flask import Blueprint, request, redirect, url_for, Response
from credit_card.models import user_model
from credit_card.models.user_model import get_user, User, delete_user, get_user_id

bp = Blueprint('user', __name__)


@bp.route('/api/user', methods=['POST'])
def add_user():
    username = request.form.get('username', None)
    age = request.form.get('age', None)
    gender = request.form.get('gender', None)
    dependent = request.form.get('dependent', None)
    Edu_Level = request.form.get('Edu_Level', None)
    marige = request.form.get('marige', None)
    income = request.form.get('income', None)
    # breakpoint()
    # user_raw = {'username':username, 'age':age, 'gender':gender, 'dependent':dependent, 'Edu_Level':Edu_Level, 'marige':marige, 'income':income}
    # print("requests.form name: " + request.form.get('username'))
    # print(request.json['username'])
    if username is None:
      return "need infomation", 400
    elif get_user(username) == True:
      return redirect(url_for('main.user_index'), msg_code=1), 200
    # elif get_user(username) == True:
    elif get_user(username) == False or get_user(username)==None:
      # breakpoint()
      raw_user = {'username':username, 'age':age, 'gender':gender, 'dependent':dependent, 'Edu_Level':Edu_Level, 'marige':marige, 'income':income}
      user_model.add_user(raw_user)
      return redirect(url_for('main.user_index', msg_code=0), code=200)


@bp.route('/api/user/')
@bp.route('/api/user/<int:user_id>')
def delete_user(user_id=None):
  '''
  user_id 값이 입력되면 user_model.delete_user함수를 실행시킨 후 결과를 보여준다.
  '''
  if user_id == None:
    return "", 400
  elif get_user_id(user_id) == None:
    return "", 404
  else:
    user_model.delete_user(user_id)
  return redirect(url_for('main.user_index', msg_code=2), code=200), 200
