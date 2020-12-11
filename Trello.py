import json



class Trello(object):
    # Base Class for Trello API#
    def __init__(self,api_key,api_token)
    self.key = api_key


@app.route('/')
def get_account_details():
    query = {'key': Config.key,'token': Config.token}
    get_base_url = 'https://api.trello.com/1/'

    headers = {
         "Accept": "application/json"
    }  
    try:
        response = requests.get(get_base_url + "members/" + Config.id + '/' , params=query)
        if response.status_code == 200:
            account_list = response.json()
    except Exception as e:
            print (e)
    return account_list

@app.route('/lists')
 # For providing details of list of cards for specific board #
def get_card_details_by_board_id():
    query = {'key': Config.key,'token': Config.token}
    result_flag = False
    get_base_url = 'https://api.trello.com/1/'
    url = get_base_url + '/boards/' + Config.id +'/cards'
    try:
        response = requests.get(url = url , params=query)
        if response.status_code == 200:
            card_list = response.json()
            result_flag = True
    except Exception as e:
            print (e)
    return card_list
