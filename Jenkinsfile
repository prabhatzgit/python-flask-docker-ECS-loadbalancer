pipeline {
    agent any

    environment{
        AWS_REGION = 'ap-south-1'
        IMAGE_NAME = 'test-flask'
        REPO_NAME = 'flask-docker-ecs-deployment-pipeline'
    }

    stages{
        stage('checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/prabhatzgit/python-flask-docker-ECS-loadbalancer'
            }
        }

        stage('Tag the image'){
            steps{
                script{
                    env.IMAGE_TAG = 'latest'
            }
          }
        }

        stage('Login to Docker') {
            steps {
                powershell '''
                    echo \"${DOCKER_CREDENTIALS_PSW}\" | docker login -u \"${DOCKER_CREDENTIALS_USR}\" --password-stdin
                '''
            }
        }                                               
        
        stage('Build Docker Image'){
            steps{
                powershell '''
                docker build -t $env.IMAGE_NAME:$env.IMAGE_TAG .
                docker tag $env.IMAGE_NAME:$env.IMAGE_TAG 362911127705.dkr.ecr.ap-south-1.amazonaws.com/test:latest
                '''
            }
        }

        stage('Login to ECR'){
            steps{
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-creds'){
                  powershell '''
                  $ecrLogin = aws ecr get-login-password --region $env.AWS_REGION

                  docker login --username AWS --password-stdin $ecrLogin https://362911127705.dkr.ecr.ap-south-1.amazonaws.com
                  '''
                }
            }
        }

        stage('Push to ECR'){
            steps {
            powershell '''
            docker push 362911127705.dkr.ecr.ap-south-1.amazonaws.com/test:latest
            '''
          }
        }
    }
}
