pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && python -m pytest -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'mkdir -p /cargo'
                sh 'cp note_search.py /cargo/'
                sh 'echo "Build delivered to cargo folder"'
            }
        }
    }
}
