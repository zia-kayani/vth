## user credentials for login 
import os
LOGINCREDENTIALS = {
   "USERNAME" : os.getenv("USERNAME"),
   "PASSWORD" : os.getenv("PASSWORD"),
   "NEW_PASSWORD" : os.getenv("NEW_PASSWORD"),
   
}
if not all(LOGINCREDENTIALS.values()):
    raise RuntimeError("Missing environment variables. Check your .env file.")