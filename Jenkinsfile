pipeline {
    agent { dockerfile true }
    stages {
        stage('Unit tests') {
            steps {
                sh 'nosetests --exe --with-xunit --with-coverage --cover-xml --cover-package=demo'
            }
            post {
                always {
                    junit 'nosetests.xml'
                }
            }
        }
        stage('Regression') {
            steps {
                echo 'Doing regression test...'
            }
        }
        stage('Publishing image') {
            agent { any }
            steps {
                script {

                }
            }
        }
    }
}