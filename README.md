# Data Quality API Validation (Python Requests)  

💡 *Automating API checks to ensure data accuracy, consistency, and reliability.*  

---

## 🚀 Overview
This project demonstrates how I use **API automation to validate and safeguard data integrity**.  
The suite leverages Python’s `requests` library to test CRUD operations against the JSONPlaceholder API, ensuring endpoints return accurate and consistent results.  

By automating these checks, I reduce manual effort, accelerate feedback, and create a repeatable framework for **data validation and reconciliation**.  

---

## 📋 Test Cases Automated
- **Retrieve Users (GET)**  
  - *Action:* Sends a GET request to `/users`.  
  - *Validation:* Confirms `200 OK` and verifies response structure contains expected user data.  

- **Create Post (POST)**  
  - *Action:* Sends a POST request to `/posts` with a JSON payload.  
  - *Validation:* Confirms `201 Created` and verifies response contains submitted data.  

- **Update Post (PUT)**  
  - *Action:* Sends a PUT request to `/posts/1` with updated JSON payload.  
  - *Validation:* Confirms `200 OK` and verifies response reflects updated data.  

- **Delete Post (DELETE)**  
  - *Action:* Sends a DELETE request to `/posts/1`.  
  - *Validation:* Confirms `200 OK`.  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Library:** requests  
- **API:** JSONPlaceholder (REST)  
- **Testing Framework:** Pytest  

---

## 🏃‍♂️ Execution
Tests are implemented with **Python requests + Pytest**.  
They validate CRUD operations and can be run locally in a standard Python environment.  

---

## 📊 What This Demonstrates
- Ability to **interact with RESTful APIs** and validate responses.  
- Experience with **data validation and reconciliation** through automated checks.  
- Hands‑on use of **Python + requests** for process reliability.  
- A mindset focused on **data quality, accuracy, and repeatable validation frameworks**.  

---
