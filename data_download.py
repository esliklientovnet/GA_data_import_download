from selenium import webdriver
import time
import os 

email = "***********@gmail.com"
password = "*********"
download_folder = os.path.dirname(os.path.abspath(__file__))
try: 
    #ссылка на старницу настроек нужного ресурса
    link = "https://analytics.google.com/analytics/web/#/a49298821w107676036p132678995/admin"

    # переназначаем папку загрузки
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
})

    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(10)
    browser.get(link)

    # ввод email
    browser.find_element_by_id("identifierId").send_keys(email)
    browser.find_element_by_id("identifierNext").click()


    # ввод пароля
    browser.find_element_by_css_selector('input[name=password]').send_keys(password)
    browser.find_element_by_id("passwordNext").click()


    #переходим в импорт данных
    browser.find_element_by_css_selector(".app-admin-dataimport").click()


    #переходим на страницу загрузки данных. изменить на свою схему
    link = "https://analytics.google.com/analytics/web/#/a49298821w107676036p132678995/admin/dataimport/datasets/o2eJ6LYJRxK2sX_DISLnjA/records"
    browser.get(link)


    #Загружаем первый попавшийся отчет
    browser.find_element_by_css_selector("a.download-button").click()

    #Задержка для загрузки файла
    time.sleep(30)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()
