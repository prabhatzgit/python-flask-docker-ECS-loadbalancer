1. Create necessary AWS components.
2. Code GET and POST endpoints.
3. Dockerize flask app. docker build -t python-flask-docker-ecs-loadbalancer .
   run --> docker run -p 5000:5000 python-flask-docker-ecs-loadbalancer
4. Push flask app to Github.
5. Create CI/CD using Jenkins.
6. Access app via Route 53 domain.
7. Connect flask app to AWS RDS.
8. Store private values in AWS secret manager.
9. Schedule Stop/Start of EC2 instance.
10. Automate alerts if ECS instance fails.

# How to delete the docker image

1. List all running containers to find the one using the image:
   docker ps
2. Identify the container that's using the image from the list. You can also run:
   docker ps -a --filter ancestor=python-flask-docker-ecs-loadbalancer:latest
3. Stop the container using:
   docker stop <container_id>
4. Remove the container:
   docker rm <container_id>
5. Now try deleting the image again:
   docker rmi python-flask-docker-ecs-loadbalancer:latest

# how flask app can run as a container task in AWS ECS cluster service (accessed through an AWS Load Balancer)

1. Create ECS Task Definition

- Launch type: Fargate
- Network mode: awsvpc
- Container:
- Image: your ECR image URI
- Port mappings: container port 5000
- Task Role: for permissions (e.g., CloudWatch logs)

2. Create ECS Cluster & Service

- Cluster: Create a new one or use existing
- Service:
- Launch type: Fargate
- Task definition: the one you created
- Desired count: 1+
- Load balancer: Application Load Balancer (ALB)
- Listener: port 80
- Target group: port 5000, protocol HTTP
- Health check path: / or your app’s health endpoint

3. Configure Networking

- Assign public IP (if needed)
- Attach to subnets in your VPC
- Security group: allow inbound traffic on port 80

4. Access Your App
   Once the service is running and the ALB is healthy, access your Flask app via the ALB DNS name.
