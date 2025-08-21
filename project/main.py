from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()
movies=[] 

class Movie(BaseModel):
    id:int
    title:str
    genre:str

@app.get("/")
def root():
    return {"message":"Welcome to the Movie API"}

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movies(movie_id: int):
    for movie in movies:
        if movie["id"]==movie_id:
            return movie
        raise HTTPException(status_code=404,detail="Movie not Found")

@app.post("/movies")
def post_movies(movie:Movie):
    movies.append(movie.dict())
    return {"message":"Movie added Successfully","movie": movie}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id:int):
    for movie in movies:
        if movie["id"]==movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted successfully"}
        raise HTTPException(status_code=404,detail="Movie not found")
    