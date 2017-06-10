import requests

currentyear = 2017


def get_friends(user_id, fields):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = 'https://api.vk.com/method'
    access_token = ''
    query_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'fields': fields
    }
    query = "{domain}/friends.get?access_token={access_token}" \
            "&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
    response = requests.get(query)
    return response


def age_predict(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    friends = get_friends(user_id, 'bdate')
    friends = list(friends.json()['response']['items'])
    divideby = 0
    age = 0
    for friend in friends:
        try:
            age += currentyear - int(friend['bdate'][-4:])
            divideby += 1
        except:
            pass
    return age / divideby
