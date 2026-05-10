pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --break-system-packages flask pytest'
            }
        }
        stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest app/tests/test_lib_serbia.py -v'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t tari:v01 .'
            }
        }
    }
}
