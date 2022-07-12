class Media():
    def create_news(self, place, name, coordinates:list = ['Mars', 'Upiter', 'Earth']):
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')
        for value in coordinates:
            print(f'{value} get our info!')