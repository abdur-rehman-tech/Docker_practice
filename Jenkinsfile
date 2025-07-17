pipeline {
    agent any
    environment{
      IMAGE_NAME ='DockerFile/Docker_pratice'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abdur-rehman-tech/Docker_practice/'
            }
        }
        stage('Build Docker image') {
            steps {
                bat ' docker build -t %IMAGE_NAME% latest .'
            }
        }
        stage('Push to Dashboard') {
            steps {
              withCredentials([usernamePassword(credentialsId: 'Docker', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                bat ***
                echo %Docker_PASS% |
                docker login -u %Docker_USER% --password - stdin
                docker push %IMAGE_NAME%:latest
                docker logout
              ***
            }
        }
    }
}
