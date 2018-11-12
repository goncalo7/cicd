### CICD - Pipeline for a Simple Web App


Developing and Releasing software can be a tricky process, where the pipeline and the tools choosen can improve massively the speed and the quallity of the delivered code. Also the iterations between build - test - deploy should be as straight forward as a simple commit to the project.

From a lot of options on the marked, from Managed Providers vs Self-Hosting, Open-Source vs Commercial Solutions i decided to choose gitlab and gitlabci for the job.
Choosing one integrated solution for use of version control, infrastructure as code, handling of secrets, creating of build test and deployment pipelines, has many advantages:

- Single Code Base
- Single upgrade 
- Single setup
- Single Interface
- Single Authentication
- Single Training

The versalibilty of this tool allows to have multiple types of pipelines all with their own specific runners with any type of software necessary for the job.

All the code is version controlled so you can trace all the changes made to any point in time. 
Rollback procedures can also be completelly automated in any case.

- Did i mention already Single System Operation? Thats right all the operation efforts will be done on a single system what can reduce all the operational process required.
This Solution can be Used online from Gitlab or you can just run their opensource project gitlabCE for free and Develop Away. And if you change your mind later, the migration is simple and fast.

Being a very complete tool that can integrate all the lifecycle of an application development, the features of GitlabCI will make you save time and money, to be applied where really matters the most: **Deliver Amazing Software**.


The CICD Pipeline is completly automated from the build stage to deployment to Production environment:
After new code is build and pushed to the repo our pipeline will do the following tasks:
(only following to the next once the previous is successfull)

- Build localy a new container with your latest code (step 1)
- Run Unittests on that container using dgoss or similar tool(step 2)
- Push your changes to the repo to triger a build(step 3)
- Deploy to a Test environment ( this ideally should be as close as a prod env but without any customer data ) 
- Run integration tests on test environment
- Deploy to acceptance ( this ideally should be the same as prod environment but with sample data) 
- Run integration tests on acceptance environment
- Run functional tests on acceptance environment
- Deploy to production

Try it yourself in the steps section

The same process would be used for the backend and for the frontend.

To show how this process will look, a sample pipeline with the first 4 steps was build in this repo.

Simple Web Application CICD Instructions:

Requirements:
- Docker
- Docker Compose
- dgoss

To run the platform just run docker-compose up in the project root directory.

This will start the following services:

- 2 x Gitlab Docker runner
- Gitlab Server

If you need to register new Runners just change and run the following command acording with the specifications fo the new runner:

`docker exec -it cicd_gitlab-runner2_1 gitlab-runner register -n -r  wKyhCsrTQ_56uc7Jnw1T -u http://gitlab --executor docker --docker-image docker:latest --docker-network-mode host --docker-privileged --tag-list docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock`

`docker exec -it cicd_gitlab-runner2_1 gitlab-runner register -n -r  wKyhCsrTQ_56uc7Jnw1T -u http://gitlab --executor docker --docker-image docker:latest --docker-network-mode host --docker-privileged --tag-list docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock`

# How to access and use your services:
Gitlab - http://localhost

gitlab user: root
gitlab password: supermario

#Steps

First don't forget to add your public key to gitlab

IMPORTANT: After clone the repo go to my-awesome-app directory and run `tar -zxvf git.gz`

**(Step 1 and 2)** 
Make your changes on the code and unittest them with:
(add more tests in goss.yml if desired)

**backend:** `docker build . -t backend; dgoss run -p 8110 backend`

**frontend:** `docker build . -t frontend; dgoss run -p 8110 frontend`

**(step 3)**

push your changes to the repo

**(Open Gitlab Pipelines and see it happening)**
 
Once the Pipeline is complete and the applications are deployed you can test your services on http://localhost:10000

to test the backend api:

http://localhost:10001/getjoke
http://localhost:10001/getperson
http://localhost:10001/getdog

The Web Application is a simple backend api created with flask that only fetches and returns random data from some websites 
The front end is a web page that prints the data of the endpoints in the same page.
Ideally we would have a service discovery tool to automatically advertise the services, but because this isn't the case on this demo both frontend and backend are in the same pipeline. 

