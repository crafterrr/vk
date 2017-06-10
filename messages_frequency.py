import requests
from datetime import datetime
from pprint import pprint as pp
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='', api_key='') # Plotly username and api key go here


def messages_get_history(user_id, offset=0, count=100):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    domain = 'https://api.vk.com/method'
    access_token = ''
    query_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'offset': offset,
        'count': count
    }
    query = "{domain}/messages.getHistory?access_token={access_token}" \
            "&user_id={user_id}&offset={offset}" \
            "&count={count}&v=5.53".format(**query_params)
    response = requests.get(query)
    return response.json()


def count_dates_from_messages(messages):
    messages = messages['response']['items']
    dateslist = []
    datescount = []
    for message in messages:
        date = datetime.fromtimestamp(message['date']).strftime("%Y-%m-%d")
        dateslist.append(date)
    index = -1
    while index + 1 < len(dateslist):
        index += 1
        datescount.append(dateslist.count(dateslist[index]))
        if index + 1 < len(dateslist) \
                and dateslist[index] == dateslist[index + 1]:
            dateslist.pop(index)
    return (dateslist, datescount)

userid = # Target user id goes here
msg = messages_get_history(userid)

try:
    coords = count_dates_from_messages(msg)
    data = [go.Scatter(x=coords[0], y=coords[1])]
    py.iplot(data)
except:
    pass
