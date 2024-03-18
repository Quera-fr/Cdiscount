from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def get_all_products(input_user):

    # Ouverture du navigateur
    driver = webdriver.Chrome()

    # Ouverture de la page Cdiscount
    driver.get("https://www.cdiscount.com/")

    # Accepter les cookies
    time.sleep(2)
    driver.find_element(By.ID, 'footer_tc_privacy_button_2').click()

    # Recherche en fonction de l'input utilisateur
    driver.find_element(By.ID, 'search').send_keys(input_user)
    driver.find_element(By.ID, 'search').send_keys(Keys.ENTER)


    # All products 
    products = driver.find_elements(By.CLASS_NAME, 'jsPrdBlocContainer')

    dict_all_products = {}

    for i in range(len(products)):
        try:
            dict_all_products[i] = {
                'image': products[i].find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'price': products[i].find_element(By.CLASS_NAME, 'price').text,
                'name': products[i].find_element(By.CLASS_NAME, 'prdtBILTit').text,
                'note': products[i].find_element(By.CLASS_NAME, 'u-visually-hidden').text
            }
        except:
            pass

    driver.quit()
    return dict_all_products