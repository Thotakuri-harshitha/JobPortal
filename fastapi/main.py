from fastapi import FastAPI
import json

app = FastAPI()


# uvicorn main:app --reload --port 8080


# ============================================================
# GET OPERATION - Get all users
# ============================================================

@app.get("/get_all_users")
def get_data():

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    print(all_users)

    return all_users


# ============================================================
# POST OPERATION - Create a new user
# ============================================================

@app.post("/create_user")
def post_data(new_user: dict):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    all_users.append(new_user)

    with open("users.json", "w") as w_file:
        json.dump(all_users, w_file, indent=4)

    return {
        "msg": "User created successfully"
    }


# ============================================================
# DELETE OPERATION - Delete user using email
# ============================================================

@app.delete("/delete_user/{email}")
def delete_user(email: str):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:

            all_users.remove(user)

            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file, indent=4)

            return "Successfully deleted and data updated"


    return "No valid user found"


# ============================================================
# PUT OPERATION - Update user using email
# ============================================================

@app.put("/update_user/{email}")
def edit_user(email: str, update_data: dict):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:

            user["name"] = update_data["name"]
            user["password"] = update_data["password"]

            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file, indent=4)

            return "User updated successfully"


    return "No user found with provided email"


# ============================================================
# GET OPERATION - Get single user
# Query Parameter
# ============================================================

@app.get("/users")
def get_single_user(email: str):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:
            return user


    return "No user found"
