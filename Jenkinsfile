pipeline {
    agent any

    triggers {
        pollSCM('* * * * *') // Poll every minute for changes in the Git repository
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout the code from the Git repository
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9-slim').inside {
                        sh '''
                            pip install -r requirements.txt
                            pip install pytest
                            pytest tests/
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('my-flask-app:latest', '.')
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