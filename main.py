import httpx 
#from reader import file_reader

def send_request(url):
    try:
        response = httpx.get(url, timeout=10)

        response_data = {
            "URL": url,
            "Headers": dict(response.headers),
            "Method": response.request.method,
            "Status": response.status_code,
            "Size": len(response.content),
            "Time": round(response.elapsed.total_seconds(), 3)
        }
        return response_data
    
    except httpx.RequestError as error:
        return {"Error": str(error)}
    
terminal_input = input("Input the url here: ")
result = send_request(terminal_input)
print(result)