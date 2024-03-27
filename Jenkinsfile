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