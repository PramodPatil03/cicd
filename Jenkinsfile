pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'Buildnig the app'
                sh 'python -m venv .venv'
                sh '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('test'){
            steps {
                echo 'Testing the app'
                sh '.venv\\Scripts\\python main.py'
            }
        }
        stage('deploy') {
            steps {
                echo 'Deploying the application'
            }
        }
    }
}
