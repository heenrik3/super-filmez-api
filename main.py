from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from routers.Movies import router as moviesRouter

# Exceptions thrown
from controllers import Error


app = FastAPI()

# origins = ['http://localhost:5173']
origins = ['*']


app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=['*'])

app.include_router(moviesRouter)


app.exception_handler(Error.Error)(Error.exceptionHandler)
app.exception_handler(Exception)(Error.exceptionHandler)

# Bind to all available network interfaces on port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)