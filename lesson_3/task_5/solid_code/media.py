class Media():
    def create_news(self, place, name):
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')