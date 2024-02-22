from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bcrypt
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
app = FastAPI()

# Dummy database to store user data
db = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


class UserSignup(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    username: str
    hashed_password: str



@app.post("/signup")
async def signup(user: UserSignup):
    if user.username in db:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db[user.username] = UserInDB(username=user.username, hashed_password=hashed_password)
    return JSONResponse(content={"message": "User created successfully"})


@app.post("/login")
async def login(user: UserLogin):
    if user.username not in db:
        raise HTTPException(status_code=401, detail="Invalid username")

    stored_user = db[user.username]

    # Check if the provided password matches the stored hashed password
    if not bcrypt.checkpw(user.password.encode('utf-8'), stored_user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
