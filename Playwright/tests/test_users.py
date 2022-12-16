
import re
from playwright.sync_api import Page, expect

def test_users_enter_to_site(page: Page):
    page.goto('http://users.bugred.ru/user/login/index')
    page.locator("input[name=\"name\"]").fill("Skala")
    page.locator("input[name=\"email\"]").fill("skala88@gmail.com")
    page.get_by_role("rowgroup").filter(has_text="Имя Email Пароль Зарегистрироваться").locator("input[name=\"password\"]").fill("1234567qwerty")
    page.get_by_role("button", name="Зарегистрироваться").click()
    
 