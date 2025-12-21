"""
This case demonstrates building a web service using Starlette
"""
import requests
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route
#The API address for Hitokoto
url = 'https://international.v1.hitokoto.cn'

#Define an asynchronous function to fetch a random quote
async def get_hitoko():
    try:
        #Request parameters:Special content type(e.g., 'a'for Animation) and format
        params = {'c':'a','encode':'json'}
        response = requests.get(url,params=params)
        status_code  = response.status_code
        if status_code == 200:
            data = response.json()
            hitokoto = data['hitokoto']
            from_who = data['from_who'] if data['from_who'] else 'Unknown'
            return {'hitokoto':hitokoto,'from_who':from_who}
        else:
            return {'error':f'Request failed with status code {status_code}'}
    except requests.exceptions.RequestException as e:
        return {'error':str(e)}

#Define an asynchronous function to handle requests to the root path
async def homepage(request):
    result = await get_hitoko()
    return JSONResponse(result)

#Create a Startlette application instance
app = Starlette(routes=[Route('/', homepage),])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)