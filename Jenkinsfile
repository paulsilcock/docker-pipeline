pipeline {
    agent { dockerfile true }
    stages {
        stage('Unit tests') {
            checkout scm
            sh '. /data/demo/env/bin/activate && nosetests --with-xunit'
            archiveArtifacts 'nosetests.xml'
        }
    }
}