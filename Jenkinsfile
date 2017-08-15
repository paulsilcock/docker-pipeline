pipeline {
    agent { dockerfile true }
    stages {
        stage('Unit tests') {
            steps {
                sh 'nosetests --exe --with-xunit'
            }
            post {
                always {
                    junit 'nosetests.xml'
                }
            }
        }
    }
}