from model import Movies
from controllers.Error import Error

async def getAllMovies():
    rawList = await Movies.getAll()

    movies = []

    for movie in rawList:
        movies.append({
            'id': movie['id'],
            'name': movie['name'],
            'img': movie['img'],
            'rating': movie['rating'],
        })

    return {
        'status': 'success',
        'data': movies
    }

async def getOneMovie(id: str):
    movie = await Movies.getOne(id)

    if not movie:
        raise Error('Movie not found for id: %s' % id, 404)
    
    
    return {
        'status': 'success',
        'data': movie
    }

