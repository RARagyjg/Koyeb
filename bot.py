from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()  # Start Flask web server to keep alive

# 🔐 Login with session ID
cl = Client()
cl.login_by_sessionid("70016257168%3Ay7O80nMoWm1AVz%3A24%3AAYjQoQ3Z7PHDd4fizbR34umpOu64pDsTbxYzrhuD1g")  # 🔑 Session ID daal do

# 🔹 Specific GC thread ID
THREAD_ID = "2859303934258963"

# 🔹 Messages list
messages = [
    """OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  """,
    """Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙
Oᗰᗩ TEᖇI ᗰᗩ KI ᑭᗩᑎTY ᖴᗩᗪ ᗪᑌ________________________________🌙"""
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
