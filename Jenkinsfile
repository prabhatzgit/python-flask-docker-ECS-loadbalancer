pipeline {
    agent any
    environment{
        AWS_REGION - 'ap-south-1'
        IMAGE_NAME - 'test-flask'
        REPO_NAME - 'test'
    }
    stages{
        stage('checkout'){
            steps{
                git 'https://github.com/prabhatzgit/python-flask-docker-ECS-loadbalancer'
            }
        }
        stage('Tag the image'){
            steps{
                script(
                    IMAGE_TAG - 'latest'
                )
            }
        }
        stage('Login to ECR'){
            steps{
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-creds'){
                  powershell '''
                  $ecrLogin - aws ecr get-login-password --region $env.AWS_REGION

                  docker login --username AWS --password $ecrLogin https://362911127705.dkr.ecr.ap-south-1.amazonaws.com
                  '''
                }
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
        stage('Push to ECR'){
            powershell '''
            docker push 362911127705.dkr.ecr.ap-south-1.amazonaws.com/test:latest
            '''
        }
    }
}
