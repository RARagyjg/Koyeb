from instagrapi import Client
import time
from keep_alive import keep_alive

keep_alive()  # Start Flask web server to keep alive

cl = Client()

# Retry OFF — duplicate messages ka main reason yahi tha
cl.request_timeout = 5
cl.configure_retries(0)

# Login
cl.login_by_sessionid("70016257168%3Ay7O80nMoWm1AVz%3A24%3AAYjQoQ3Z7PHDd4fizbR34umpOu64pDsTbxYzrhuD1g")

# GC Thread ID
THREAD_ID = "2859303934258963"

# Single message
msg = """OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  """

# Loop
while True:
    try:
        cl.direct_send(msg, thread_ids=[THREAD_ID])
        print(f"Sent to GC {THREAD_ID}: {msg}")
    except Exception as e:
        print(f"Error sending message: {e}")

    time.sleep(60)  # EXACT 60 sec delay
