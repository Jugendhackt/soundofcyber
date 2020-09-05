from fastapi import FastAPI
import motor.motor_asyncio

DATABASE_URL = "mongodb://localhost:27017"

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["soundofcyber"]
userrules = db["userrules"]
allpis = db["allpis"]
rawdata = db["rawdata"]
usermusic = db["usermusic"]


@app.post("/test")
async def test_this_app():
    return {'test': True}