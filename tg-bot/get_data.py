from bs4 import BeautifulSoup
import requests as req
import time


## ///   START GLOBAL_VARIABLES   ///


holidays            = ['den-rozhdeniya/', 'lyubov/', 'prazdniki/8-marta/', 'prazdniki/noviy-god/']
picture             = 'kartinki/'
base                = "https://pozdravok.com/pozdravleniya/"

expansion_page      = ".htm"
expansion_text      = ".txt"
expansion_pic       = ".gif"

files               = ['birthday/', 'love/', '8_march/', 'new_year/']
dir                 = 'congratulation/'
dir_pic             = 'congratulation_pic/'

site                = 'https://pozdravok.com/'
START_INDEX_PAGE    = 2
NUMBER_TEXT_PAGE    = 4
NUMBER_PICTURE_PAGE = 9
NUMBER_HOLIDAY      = len(holidays)

## /// END GLOBAL_VARIABLES   ///


## /// FUNCTION CREATES FILE NAME FOR TEXT AND PICTURE FILES   ///


def get_file_name(string_front, string_back, index):
    if index < 10:
        return string_front + '0' + string_back
    
    return string_front + string_back


## /// FUNCTION MAKES REQUESTS TO URL (SITE) AND RETURN LXML DOCUMENT ///


def get_soup(url):
    resp = req.get(url)
    time.sleep(3)
    soup = BeautifulSoup(resp.text, 'lxml')

    return soup


## /// FUNCTION WRITES ONE TEXT CONGRATULATION TO ONE FILE


def write_text(i, index, tag):
    file_name = get_file_name(dir + files[i], str(index) + expansion_text, index)
    f = open(file_name, 'w')
    f.write(tag.text)
    f.close()


## /// FUNCTION SAVES ONE PICTURE CONGRATUlATION 


def write_pic(i, index, link):
    lnk = link["src"]
    print(lnk)

    if lnk[-3:-1] == "gi":
        file_name = get_file_name(dir_pic + files[i], str(index) + expansion_pic, index)
        f = open(file_name, 'wb')
        f.write(req.get(site + lnk).content)
        f.close()

        return 0

    return 1


## /// FUNCTION MAKES DATA WITH TEXT AND PICTURE


def get_data(prefix, data_tag, class_name, write_data, number_pages):
    for i in range(NUMBER_HOLIDAY):
        index = 0
        soup = get_soup(base + holidays[i] + prefix)

        for tag in soup.find_all(data_tag, {"class": class_name}):
            write_data(i, index, tag)
            index += 1
        
        for j in range(START_INDEX_PAGE, START_INDEX_PAGE + number_pages):
            soup = get_soup(base + holidays[i]  + prefix + str(j) + expansion_page)

            for tag in soup.find_all(data_tag, {"class": class_name}):
                write_data(i, index, tag)
                index += 1


# ///   USE THIS FUNCTION TO MAKE PICTURE FILES    ///


# get_data(picture, 'img', 'kartinki', write_pic, NUMBER_PICTURE_PAGE)


# ///   USE THIS FUNCTION TO MAKE TEXT FILES    ///


# get_data('', 'p', 'sfst', write_text, NUMBER_TEXT_PAGE)


