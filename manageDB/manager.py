import requests

url = "http://127.0.0.1:8000"

def reset_users():
    try:
        response = requests.put(url+"/reset_users")
        print(response.content)
    except Exception as e:
        print(f"Error while resetting users: {e}")

def edit_user(user):
    update = {}
    while True:
        key = input("feild: ")
        if key == 'end': break
        val = input("new val: ")
        update[key] = val

    try:
        response = requests.put(url, json= {"user_name": user, "update": update})
        print(response.content)
    except Exception as e:
        print(f"Error while resetting users: {e}")


if __name__ == "__main__":
    while True:
        operation = int(input("operation (1: reset users, 2: edit user, 3: edit event, 4: insert user, 5: insert event) : "))
        if operation == 1:
            reset_users()
        elif operation == 2:
            user = input("user name: ")
            edit_user(user)
        elif operation == 3:
            pass