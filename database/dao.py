

from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_artisti__per_n_album(num_album):
        conn = DBConnect.get_connection()
        artisti = []
        cursor = conn.cursor(dictionary=True)

        query = """ SELECT ar.id, ar.name
                    FROM album al, artist ar
                    WHERE al.artist_id = ar.id
                    GROUP BY ar.id, ar.name
                    HAVING COUNT(al.id) >= %s
                    ORDER BY ar.id"""

        cursor.execute(query, (num_album,))
        for row in cursor:
            artista = Artist(id=row['id'], name=row['name'])
            artisti.append(artista)
        cursor.close()
        conn.close()
        return artisti


    @staticmethod
    def get_artisti_connessi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        artisti_connessi = []

        query = """ SELECT LEAST(ar1.id, ar2.id) as A1,
                           GREATEST(ar1.id, ar2.id) as A2,
                           COUNT(DISTINCT t1.genre_id) as peso
                    FROM artist ar1, artist ar2, album al1, album al2, track t1, track t2
                    WHERE ar1.id = al1.artist_id
                    AND ar2.id = al2.artist_id
                    AND al1.id = t1.album_id
                    AND al2.id = t2.album_id
                    AND t1.genre_id = t2.genre_id
                    GROUP BY A1, A2"""

        cursor.execute(query)
        for row in cursor:
            artisti_connessi.append([row['A1'], row['A2'], row['peso']])
        cursor.close()
        conn.close()
        return artisti_connessi
