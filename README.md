<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darkstars31/fast-api-discovery">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">FastAPI Exploration and Experimentation</h3>

  <p align="center">
    This was project was designed and built to explore the use of FastAPI with Firestore as a means to create a lightweight Restful API with persistent document storage (nosql)
    <br />
    <br />
    <a href="https://github.com/darkstars31/fast-api-discovery/issues">Report Bug</a>
    ·
    <a href="https://github.com/darkstars31/fast-api-discovery/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

### Built With

* [Python v3.9.x](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Firebase-Admin-SDK](https://firebase.google.com/docs/reference/admin/python)
* [Insomnia](https://insomnia.rest/) - For testing the endpoints

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can use pip to install the dependencies, but I highly recommend using something like [pipenv](https://github.com/pypa/pipenv) to help manage the project's packages and virtual environment.

* To run the project
```
uvicorn main:app --reload 
```

* Once the project is running locally, you can view the endpoint documentation on your machine
```
localhost:8000/docs
```



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pipenv
  ```sh
  pipenv install
  ```
* Firestore
You will be required to setup a Firebase Account and use a Google Service Account to interact with the persistent storage

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darkstars31/repo_name.git
   ```
2. Install the necessary packages using pip or your favorite python package manager
   ```sh
   pipenv install
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
