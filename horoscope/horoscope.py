import requests

"""
    Scraping astrology.com without bs4, just by logic and string manipulation.
    AUTHOR: Himanshu Sharma
"""

main_url = "https://www.astrology.com"

def extract_p_tag(html_code):
    a = html_code
    return a[a.find("<p>")+len("<p>"): a.find("</p>"): 1]

def remove_span(html_code):
    a = html_code
    p_tagged = extract_p_tag(a)

    a = p_tagged
    date = a[a.find('">')+len('">'):a.find("</span>"):1]
    text_only = a[a.find("</span>")+len("</span>")::]

    return date+text_only

def get_prediction(zodiac):
    zodiac = zodiac.lower()

    prediction_url = main_url+"/horoscope/daily/{}.html".format(zodiac)
    
    r = requests.get(prediction_url)
    a =  r.text

    return remove_span(a)
