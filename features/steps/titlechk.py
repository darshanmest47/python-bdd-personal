from behave import *
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from features.testdata.locators import Locators


@given(u'user is successfully landed on the page')
def step_impl(context):
    print('User is successfully landed on the webpage')
    # print(context)


@when(u'user reloads the webpage')
def step_impl(context):
    context.driver.refresh()
    print('reload')


@then(u'the title of the webpage should match exactly with the test title')
def step_impl(context):
    context.status_Fail = False
    context.driver.execute_script("window.scrollTo(0,0)")

    assert context.driver.title == Locators().title




@when(u'user scrolls upto the top of the page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,0)")


@when(u'user hovers the mouse over projects')
def step_impl(context):
    pros = context.driver.find_element(By.XPATH, Locators().projects)

    acts = ActionChains(context.driver)
    acts.move_to_element(pros).perform()


@when(u'user hovers the mouse over contact')
def step_impl(context):
    ctcs = context.driver.find_element(By.XPATH, Locators().contact)

    acts = ActionChains(context.driver)
    acts.move_to_element(ctcs).perform()


@then(u'hovering action must take place')
def step_impl(context):
    print('Hover success')


@when('user scrolls to the react-quiz section')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,1000)")


@when('user enters the frame containing react-quiz and performs some scrolling')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,1000)")
    context.driver.switch_to.frame(1)
    time.sleep(2)

    val1 = 2
    val2 = 2

    for ele in range(1, 10):
        val1 = val1 * ele
        time.sleep(0.5)
        context.driver.execute_script(f"window.scrollBy(0,{val1})")

    for ele2 in range(1, 10):
        val2 = val2 * ele2
        time.sleep(0.5)
        context.driver.execute_script(f"window.scrollBy(0,{-val2})")

    context.driver.switch_to.default_content()
    time.sleep(2)
    print(context.driver.title)


@when('user enters multiple values {firstname} {lastname} {email} {password}')
def step_impl(context, firstname, lastname, email, password):
    print('Scrolled')
    print(firstname)
    print(lastname)
    print(email)
    print(password)

    context.driver.execute_script("window.scrollTo(0,1000)")
    context.driver.switch_to.frame(1)

    context.driver.find_element(By.XPATH, Locators().firstname).send_keys(firstname)
    context.driver.find_element(By.XPATH, Locators().lastname).send_keys(lastname)
    context.driver.find_element(By.XPATH, Locators().email).send_keys(email)
    context.driver.find_element(By.XPATH, Locators().password).send_keys(password)

    context.driver.switch_to.default_content()
    time.sleep(2)
    print(context.driver.title)


@then('values must get entered')
def step_impl(context):
    print('Entered')
    assert context.driver.title == Locators().title
