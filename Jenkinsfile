pipeline {
    agent { dockerfile true }
    stages {
        stage('Unit tests') {
            steps {
                checkout scm
                sh '. /data/demo/env/bin/activate && nosetests --exe --with-xunit'
                archiveArtifacts 'nosetests.xml'
            }
        }
    }
}