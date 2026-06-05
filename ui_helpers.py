import os

from conftest import (
    SCREENSHOT_DIR,
    enable_flutter_semantics,
    flutter_click_button,
    flutter_fill,
    wait_for_flutter,
)


MEMBER_EMAIL = "ba.nguyen@email.com"
MEMBER_PASSWORD = "password123"
MEMBER_NAME = "Nguyễn Học Bá"

BORROW_MEMBER_EMAIL = "dam.tran@email.com"
BORROW_MEMBER_PASSWORD = "password123"

LIBRARIAN_EMAIL = "librarian@library.com"
LIBRARIAN_PASSWORD = "admin123"


def semantics_text(page):
    """Return visible text plus aria-labels from Flutter semantics nodes."""
    parts = []
    nodes = page.locator("flt-semantics")
    for i in range(nodes.count()):
        node = nodes.nth(i)
        text = node.text_content() or ""
        label = node.get_attribute("aria-label") or ""
        if text:
            parts.append(text)
        if label:
            parts.append(label)
    return " ".join(parts)


def save_screenshot(page, name):
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, name))


def login_as(page, base_url, email=MEMBER_EMAIL, password=MEMBER_PASSWORD):
    page.goto(base_url, wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", email)
    flutter_fill(page, "Mật khẩu", password)
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    enable_flutter_semantics(page)


def click_semantics_button(page, text, index=0):
    buttons = page.locator(f'flt-semantics[role="button"]:has-text("{text}")')
    buttons.nth(index).click()
    enable_flutter_semantics(page)


def click_semantics_tab(page, label):
    page.locator(f'flt-semantics[role="tab"][aria-label="{label}"]').first.click()
    enable_flutter_semantics(page)


def book_cards(page):
    return page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
