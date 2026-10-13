
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'python --version'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'python test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat 'if not exist deployment mkdir deployment'
                bat 'copy /Y app.py deployment\\app.py'
            }
        }
    }
}
