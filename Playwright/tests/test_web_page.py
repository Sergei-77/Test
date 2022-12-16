import re
from playwright.sync_api import Page, expect


def test_playwright(page: Page):

    page.goto("https://ya.ru/") #1 шаг
    page.goto("https://yandex.ru/search/?text=michael+jackson&lr=10262&msid=1669312553907417-6262618382681667128-vla1-3402-vla-l7-balancer-8080-BAL-7533&search_source=yaru_desktop_common&suggest_reqid=183122684166931255325544312468613&src=suggest_B")
    page.goto("https://yandex.ru/search/?text=michael+jackson&lr=10262&search_source=yaru_desktop_common&src=suggest_B")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Home - Michael Jackson Official Site").click()
    page1 = popup_info.value


def test_enter_to_site(page: Page):
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username', 'demo' )
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')
    
    