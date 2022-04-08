from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import pprint
import sys
#pretty printer for json files
pp = pprint.PrettyPrinter(indent=4)

def main():
    #Initial interface for current year or custom year by user input
    print('Press 1 for the top 50 movies of this year, or 2 to input a specific year')
    user_inp = input()
    if user_inp == '1':
        year = int(datetime.datetime.now().year)
    elif user_inp == '2':
        year = int(input('Which year''s top 50 Movies would you like to look at?'))
    else:
        print('Invalid input')
        quit()
    
    #scraping location
    sys.stdout = open('imdb web scraper\Top50Data\IMDB_Top_50_' + str(year) + '.json', 'w')
    url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), features = "html.parser")
    dataset_top50 = {}
    id = 1
    #find all within div tags with class lister item content
    movies_list = soup.findAll('div', attrs = {'class':'lister-item-content'})
    for each in movies_list:
        #each movie type
        movie_item = {
            'name' : '',
            'certificate': '',
            'runtime': '',
            'genre': '',
            'description': '',
            'director': '',
            'stars': []
        }
        #h3 tag with lister-item-header class
        if each.find('h3', attrs = {'class':'lister-item-header'}).find('a').text:
            name_value = each.find('h3', attrs = {'class': 'lister-item-header'}).find('a').text.strip()
            movie_item['name'] = name_value

        p_list = each.findAll('p')

        if p_list[0]:
            if p_list[0].find('span', attrs={'class':'certificate'}):
                certificate_value = p_list[0].find('span', attrs={'class':'certificate'}).text.strip()
                movie_item['certificate'] = certificate_value

            if p_list[0].find('span', attrs={'class':'runtime'}):
                runtime_value = p_list[0].find('span', attrs={'class':'runtime'}).text.strip()
                movie_item['runtime'] = runtime_value

            if p_list[0].find('span', attrs={'class':'genre'}):
                genre_value = p_list[0].find('span', attrs={'class':'genre'}).text.strip()
                movie_item['genre'] = genre_value

        if p_list[1]:
            description_value = p_list[1].text.strip()
            movie_item['description'] = description_value

        if p_list[2]:
            director_value = p_list[2].findAll('a')[0].text.strip()
            movie_item['director'] = director_value
            stars_list = p_list[2].findAll('a')[1:]
            stars_value = []
            for each in stars_list:
                stars_value += [each.text.strip()]
            movie_item['stars'] = stars_value

        dataset_top50[id] = movie_item
        id += 1
    #print onto external json file
    print(json.dumps(dataset_top50, indent = 4))
    pp.pprint('-------------------------------------------------')
    pp.pprint(f"The top 5 movies of {year} are:")
    for i in range(1,6):
        pp.pprint(f"{i}: " + dataset_top50[i]['name'])

if __name__ == "__main__":
    main()
        