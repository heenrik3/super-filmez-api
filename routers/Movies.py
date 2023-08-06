from fastapi import APIRouter
from controllers import Movies 

router = APIRouter()    

router.get('/movies')(Movies.getAllMovies)
router.get('/movies/{id}')(Movies.getOneMovie)

