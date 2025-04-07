# wallet_tracker
# 💸 Wallet Tracker

Wallet Tracker is a personal finance management web app built with Django and PostgreSQL. It allows users to log in, manage their income and expenses, filter entries by category and date, and view their real-time financial balance. The goal is to provide users with a simple yet powerful tool to gain control over their personal finances.

---

## 📖 Project Story

This application was developed as part of the **Code Institute Level 5 Diploma in Web Application Development**, fulfilling the criteria for the **Data-Centric Web Development Milestone Project (Project 3)**.

Inspired by the need for a clean and focused money management app, Wallet Tracker gives users full CRUD functionality with secure authentication, clean UI, and dynamic balance calculations. The application is fully responsive and suitable for desktop, tablet, and mobile devices. 

The app demonstrates practical usage of Django, models, forms, user authentication, filtered queries, and PostgreSQL integration. It was designed and built step-by-step with Git version control, Agile Kanban planning, Heroku deployment, and detailed testing.

The live site can be found here: [Live Site - Wallet Tracker](https://wallet-tracker-7acecdc627f5.herokuapp.com/)

![Mockup](docs/readme_images/mockup.png)


---


## Table of Contents

- [Wallet Tracker 💸](#wallet-tracker-💸)
  - [User Experience Design](#user-experience-design)
    - [The Strategy Plane](#the-strategy-plane)
      - [Site Goals](#site-goals)
      - [Agile Planning](#agile-planning)
      - [User Stories](#user-stories)
    - [The Scope Plane](#the-scope-plane)
    - [The Structure Plane](#the-structure-plane)
      - [Features](#features)
      - [Features Left to Implement](#features-left-to-implement)
    - [The Skeleton Plane](#the-skeleton-plane)
      - [Wireframes](#wireframes)
      - [Database Design (ERD)](#database-design-erd)
      - [Security](#security)
    - [The Surface Plane](#the-surface-plane)
      - [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
  - [Credits](#credits)


---


# User Experience Design

## The Strategy Plane

### Site Goals

The Wallet Tracker 💸 app is designed to help users manage their personal finances in a simple and effective way. The core focus is to allow users to:

- Add and categorize their income and expenses.
- Track all transactions and view financial history.
- Edit or delete existing entries as their records change.
- View totals and monitor how much they’re spending or earning.
- Navigate the platform easily on mobile, tablet, or desktop.
- Use the app safely with user authentication and protected data.
- Have full CRUD functionality over income and expenses.

The app also focuses on a clean, accessible user interface and fully responsive design.

---

### Agile Planning

Agile methodology was used throughout the development of this project using GitHub Projects. Each user story was planned and executed in small, manageable tasks to ensure continuous progress.

User stories were written to capture the goals from the user’s perspective and each included clear **Acceptance Criteria** to define when a task is complete. These user stories can be viewed on the [Wallet Tracker GitHub Project Board](https://github.com/USERNAME/wallet_tracker/projects/1).

#### User Stories

- **Story 1: Register an account**
  - *As a new user I can to create an account so that I can log in and track my income and expenses.*
  - **Acceptance Criteria:** Registration form includes username, email, and password, confirmation message is shown after successful registration and redirect to login page.

- **Story 2: Login and logout**
  - *As a registered user I can log in and out securely so that only I can access my data*
  - **Acceptance Criteria:** Correct credentials redirect to homepage, incorrect credentials show an error and logout button appears only when logged in.

- **Story 3: Add Expense**
  - *As a logged-in user I can add an expense so that I can track my spending.*
  - **Acceptance Criteria:** Expense form includes title, amount, category, and date: form is validated and expenses are saved and visible in table format.

- **Story 4: Add Income**
  - *As a logged-in user I can record income so that I can calculate my total balance.*
  - **Acceptance Criteria:** Same structure as the expense form,income shows up in income table and total income is calculated at the top.

- **Story 5: View Financial Summary**
  - *As a user I can see total income and expenses so that I know how much money I have left.
  - **Acceptance Criteria:** Homepage shows financial summary, all values are calculated in real-timeand balance is visually separated.

- **Story 6: Edit or Delete Records**
  - *As a user I can update or remove records so that I can correct mistakes.*
  - **Acceptance Criteria:** Edit and delete buttons are available beside each item, confirmation message on delete and data updates in real-time.

- **Story 7: Deploy the project to Heroku**
  - *As a developer I can deploy the app to Heroku so that it is accessible online.*
  - **Acceptance Criteria:** The project must be pushed to Heroku using GitHub/CLI/dashboard, environment variables such as SECRET_KEY, DEBUG, and DATABASE_URL must be securely configured and the site must load correctly with static files working on Heroku.

- **Story 8: Write a professional README file**
  - *As a developer I can create a detailed README.md so that users and assessors understand the purpose, usage, and structure of the project.*
  - **Acceptance Criteria:** README includes project overview, features, and UX considerations, technologies used, setup instructions, testing, and deployment are documented, credits and licensing information are clearly listed and Markdown formatting is consistent and professional.

- **Story 9: Perform manual testing on the app**
  - *As a developer I can manually test the site functionality so that I can ensure the user flows and inputs behave as expected.*
  - **Acceptance Criteria:** All forms are tested for valid and invalid input, all views are accessible based on user authentication, expected feedback messages appear after actions and test cases are documented in the README under "Testing" section.

- **Story 10: Design an Entity Relationship Diagram (ERD)**
  - *As a developer I can create an ERD for the database structure so that others can understand the relationships between the models.*
  - **Acceptance Criteria:** ERD includes all models (e.g., User, Expense, Income), relationships (e.g., ForeignKeys) are clearly represented, Diagram is added to the documentation (README or /docs), ERD is updated if database schema changes.


  ---

  
