pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'Building the app'

                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('test') {
            steps {
                echo 'Testing the app'

                bat '.venv\\Scripts\\python main.py'
            }
        }

        stage('deploy') {
            steps {
                echo 'Deploying the application'
            }
        }
    }
}