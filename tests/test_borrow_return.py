"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

This file contains completed borrow and return test cases TC-08 to TC-10.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
from conftest import (
    flutter_fill, wait_for_flutter,
)
from ui_helpers import (
    BORROW_MEMBER_EMAIL,
    BORROW_MEMBER_PASSWORD,
    click_semantics_button,
    click_semantics_tab,
    login_as,
    save_screenshot,
    semantics_text,
)


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    ✅ COMPLETED (*ĐÃ HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → find an "Available" book → click "Mượn sách này" → confirm dialog
        → verify book status changes to "Borrowed".
        (*Đăng nhập → tìm sách "Có sẵn" → click "Mượn sách này" → xác nhận dialog
        → kiểm tra sách chuyển sang trạng thái "Đang mượn".*)

    Suggested steps (*Gợi ý các bước*):
        1. login(page, test_config)
        2. Find available book: page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
           (*Tìm sách Có sẵn*)
        3. Click "Mượn sách này" button inside that book card
           (*Click nút "Mượn sách này" trong sách đó*)
        4. Wait for confirmation dialog, re-enable semantics
           (*Đợi dialog xác nhận, bật lại semantics*)
        5. Click "Mượn" button (confirm button in dialog)
           (*Click nút "Mượn" — nút xác nhận trong dialog*)
        6. Assert: "Đang mượn" or "thành công" appears
           (*Assert: "Đang mượn" hoặc "thành công" xuất hiện*)
    """
    login_as(
        page,
        test_config["base_url"],
        email=BORROW_MEMBER_EMAIL,
        password=BORROW_MEMBER_PASSWORD,
    )
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Lập trình Flutter cơ bản")
    wait_for_flutter(page, text="Lập trình Flutter cơ bản")
    wait_for_flutter(page, text="Có sẵn")
    click_semantics_button(page, "Mượn sách này")
    wait_for_flutter(page, text="Xác nhận")
    page.locator('flt-semantics[role="button"]:has-text("Mượn")').last.click()
    wait_for_flutter(page, text="thành công")
    save_screenshot(page, "tc08_borrow_book.png")

    sem_text = semantics_text(page)
    assert "Mượn sách thành công" in sem_text or "thành công" in sem_text
    assert "Lập trình Flutter cơ bản" in sem_text
    assert "Đang mượn" in sem_text


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    ✅ COMPLETED (*ĐÃ HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    login_as(page, test_config["base_url"])
    click_semantics_tab(page, "Mượn / Trả")
    wait_for_flutter(page, text="Kiểm thử phần mềm nhập môn")
    save_screenshot(page, "tc09_view_borrowed_books.png")

    sem_text = semantics_text(page)
    assert "Kiểm thử phần mềm nhập môn" in sem_text
    assert "Đang mượn" in sem_text
    assert "Trả sách" in sem_text


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    ✅ COMPLETED (*ĐÃ HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    login_as(page, test_config["base_url"])
    click_semantics_tab(page, "Mượn / Trả")
    wait_for_flutter(page, text="Kiểm thử phần mềm nhập môn")
    click_semantics_button(page, "Trả sách")
    wait_for_flutter(page, text="thành công")
    save_screenshot(page, "tc10_return_book.png")

    sem_text = semantics_text(page)
    assert "Trả sách thành công" in sem_text or "thành công" in sem_text
    assert "Kiểm thử phần mềm nhập môn" in sem_text
