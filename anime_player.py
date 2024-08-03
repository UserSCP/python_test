from animeflv import AnimeFLV
from animeflv.exception import AnimeFLVParseError
"""
la api que uce
git clone https://github.com/UserSCP/animeflv-api.git
cd animeflv-api
pip install -r requirements.txt
pip install .
"""
with AnimeFLV() as api:
    try:
        search_query = input("Escribe serie: ")
        elements = api.search(search_query)
        for i, element in enumerate(elements):
            print(f"{i}. {element.title}")       
        selection = int(input("Selecciona una opción: "))
        if selection < 0 or selection >= len(elements):
            raise ValueError("Selección fuera de rango.")
        info = api.get_anime_info(elements[selection].id)
        if not info or not info.episodes:
            raise ValueError("No se pudo obtener información de la serie o no hay episodios disponibles.")
        info.episodes.reverse()
        for j, episode in enumerate(info.episodes):
            print(f"{j}. Episode - {episode.id}")
        index_episode = int(input("Selecciona un episodio: "))
        if index_episode < 0 or index_episode >= len(info.episodes):
            raise ValueError("Índice de episodio fuera de rango.")
        serie = elements[selection].id
        capitulo = info.episodes[index_episode].id
        results = api.get_links(serie, capitulo)
        if not results:
            raise ValueError("No se encontraron enlaces para el episodio seleccionado.")
        for result in results:
            print(f"{result}")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except IndexError as ie:
        print(f"Error de índice: {ie}")
    except AnimeFLVParseError as ap:
        print(f"Error de análisis de API: {ap}")
    except Exception as e:
        print(f"Error: {e}")
