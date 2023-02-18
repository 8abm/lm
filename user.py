import requests,random

def h():

     while True:

            user1 = str("".join(random.choice('qwertyuioplkjhgfdsamnbvcxz_')for x in range(1)))

            user2 = str("".join(random.choice('qwert.yui.oplkjhgf_dsamn.bvcxz')for x in range(1)))

            user3 = str("".join(random.choice('abcdefghijklmnopqrstuvwxyz1234567_890._')for x in range(1)))

            user4 = str("".join(random.choice('qwert_yuioplkjhg_fdsamnbvcxz1234_567890')for x in range(1)))

            user = user1+user2+user3+user4

            req = requests.get(f"https://ip-info.aliasd5.repl.co/?user={user}").text

            if "True" in req:

                    requests.get("https://api.telegram.org/bot2007239629:AAE6giqboLt0ScMl6wbTTONPhI2k1jsD8m8/sendMessage?chat_id=1934060947&text="+user)

                    print(f"{user} ✅")

            else:

                print(f"{user} ❌")

h()
