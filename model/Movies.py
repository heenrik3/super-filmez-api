movies = [
    {
        'id': 1,
        'name': 'Avatar',
        'img': 'https://m.media-amazon.com/images/M/MV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2009,
        'director': 'James Cameron',
        'rating': 8
    },
    {
        'id': 2,
        'name': 'Vingadores: Ultimato',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2019,
        'director': 'Anthony Russo, Joe Russo',
        'rating': 10
    },
    {
        'id': 3,
        'name': 'Jurassic World',
        'img': 'https://m.media-amazon.com/images/M/MV5BNzQ3OTY4NjAtNzM5OS00N2ZhLWJlOWUtYzYwZjNmOWRiMzcyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2015,
        'director': 'Colin Trevorrow',
        'rating': 7
    },
    {
        'id': 4,
        'name': 'O Rei Leão',
        'img': 'https://m.media-amazon.com/images/M/MV5BMjIwMjE1Nzc4NV5BMl5BanBnXkFtZTgwNDg4OTA1NzM@._V1_.jpg',
        'genre': 'Animação/Aventura/Drama',
        'year': 2019,
        'director': 'Jon Favreau',
        'rating': 8
    },
    {
        'id': 5,
        'name': 'Os Vingadores',
        'img': 'https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2012,
        'director': 'Joss Whedon',
        'rating': 8
    },
    {
        'id': 6,
        'name': 'Harry Potter e a Pedra Filosofal',
        'img': 'https://m.media-amazon.com/images/M/MV5BNmQ0ODBhMjUtNDRhOC00MGQzLTk5MTAtZDliODg5NmU5MjZhXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_QL75_UY281_CR1,0,190,281_.jpg',
        'genre': 'Aventura/Fantasia',
        'year': 2001,
        'director': 'Chris Columbus',
        'rating': 8
    },
    {
        'id': 7,
        'name': 'Star Wars: O Despertar da Força',
        'img': 'https://m.media-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_.jpg',
        'genre': 'Ação/Aventura/Fantasia',
        'year': 2015,
        'director': 'J.J. Abrams',
        'rating': 8
    },
    {
        'id': 8,
        'name': 'Vingadores: Guerra Infinita',
        'img': 'https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2018,
        'director': 'Anthony Russo, Joe Russo',
        'rating': 9
    },
    {
        'id': 9,
        'name': 'Velozes e Furiosos 7',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE@._V1_.jpg',
        'genre': 'Ação/Crime/Thriller',
        'year': 2015,
        'director': 'James Wan',
        'rating': 7
    },
    {
        'id': 10,
        'name': 'Pantera Negra',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2018,
        'director': 'Ryan Coogler',
        'rating': 8
    },
    {
        'id': 11,
        'name': 'Frozen II',
        'img': 'https://m.media-amazon.com/images/M/MV5BMjA0YjYyZGMtN2U0Ni00YmY4LWJkZTItYTMyMjY3NGYyMTJkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_.jpg',
        'genre': 'Animação/Aventura/Comédia',
        'year': 2019,
        'director': 'Chris Buck, Jennifer Lee',
        'rating': 7
    },
    {
        'id': 12,
        'name': 'Transformers: O Lado Oculto da Lua',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTkwOTY0MTc1NV5BMl5BanBnXkFtZTcwMDQwNjA2NQ@@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2011,
        'director': 'Michael Bay',
        'rating': 6
    },
    {
        'id': 13,
        'name': 'O Cavaleiro das Trevas Ressurge',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura',
        'year': 2012,
        'director': 'Christopher Nolan',
        'rating': 9
    },
    {
        'id': 14,
        'name': 'O Senhor dos Anéis: O Retorno do Rei',
        'img': 'https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UX190_CR0,0,190,281_.jpg',
        'genre': 'Aventura/Drama/Fantasia',
        'year': 2003,
        'director': 'Peter Jackson',
        'rating': 9
    },
    {
        'id': 15,
        'name': 'Skyfall',
        'img': 'https://m.media-amazon.com/images/M/MV5BMWZiNjE2OWItMTkwNy00ZWQzLWI0NTgtMWE0NjNiYTljN2Q1XkEyXkFqcGdeQXVyNzAwMjYxMzA@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura/Thriller',
        'year': 2012,
        'director': 'Sam Mendes',
        'rating': 8
    },
    {
        'id': 16,
        'name': 'Transformers',
        'img': 'https://m.media-amazon.com/images/M/MV5BNWI1NjkxM2MtOTU4My00YzQ5LTliNGMtNmFlM2U5NWM3MDY1XkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2007,
        'director': 'Michael Bay',
        'rating': 7
    },
    {
        'id': 17,
        'name': 'Homem-Aranha: Sem Volta para Casa',
        'img': 'https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_QL75_UX190_CR0,0,190,281_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2021,
        'director': 'Jon Watts',
        'rating': 8
    },
    {
        'id': 18,
        'name': 'Harry Potter e a Ordem da Fênix',
        'img': 'https://m.media-amazon.com/images/M/MV5BOTA3MmRmZDgtOWU1Ny00ZDc5LWFkN2YtNzNlY2UxZmY0N2IyXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg',
        'genre': 'Aventura/Fantasia',
        'year': 2007,
        'director': 'David Yates',
        'rating': 8
    },
    {
        'id': 19,
        'name': 'Homem de Ferro 3',
        'img': 'https://m.media-amazon.com/images/M/MV5BMjE5MzcyNjk1M15BMl5BanBnXkFtZTcwMjQ4MjcxOQ@@._V1_.jpg',
        'genre': 'Ação/Aventura/Ficção Científica',
        'year': 2013,
        'director': 'Shane Black',
        'rating': 7
    },
    {
        'id': 20,
        'name': 'Harry Potter e as Relíquias da Morte - Parte 2',
        'img': 'https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg',
        'genre': 'Aventura/Fantasia',
        'year': 2011,
        'director': 'David Yates',
        'rating': 9
    },
    {
        'id': 21,
        'name': 'Toy Story 4',
        'img': 'https://m.media-amazon.com/images/M/MV5BMTYzMDM4NzkxOV5BMl5BanBnXkFtZTgwNzM1Mzg2NzM@._V1_.jpg',
        'genre': 'Animação/Aventura/Comédia',
        'year': 2019,
        'director': 'Josh Cooley',
        'rating': 8
    }
]

for movie in movies:

    genre = []
    for g in movie['genre'].split('/'):
        genre.append(g.strip())

    movie['genre'] = genre
    movie['description'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lobortis neque sed varius porttitor. Aliquam scelerisque nec neque eu cursus. Duis ornare sed mauris nec dapibus. Etiam pulvinar ullamcorper leo, ut iaculis est ornare facilisis. Quisque semper faucibus feugiat. Sed blandit luctus fringilla. Nullam et lobortis lacus. Phasellus ut suscipit mauris. '




async def getAll():
    return [*movies]

async def getOne(id):
    
    found = False

    for m in movies:
        
        if m['name'] == id:
            found = m
            break
    
    return found