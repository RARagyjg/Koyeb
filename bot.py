from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()  # Start Flask web server to keep alive

# 🔐 Login with session ID
cl = Client()
cl.login_by_sessionid("YOUR_SESSION_ID_HERE")  # 🔑 Session ID daal do

# 🔹 Specific GC thread ID
THREAD_ID = "YOUR_GC_THREAD_ID_HERE"

# 🔹 Messages list
messages = [
    "tu pagal hai 🤣",
    "tu sudhar ja 🤣",
    "tujhe bahut maruga ❤️"
]

# 🔹 Loop me message send karna
while True:
    msg = random.choice(messages)
    try:
        cl.direct_send(msg, thread_ids=[THREAD_ID])
        print(f"Sent to GC {THREAD_ID}: {msg}")
    except Exception as e:
        print(f"Error sending message: {e}")
    time.sleep(60)  # 1 min interval, adjust as needed
