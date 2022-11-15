from source.hintings import DeezerMusicResult

import requests 


class DeezerSearchTrack :

    BASE_URL = "https://api.deezer.com/track?q="

    @classmethod 
    def search(self, querystring:str) -> DeezerMusicResult : 

        query = self.BASE_URL + querystring 
        r = requests.get(query)

        try : 
            result = r.json()['data'][0] 
            m_result = DeezerMusicResult(name=result['title'],
                                         artist=result['artist']['name'], 
                                         cover=result['album']['cover_xl'], 
                                         url=result['link'], 
                                         preview=result['preview'], 
                                         rank = result['rank'])
                                         
            return m_result

        except IndexError : 
            raise IndexError("No result found")

class DeezerSearcArtist :
        
    BASE_URL = "https://api.deezer.com/artist?q="

    @classmethod 
    def search(self, querystring:str) -> DeezerMusicResult : 

        query = self.BASE_URL + querystring 
        r = requests.get(query)

        try : 
            result = r.json()['data'][0] 
            m_result = DeezerMusicResult(name=result['title'],
                                         artist=result['artist']['name'], 
                                         cover=result['album']['cover_xl'], 
                                         url=result['link'], 
                                         preview=result['preview'], 
                                         rank = result['rank'])
                                         
            return m_result

        except IndexError : 
            raise IndexError("No result found")
