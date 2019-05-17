import scrapy, json, os
from collections import OrderedDict

class PokemonSpider(scrapy.Spider):

    name = 'pokemon'

    def start_requests(self):
        yield scrapy.Request(url = 'https://pokemondb.net/pokedex/national', callback = self.parse)

    def parse(self, response):
        # pokemon_name = response.css('span.infocard-tall .ent-name::text').extract()
        pokemons = []
        pokemon_cards = response.css('span.infocard-tall')
        
        if pokemon_cards is not None:
            for pokemon in pokemon_cards:
                p_id = pokemon.css('small::text').extract_first()
                p_name = pokemon.css('.ent-name::text').extract_first()
                p_aside = pokemon.css('small.aside')
                p_categories = p_aside.css('a::text').extract()
                p_link = 'https://pokemondb.net/pokedex/%s' % (p_name.lower())

                p_line = OrderedDict()
                p_line['id'] = p_id,
                p_line['name'] = p_name,
                p_line['link'] = p_link,
                p_line['categories'] = p_categories
                
                pokemons.append(p_line)
            
            f = open('pokemons.json', 'wb')
            f.write(json.dumps(pokemons))
            f.close()    

        self.log('POKEMON: %s' % type(pokemon_cards[0].css('small::text').extract_first()))
