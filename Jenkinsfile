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

                
            }
        }

        stage('deploy') {
            steps {
                echo 'Deploying the application'
                bat '.venv\\Scripts\\python main.py'
                echo 'Application deployed successfully, please check http://localhost:5000/hello'
            }
        }
    }
}