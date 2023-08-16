import requests
from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hello_msg: str = "Hello, World!"

settings = Settings()
app = FastAPI()


@app.get("/")
def hello():
    return {"message": f"{settings.hello_msg}"}


@app.get("/data/{id}")
def get_star_wars_data(id):
    try:
        response = requests.get(f"https://swapi.dev/api/people/{id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=500, detail="API Error")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail="Service Unavailable")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data Processing Error")


# TODO: Add new endpoint to return the top 20 people in the Star Wars API with the highest BMI.


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
