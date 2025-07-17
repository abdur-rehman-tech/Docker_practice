pipeline {
    agent any

    environment {
        IMAGE_NAME = 'dockerfile/docker_practice'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abdur-rehman-tech/Docker_practice/'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push %IMAGE_NAME%
                    docker logout
                    """
                }
            }
        }
    }
}
