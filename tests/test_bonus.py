"""
Bonus tests for A2.

These tests are outside TC-01..TC-12 and target SRS rules that are not covered
deeply by the required suite.
"""
import pytest

from conftest import enable_flutter_semantics, flutter_click_button, flutter_fill, wait_for_flutter
from ui_helpers import (
    MEMBER_EMAIL,
    book_cards,
    login_as,
    save_screenshot,
    semantics_text,
)


@pytest.mark.parametrize(
    "email,password,expected_error,screenshot_name",
    [
        ("nobody@test.com", "anything", "Không tìm thấy thành viên", "bonus_login_unknown_email.png"),
        (MEMBER_EMAIL, "wrongpassword", "Mật khẩu không đúng", "bonus_login_wrong_password.png"),
        ("", "", "Vui lòng nhập email và mật khẩu", "bonus_login_empty_fields.png"),
    ],
)
def test_bonus_login_validation_messages_data_driven(
    page, test_config, email, password, expected_error, screenshot_name
):
    """B2: data-driven validation for REQ-01 login failure messages."""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    if email:
        flutter_fill(page, "Email", email)
    if password:
        flutter_fill(page, "Mật khẩu", password)
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text=expected_error)
    save_screenshot(page, screenshot_name)

    sem_text = semantics_text(page)
    assert expected_error in sem_text
    assert "Đăng nhập" in sem_text
    assert "Đăng xuất" not in sem_text


def test_bonus_search_is_case_insensitive(page, test_config):
    """B1/B3: REQ-03 search must be case-insensitive."""
    login_as(page, test_config["base_url"])
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "flutter")
    wait_for_flutter(page, text="Lập trình Flutter cơ bản")
    save_screenshot(page, "bonus_search_case_insensitive.png")

    labels = [
        book_cards(page).nth(i).get_attribute("aria-label") or ""
        for i in range(book_cards(page).count())
    ]
    assert any("Lập trình Flutter cơ bản" in label for label in labels)
    assert any("Flutter" in label for label in labels)


def test_bonus_suspended_member_cannot_borrow_book(page, test_config):
    """B1/B3: REQ-04 must reject suspended members with the correct reason."""
    login_as(
        page,
        test_config["base_url"],
        email="cu.le@email.com",
        password="password123",
    )
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Lập trình Flutter cơ bản")
    wait_for_flutter(page, text="Lập trình Flutter cơ bản")
    page.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').first.click()
    wait_for_flutter(page, text="Xác nhận")
    page.locator('flt-semantics[role="button"]:has-text("Mượn")').last.click()
    wait_for_flutter(page, text="tạm ngưng")
    save_screenshot(page, "bonus_suspended_member_cannot_borrow.png")

    sem_text = semantics_text(page)
    assert "tạm ngưng" in sem_text
    assert "hết hạn" not in sem_text
