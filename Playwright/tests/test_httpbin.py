import requests



def test_reques():
    b = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY")
    print(b.status_code)
    
    test_reques()
    