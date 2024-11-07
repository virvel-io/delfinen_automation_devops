# delfinen_automation_devops

## Project Plan

<br>Project Plan: Delfinen</br>
<br>Project Members: Kristofer, Larissa & Viji</br>
Project Overview: 
The project aims to build a web app using the OpenWeatherMap API where we will write a function to fetch specific locations, meaning the user will enter a location to retrieve data. The data will be displayed with a graph of temperatures for the specified location, using the Streamlit tool.

Functionality and Flow:
The user enters a location which will then generate temperature data and display the result for the specified location.

Workflow:
1. API Request:
A request is sent to the OpenWeatherMap API to fetch the temperature based on a specified location, entered by the user.
2. Data Processing:
A function processes the received data and presents the temperature for a specified location as a graph.
3. Basic UX Design:
The web app will have a simple and user-friendly design to ensure that the user can quickly interact with the application.
4. Unit Tests for API and Data Processing:
Unit tests are implemented to ensure that the API request returns correct data and that the processing function works as expected. Example: Testing that the application can fetch the correct location entered by the user.
5. CI/CD Pipeline via GitHub Actions:
The project is integrated with a GitHub Actions pipeline where tests are run automatically. The tests include, for example, validation of the correctly specified location.
6. Docker Containerization:
When the tests pass the expected results, the application is containerized with Docker to create a consistent environment for deployment.
7. Deployment via Azure:
The Docker-containerized app is deployed to Azure, where users can access the application with expected and reliable results.
Goals and Expected Results:
The goal is to develop a stable web app that meets user expectations in terms of user-friendliness and correct API requests and data processing. The app is tested and deployed in a DevOps pipeline with GitHub Actions and Azure.