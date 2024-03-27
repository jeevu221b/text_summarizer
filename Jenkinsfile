pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside('-u root') {
                        sh '''
                            pip install -r requirements.txt
                            pytest
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    def dockerImage = docker.build("my-flask-app:${env.BUILD_NUMBER}", '.')
                    dockerImage.run("-d -p 5000:5000") // Runs the Docker image in detached mode, mapping port 8080 on host to port 80 in the container
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}