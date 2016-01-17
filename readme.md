# flask-uwsgi-nginx-haproxy-docker

This project demonstrates the following technologies:

  * [Flask](http://flask.pocoo.org/), Python based WEB framework
  * [uWSGI](http://uwsgi-docs.readthedocs.org/), web application deployment solution
  * [nginx](http://nginx.org/), reverse proxy server. Capable of proxying HTTP requests to uWSGI via UNIX-domain sockets
  * [HAProxy](http://www.haproxy.org/), TCP/HTTP load balancer
  * [Docker](https://www.docker.com/), solution for deploying distributed applications in containers

The Flask application only returns a simple *Hello World* response. Before that it sleeps for 0.1 seconds to simulate real work. Not a CPU intensive work but for example a database query.

The uWSGI server is configured to spawn the Flask application into 5 processes, each communicating with nginx via UNIX-domain sockets. Flask application processes, uWSGI process and nginx process all run in the same Docker container.

HAProxy acts as a load balancer in front of nginx instance(s). This makes sense as soon as the web containers are scaled up to 2 or more.

# Running the containers

Build and run the application in Docker container:

    [sudo] docker-compose build
    [sudo] docker-compose up

Scale the web node to 5 instances:

    [sudo] docker-compose scale web=5

## Testing

Navigate to [http://localhost:8080](http://localhost:8080). By continuously hitting F5 you should see that the HOSTNAME is changed because HAProxy routes the requests balanced to every node. Also the PID changes every now and then because uWSGI routes the requests to different processes. However the uWSGI "load balancing" is not really balanced between every process but the the first one is always used by default and if it's busy then the next one is used, etc.

To test load balancing with 10000 requests (where 1000 concurrent):

    ab -n 10000 -c 1000 http://localhost:8080/
