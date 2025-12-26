import os

API_ID = API_ID =  29978901

API_HASH = os.environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8464714544:AAF7cN9yIE_JoLap0HsjXlEhuGCKspr-jtw")

PASS_DB = int(os.environ.get("PASS_DB", "mongodb+srv://rupakaryanaryan:rupakaryanaryan@cluster0.05xkjx2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5776977809").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


