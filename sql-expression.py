from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinbook" db
db = create_engine("postgresql://chinbook")

meta = MetaData(db)

#creat variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistID", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
artist_table = Table(
    "Album", meta
)

# making the connection
with db.connect() as connection: