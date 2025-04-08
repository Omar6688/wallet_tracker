# TESTING.md

## Overview

This document outlines the testing process for the **Wallet Tracker** Django web application. Manual testing was carried out across all devices, features, and views to ensure stability, responsiveness, and a seamless user experience. All core functionality was tested for expected behavior, error handling, and input validation.

---

## Contents

- [Manual Testing](#manual-testing)
  - [Navigation](#navigation)
  - [Authentication (Login / Logout / Register)](#authentication-login--logout--register)
  - [Expense Management (CRUD)](#expense-management-crud)
  - [Income Management (CRUD)](#income-management-crud)
  - [Delete Confirmation Flow](#delete-confirmation-flow)
  - [Error Handling & Permissions](#error-handling--permissions)
  - [Input Validation](#input-validation)
  - [Responsive Design Testing](#responsive-design-testing)
- [Validator Testing](#validator-testing)
- [Bugs](#bugs)
- [Additional Testing](#additional-testing)
- [Screenshots (Optional)](#screenshots-optional)

---

## Manual Testing

### Navigation

| Test Case                             | Expected Result                                   | Outcome  |
|--------------------------------------|---------------------------------------------------|----------|
| Click on “Home” in navbar            | Redirects to home page                            | ✅ Pass   |
| Click on “Expenses”                  | Redirects to expense list                         | ✅ Pass   |
| Click on “Add Expense”               | Opens add expense form                            | ✅ Pass   |
| Click on “Income”                    | Redirects to income list                          | ✅ Pass   |
| Click on “Add Income”                | Opens add income form                             | ✅ Pass   |
| Navbar collapse on mobile            | Hamburger menu opens with all links               | ✅ Pass   |

---

### Authentication (Login / Logout / Register)

| Test Case                        | Expected Result                              | Outcome  |
|----------------------------------|----------------------------------------------|----------|
| Register with valid data         | User account created and logged in           | ✅ Pass   |
| Register with existing email     | Error message shown                          | ✅ Pass   |
| Login with valid credentials     | User logged in and redirected                | ✅ Pass   |
| Login with invalid credentials   | Error shown, login fails                     | ✅ Pass   |
| Logout as logged-in user         | User logged out, redirected to login page    | ✅ Pass   |

---

### Expense Management (CRUD)

| Action           | Test Case                                      | Expected Result                                 | Outcome  |
|------------------|------------------------------------------------|--------------------------------------------------|----------|
| Create Expense    | Submit valid data in form                     | Expense is saved and appears in list            | ✅ Pass   |
| Edit Expense      | Update data through form                      | Expense is updated                              | ✅ Pass   |
| Delete Expense    | Click delete → confirmation → confirm delete  | Expense is removed from list                    | ✅ Pass   |
| View Expense List | See all expenses sorted by date               | User's expenses are listed                      | ✅ Pass   |

---

### Income Management (CRUD)

| Action           | Test Case                                      | Expected Result                                 | Outcome  |
|------------------|------------------------------------------------|--------------------------------------------------|----------|
| Create Income     | Submit valid data in form                     | Income is saved and appears in list             | ✅ Pass   |
| Edit Income       | Update data through form                      | Income is updated                               | ✅ Pass   |
| Delete Income     | Click delete → confirmation → confirm delete  | Income is removed from list                     | ✅ Pass   |
| View Income List  | See all income sorted by date                 | User's income is listed                         | ✅ Pass   |

---

### Delete Confirmation Flow

| Feature                  | Test Case                                          | Outcome |
|--------------------------|---------------------------------------------------|---------|
| Delete Expense           | Loads confirmation page before deleting           | ✅ Pass |
| Delete Income            | Loads confirmation page before deleting           | ✅ Pass |
| Delete from other user   | Triggers 403 forbidden error page                 | ✅ Pass |

---

### Error Handling & Permissions

| Test Case                                | Expected Result                         | Outcome  |
|------------------------------------------|-----------------------------------------|----------|
| Access non-existent URL                  | 404 error page is displayed             | ✅ Pass   |
| Try to edit/delete another user's data   | 403 error page is shown                 | ✅ Pass   |
| Try to access protected pages while logged out | Redirected to login page           | ✅ Pass   |

---

### Input Validation

| Field      | Test Case                           | Expected Result                         | Outcome  |
|------------|--------------------------------------|-----------------------------------------|----------|
| Amount     | Enter negative value                | Validation error shown, not saved       | ✅ Pass   |
| Amount     | Enter 0                             | Validation error shown, not saved       | ✅ Pass   |
| Amount     | Enter 0.01 or more                  | Accepted                                | ✅ Pass   |
| Required fields | Submit blank form              | Validation errors shown                 | ✅ Pass   |

---

### Responsive Design Testing

Tested on the following devices:

- MacBook (Chrome, Safari)
- iPhone (iOS Safari)
- iPad (Chrome & Safari)
- Android phone (Chrome)
- Chrome DevTools responsive view

| Screen Size       | Result                                    |
|-------------------|-------------------------------------------|
| Desktop (1920px)  | Layout fully responsive                   |
| Tablet (768px)    | Navbar collapses, spacing maintained      |
| Mobile (375px)    | Forms and tables stack correctly, readable|

✅ All pages are fully responsive and mobile-friendly.

---

## Validator Testing

### HTML

- All templates were tested using [W3C Validator](https://validator.w3.org/)

- All templates were tested using the W3C Markup Validator by copying the rendered HTML from the browser (after Django template rendering). All pages passed with no critical errors. Minor template syntax like `{% static %}` was excluded from validation.

### CSS

- Validated via [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- ✅ No issues detected

### Python (PEP8)

- All `.py` files validated using `flake8`
- ✅ No style violations remaining after cleanup

---

## Bugs

### Resolved Bugs

| Bug | Description | Resolution |
|-----|-------------|------------|
| Delete income caused 500 error | Template `delete_income.html` missing | Created proper confirmation template |
| Accessing edit/delete without permission | No restriction in place | Added `PermissionDenied` handling |
| Negative values allowed | No validators applied | Added `MinValueValidator(0.01)` |

---

## Additional Testing

### Browser Compatibility

Tested successfully on:
- Chrome (macOS, iOS, Android)
- Safari (macOS, iOS)
- Firefox (macOS)
- Microsoft Edge (Windows)

### Accessibility

- Forms and buttons tested with keyboard navigation
- Color contrast checked (orange on dark blue passes WCAG AA)
- ARIA labels used where applicable

---

## Screenshots (Optional)

## Screenshots

### Delete Income Confirmation
![Delete Income Confirmation](docs/testing_screens/delete_income.png)

### 403 Forbidden Page
![403 Error](docs/testing_screens/error_403.png)

### 404 Page Not Found
![404 Error](docs/testing_screens/error_404.png)

### Validation Error
![Validation Error](docs/testing_screens/validation_error.png)

### Mobile Responsive View
![Mobile View - Expenses](docs/testing_screens/mobile_expense_list.png)


Example:

```markdown
![Delete Confirmation - Expense](docs/testing_screens/delete_expense.png)
