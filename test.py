import re

wordlist = ['admin', 'boss', 'cat']
string_container = "https://www.example.co.za/FuZZ?user-id=1&uid=25367"

searcher = re.search(r"FUZZ", string_container, re.IGNORECASE)

if searcher:
    for word in wordlist:
        switcher = re.sub(r"FUZZ", lambda _: word, string_container, flags=re.IGNORECASE)
        print(switcher)
else:
    print("URL must contain FUZZ")