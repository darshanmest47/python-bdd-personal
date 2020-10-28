from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import allure
import time


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

    context.driver.get('https://mynewportofolio.herokuapp.com/')

    context.driver.maximize_window()


def after_scenario(context, scenario):
    if context.failed:
        print(context.scenario)

        allure.attach(context.driver.get_screenshot_as_png(), name="testfail", attachment_type=AttachmentType.PNG)
        context.driver.quit()
    else:

        context.driver.quit()
