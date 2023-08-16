import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseSettings

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

@app.get("/top-people-by-bmi")
def get_top_people_by_bmi():
    get_people_url = "https://swapi.dev/api/people"
    people_list = []

    while get_people_url:

        try:
            response = requests.get(get_people_url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise HTTPException(status_code=500, detail="API Error")
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503, detail="Service Unavailable")
        except (KeyError, ValueError) as e:
            raise HTTPException(status_code=500, detail="Data Processing Error")
        
        # calculate BMI
        people_bmi_list = response.json()['results']
        for people in people_bmi_list:
            try:
                people['bmi'] = float(people['mass']) / float(people['height']) / float(people['height'])
                people_list.append(people)
            except ValueError:
                # just ignore unkown value
                pass

        # update query url
        get_people_url = response.json()['next']
    
    sorted_people_list = sorted(people_list, key=lambda people: people['bmi'], reverse=True) 

    return sorted_people_list[:20]


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
