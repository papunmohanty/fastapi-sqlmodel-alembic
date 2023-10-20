from fastapi import Depends, FastAPI
from sqlmodel import select
# from sqlmodel import Session  #Old: Sync session import
from sqlmodel.ext.asyncio.session import AsyncSession #New: Async session import

from app.db import get_session, init_db
from app.models import Song, SongCreate


app = FastAPI()


# Old: Sync start up event
# @app.on_event("startup")
# def on_start():
#     init_db()

# New: Async start event
# Removeed: the start-up event on startup the app
# because, we need to put this functionality during
# migration process.
# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [
        Song(
            name=song.name,
            artist=song.artist,
            year=song.year,
            id=song.id
        ) for song in songs
    ]


@app.post("/songs")
async def add_song(
    song: SongCreate, session: AsyncSession = Depends(get_session)
):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
