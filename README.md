# Omnilytics File Generator
###### v0.01
This repository has been created to manage a Django Web Application built for the programming challenge by Omnilytics

According to the challange stated here https://docs.google.com/document/d/1RvJaYLFOp7uOydSk8Cy7dMBJh2jz0GZ4_4DqbzhH7JE/edit#heading=h.82ptcrbz6e3k, the purpose of the application is to generate a file that includes four types of random objects through RESTful API


## Guide to run the dockerized application
1. Git Clone the repository on the local machine
2. cd to the directory Omnilytics_Programming_Contest
3. Now build the docker image by running the command ``` docker-compose build ```
4. After the image is built, run the command ``` docker-compose up ``` to run the application as a container
5. You will be seing something like:
6. ![Screenshot_1](https://user-images.githubusercontent.com/59188728/141673769-de8a9635-3950-4a4c-8b87-b21c74e9cd5e.png)
7. Now the application is up and running


## Guide to use swagger ui to get responses from the API endpoints.
1. Now that the application server has started, the backend api's will be available
2. You can easily see the API documentation by hitting the in-built swagger API documentation url ```/swagger```
3. For example, just open a web browser and go the link http://localhost:8000/swagger
4. Here you can see the swagger_ui to explore the backend API's. You can see sample json responses and even get response from the ui itself
5. See the following guides to use the swagger API documentation UI
6. ![Screenshot_2](https://user-images.githubusercontent.com/59188728/141674514-cc862039-2a67-431c-a69b-627b9a6b1799.png)
7. ![Screenshot_3](https://user-images.githubusercontent.com/59188728/141674515-534c95f3-aa90-4f85-9c05-951a240b3bb1.png)
8. ![Screenshot_6](https://user-images.githubusercontent.com/59188728/141674653-be3f1c16-0cc9-4d97-a92b-e18bfb3f1715.png)


## API endpoints and response specifications
1. Other than swagger, the API endpoints can be accessible from anywhere locally(i.e. Postman, Any front-end framework like Angular)
2. Two API endpoints have been exposed. ```/api/file_generator``` and ```/api/download_file```
3. Here ```/api/file_generator``` endpoint is the important one to fulfil the backend part of the challange
4. Upon ```GET``` request to ```/api/file_generator``` (i.e. ```http://localhost:8000/api/file_generator```) , a json response will be genarated as follows
```
{
    "ack_timestamp": "2021-11-14T15:21:31.139017",
    "generated_objects": {
        "alphabetical_string": {
            "generated_string": "MTHXIJicbhGgVsXufeirfwDjQjyokWg",
            "obj_length": 31
        },
        "real_number": {
            "generated_number": 33.62938579061762,
            "obj_length": 17
        },
        "integer": {
            "generated_integer": -267479423,
            "obj_length": 10
        },
        "alphanumeric": {
            "generated_alphanumeric": "2qkbQa2ESIUpxEIOZIg1nv1OPcy0mDFMKiz3RxfjcT4q31a0nuUxeSxA9w0t6HO3PnqSFz9TtqM0QvEafN4gfer2aklZkxZpTyE5OdEW9wxUb6oKm9UgpD2oJWQ7uUymJ3i0IiItuszirE18tz1NXhkcYynD4Iei",
            "obj_length": 160
        }
    },
    "file_content": "MTHXIJicbhGgVsXufeirfwDjQjyokWg,33.62938579061762,-267479423,2qkbQa2ESIUpxEIOZIg1nv1OPcy0mDFMKiz3RxfjcT4q31a0nuUxeSxA9w0t6HO3PnqSFz9TtqM0QvEafN4gfer2aklZkxZpTyE5OdEW9wxUb6oKm9UgpD2oJWQ7uUymJ3i0IiItuszirE18tz1NXhkcYynD4Iei",
    "status": {
        "status_code": 200,
        "msg": "File Content Generated Successfully!"
    }
}
```
5. Here generated_objects are listed with their respected object lengths.
6. file_content holds all the objects sequentially separated by ","
7. Using this, the front-end can generate files and even display on the web ui.
8. The other endpoint is ```/api/download_file```. Which can be used to download the generated file from a web browser.


Thanks for using the application.
