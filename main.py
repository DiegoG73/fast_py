from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Learning FastAPI", description="A first steps API", version="0.0.1"
)

movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "overview": "The Godfather It's a movie from 1972 directed by Francis Ford Copola",
        "year": "1972",
        "rating": 9.2,
        "category": "Crime",
    },
    {
        "id": 2,
        "title": "Batman Begins",
        "overview": "Batman Begins It's a movie directed by Christopher Nolan",
        "year": "1972",
        "rating": 9,
        "category": "Super heroes",
    },
    {
        "id": 3,
        "title": "Oppenheimer",
        "overview": "It's a movie from 2023 directed by Christopher Nolan",
        "year": "2023",
        "rating": 10,
        "category": "Biographical",
    },
]


# * Creating the first endpoint with a decorator included:
@app.get("/", tags=["start"])
def read_root():
    return HTMLResponse("<h2> Hello cruel world! </h2>")


# * Creating an endpoint to create a movie list
@app.get("/movies", tags=["Get Movies"])
def get_movies():
    return movies
