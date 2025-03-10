import requests
import time
import random
from playsound import playsound
import buyTicket
import config
import os

api_url = config.api_url
target_session_id = config.target_session_id
sound_file = sound_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'alarm.mp3')

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
]

headers = {
    "User-Agent": random.choice(user_agents),
    "Referer": "https://ztwen.jussyun.com/pc"
}

def check_tickets():
    retries = 3 
    for attempt in range(retries):
        try:
            response = requests.get(api_url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                sessions = data.get("data", {}).get("sessionVOs", [])

                for session in sessions:
                    if session.get("bizShowSessionId") in target_session_id:
                        status = session.get("sessionStatus")
                        soldOut = session.get("hasSessionSoldOut")
                        if status != "LACK_OF_TICKET" and soldOut == True:
                            global count
                            print(f"❌ No tickets available! Attempt #{str(count)}")
                            count += 1
                        else:
                            print("✅ Tickets might be available!")
                            buyTicket.buyTicket()
                            global haveTicket
                            haveTicket = True
                            for _ in range(10):
                                playsound(sound_file)
                            return
                break
            else:
                print("❌❌❌ Error fetching data:", response.status_code)
                break
        except requests.exceptions.RequestException as e:
            print(f"❌ Error on attempt {attempt + 1}: {e}")
            if attempt < retries - 1:
                print(f"Retrying in 3 seconds...")
                time.sleep(3)

count = 1
haveTicket = False
while True and not haveTicket:
    check_tickets()
    wait_time = random.uniform(0, 0.1)
    time.sleep(wait_time)

print("Sleeping for 60 minutes")
time.sleep(3600)
print("FINISHED")