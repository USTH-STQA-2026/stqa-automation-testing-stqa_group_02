# Automation Test Report

## Summary

This suite tests the ABC Library borrowing system at `https://stqa.rbc.vn` with
Python, pytest, and Playwright. Expected results are derived from
`docs/SRS-library-system.md`; `docs/BRD-yeu-cau-nghiep-vu.md` is treated only as
business context.

## Required Test Cases

| TC | Test | Short description | Main oracle |
| --- | --- | --- | --- |
| TC-01 | Login success | Valid email and password open the main app. | User name or `Đăng xuất` is visible. |
| TC-02 | Wrong password | Valid email with wrong password is rejected. | `Mật khẩu không đúng` is visible and `Đăng xuất` is absent. |
| TC-03 | Empty login fields | Empty email and password are rejected. | `Vui lòng nhập email và mật khẩu` is visible. |
| TC-04 | Search by book name | Search `Flutter`. | Result contains `Lập trình Flutter cơ bản`. |
| TC-05 | Search no result | Search a unique non-existent keyword. | `Không tìm thấy sách` is visible and no book cards remain. |
| TC-06 | Filter by category | Filter by `Công nghệ`. | Every displayed book card contains `Công nghệ`. |
| TC-07 | Search by author | Search `Nguyễn Minh Đức`. | Returned books all contain the author name. |
| TC-08 | Borrow book | Active member borrows an available book. | Success message and `Đang mượn` status appear. |
| TC-09 | View borrowed books | Member opens `Mượn / Trả`. | Existing borrowed book and `Trả sách` action are visible. |
| TC-10 | Return book | Member returns an active borrowed book. | Return success message appears. |
| TC-11 | Logout | User logs out from the main app. | Login form is visible and `Đăng xuất` is absent. |
| TC-12 | Switch to English | User switches UI language to English. | English UI text such as `Logout` is visible. |

## Bonus Coverage

| Bonus test | Requirement | Short description | Main oracle |
| --- | --- | --- | --- |
| `test_bonus_login_validation_messages_data_driven` | B1, B2, B3 | Parametrized login validation for unknown email, wrong password, and empty fields. | Exact SRS error text appears for each data row. |
| `test_bonus_search_is_case_insensitive` | B1, B3 | Search lowercase `flutter`. | The Flutter book still appears, proving case-insensitive search. |
| `test_bonus_suspended_member_cannot_borrow_book` | B1, B3 | Suspended member tries to borrow an available book. | Rejection message mentions `tạm ngưng`, not `hết hạn`. |

## AI Usage Declaration

The group used Codex to draft and review Playwright/pytest automation code,
then aligned assertions with the SRS and the provided seed data.
