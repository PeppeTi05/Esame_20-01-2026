from database.dao import DAO

artist = DAO.get_artisti__per_n_album(5)
print(artist)

artisti_connessi = DAO.get_artisti_connessi()
print(artisti_connessi)