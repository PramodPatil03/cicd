pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'Buildnig the app'
                run 'python -m venv .venv'
                run '.venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('test'){
            steps {
                echo 'Testing the app'
                run '.venv\\Scripts\\activate && python main.py'
            }
        }
        stage('deploy') {
            steps {
                echo 'Deploying the application'
            }
        }
    }
}
