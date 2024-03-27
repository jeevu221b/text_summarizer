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
                    docker.build("my-flask-app:${env.BUILD_NUMBER}", '.')
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