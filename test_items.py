import pytest,time
from selenium import webdriver

       
def test_guest_should_see_busket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
        
    button=browser.find_element_by_css_selector("form.add-to-basket :nth-child(3)")
    assert button, "Should be absolute value of a number"

    
