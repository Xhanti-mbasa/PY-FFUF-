import httpx 
import re
from reader import file_reader

def send_request(url):
    try:
        response = httpx.get(url, timeout=10)

        response_data = {
            "URL": url,
            #"Headers": dict(response.headers),
            "Method": response.request.method,
            "Status": response.status_code,
            "Size": len(response.content),
            "Time": round(response.elapsed.total_seconds(), 3)
        }
        return response_data
    
    except httpx.RequestError as error:
        return {"Error": str(error)}
    
def fuzzer(fuzzed_url):
    word_list = file_reader("wordlist.txt") #Takes the word list and imports it into this function.
    searcher = re.search("fuzz", fuzzed_url, re.I)
    if searcher:
            result = []
            for word in word_list:
                switcher = re.sub(r"fuzz", lambda _: word, fuzzed_url, flags=re.I)
                response = send_request(switcher)
                result.append(response)
                print(result)
                return result
    else:
            print("Invalid URL to fuzz")
            return  []
             
if __name__ == "__main__":
    fuzzer_input = input("Insert fuzzer url: ")
    fuzzer_result = fuzzer(fuzzer_input)
    print(fuzzer_result)
