# AWS Cloud Resume Challenge - Project Summary
**Candidate:** Alejandro Gonzalez
**Project Date:** April 2026

## 🚀 Project Overview
This project demonstrates a full-stack, serverless architecture on AWS, incorporating Infrastructure as Code (IaC) and modern DevOps practices (CI/CD). The goal was to build and deploy a live, secure resume with a functional visitor counter.

---

## 🏗️ Architecture & Technologies

### 1. Frontend (Presentation Layer)
- **HTML5/CSS3:** A responsive, professional resume layout.
- **JavaScript (Vanilla):** Client-side logic to fetch and display the visitor count from the backend API.
- **Amazon S3:** Used for high-availability static website hosting.
- **Amazon CloudFront:** Content Delivery Network (CDN) providing **HTTPS** security and global edge caching.
- **Origin Access Control (OAC):** Secured the S3 bucket to ensure it is only accessible via the CloudFront distribution.

### 2. Backend (Logic & Database Layer)
- **AWS Lambda (Python):** A serverless function using the `boto3` library to perform atomic increments on the database.
- **Amazon DynamoDB:** A NoSQL database storing the visitor count.
- **AWS API Gateway:** A RESTful API that serves as the entry point for the frontend to communicate with the Lambda function.

### 3. Infrastructure as Code (IaC)
- **Terraform:** Used to define, provision, and manage the entire AWS stack (S3, DynamoDB, Lambda, IAM Roles, API Gateway, CloudFront). This ensures consistent and repeatable deployments.

### 4. DevOps & Automation (CI/CD)
- **GitHub Actions:** Two automated pipelines were implemented:
  - **Frontend CI/CD:** Automatically syncs changes to S3 and invalidates the CloudFront cache upon every push to the `main` branch.
  - **Backend CI/CD:** Automatically runs Python unit tests and applies Terraform changes to the AWS environment.

---

## 🔗 Project Links
- **Live Website (HTTPS):** [https://d3b324ie71jomx.cloudfront.net](https://d3b324ie71jomx.cloudfront.net)
- **GitHub Repository:** [https://github.com/alejo1256/cloud-resume-challenge](https://github.com/alejo1256/cloud-resume-challenge)
- **Backend API:** `https://hxoj0ksiak.execute-api.us-east-1.amazonaws.com/prod/visitor`

---

## 🛠️ Key Accomplishments
- **Full Automation:** Achieved 100% automation for both infrastructure and code deployments.
- **Security First:** Implemented IAM roles with "Least Privilege" and secured the static site with HTTPS and private S3 buckets.
- **Serverless Scaling:** The entire stack is serverless, ensuring it scales automatically and remains cost-effective.
