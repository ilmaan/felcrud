import requests
import json


URL = "http://localhost:8000/empl/"

def get_data(id= None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    headers = {'content-Type':'application/json'}


    r = requests.get(url= URL,headers=headers, data = json_data)

    data = r.json()
    print(data)


# get_data()

def post_data():
    data = {
        'name':'pelpendiculal',
        'age':16,
        'city':'Bombay'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    
    r = requests.post(url= URL, headers=headers, data = json_data)

    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id':5,
        'name':'perpendicular',
        # 'bauthor':'Madhav',
        # 'bquantity':'43'
    }

    json_data = json.dumps(data)
    
    headers = {'content-Type':'application/json'}
    r = requests.put(url= URL,headers=headers, data = json_data)

    data = r.json()
    print(data)


# update_data()



def delete_data():
    data = {
        'id':'4'
    }

    json_data = json.dumps(data)
    
    headers = {'content-Type':'application/json'}
    r = requests.delete(url= URL,headers=headers, data = json_data)

    data = r.json()
    print(data)


delete_data()

