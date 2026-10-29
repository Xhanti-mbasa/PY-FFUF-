import httpx 

def send_request(url):
    try:
        response = httpx.get(url, timeout=10)

        Response = {
            "URL": url,
            #"Request": response.request,
            #"Method": response.method,
            #"Headers": dict(response.headers),
            "Status": response.status_code,
            "Size": len(response.content),
            "Time": round(response.elapsed.total_seconds(), 3)
        }
        return Response
        #print(f"URL: {url}")
        #print(f"Method: {response.headers}") #Still thinking about this feature
        #heads = {"Method": dict(response.headers)}
        #print(heads)
        #print(f"Status: {response.status_code}")
        #print(f"Size: {len(response.content)} bytes")
        #print(f"Time: {response.elapsed.total_seconds():.3f}s")

    except httpx.RequestError as error:
        print(f"request failed: {error}")

terminal_input = input("Input the url here: ")
result = send_request(terminal_input)
print(result)