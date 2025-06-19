pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t python-flask-docker-ecs-loadbalancer .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm python-flask-docker-ecs-loadbalancer pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 python-flask-docker-ecs-loadbalancer'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
    }
}