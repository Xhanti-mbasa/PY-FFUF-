import httpx 

def send_request(url):
    try:
        response = httpx.get(url, timeout=10)

        print(f"URL: {url}")
        #print(f"Method: {response.headers}") #Still thinking about this feature
        print(f"Status: {response.status_code}")
        print(f"Size: {len(response.content)} bytes")
        print(f"Time: {response.elapsed.total_seconds():.3f}s")

    except httpx.RequestError as errors:
        print(f"request failed: {error}")

send_request("https://ai.wethinkcode.co.za/survey-for-professionals?name=Mr.%20Xhanti%20Daka&email=xhmohcpt025@student.wethinkcode.co.za")