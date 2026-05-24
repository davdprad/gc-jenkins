pipeline {
    agent any

    triggers {
        cron('H/15 * * * *') 
    }

    stages {
        stage('Setup & Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test & Coverage') {
            steps {
                sh '''
                    ./venv/bin/python3 -m pytest --junitxml=result.xml --cov=app --cov-report=xml
                '''
            }
        }
    }

    post {
        always {
            junit 'result.xml'
            recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']])
        }
    }
}
