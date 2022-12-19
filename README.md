![Raftt](https://raftt-resources.s3.eu-central-1.amazonaws.com/docs/Logos/Navbar/logo-light-blue.svg)

---

### Introduction:

This is a very simple project using Python + Flask to create a simple web todo app.  
In addition to the Python service, there is Postgres DB that used to store the tasks.  
This project is using docker-compose for its description.

The goal of this workshop is to get you more familiar with Raftt, how environments are defined, and how to fix issues and improve your envs.

### Setup:

- Clone this repo.
- Install Raftt:
    - [https://docs.raftt.io/docs/basics/quickstart](https://docs.raftt.io/docs/basics/quickstart)
- Edit `raftt.yml`, change `host: <change-me>` to you organization's host.

### References:

- Raftt - [https://docs.raftt.io/docs/intro/raftt](https://docs.raftt.io/docs/intro/raftt)
- Docker-compose - [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- Dockerfile - [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)

### Tasks:

0. After installing Raftt and cloning the repo, run `raftt up`, you will see that it fails. Your first task is to get it up and running.
    - You shouldn’t have to delete the environment and bring it up, use `raftt rebuild` and `raftt restart` to fix it.
    - Once you have a working environment, do try to bring it up from scratch to verify that it still works. Do this by running `raftt down && raftt up`.
    - No Python code changes are needed.
1. Now that you have a working environment, let's make a small modification to the `app.py` file. To make the tasks looks better, let's make it so all tasks titles are always capitalized.
2. To have an even better experience, let’s add debug configuration for the Python service.
    - You can use your preferred IDE - PyCharm / VSCode.
    - Bonus points for configuring both :)
    - You might need to install Raftt's plugin in your IDE if it isn't installed yet.
3. Now we have a great environment, but our DB starts empty and is a bit boring… To have an even awesomer environment, let’s add seeding definition for the `db` service.
    - You’ll find an SQL file under `dev/dump.sql`.
4. Now let’s add a file watching hook! Our goal is to install pip dependencies following any change to the `requirements.txt` file.

---

Built with ☕ by [raftt](!https://www.raftt.io)
