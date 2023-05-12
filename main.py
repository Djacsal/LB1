import Parser

if __name__ == '__main__':
    Parser.scrape_flats()
    Parser.save_to_excel('flats.xlsx')
