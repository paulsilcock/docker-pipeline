pipeline {
    agent { dockerfile true }
    stages {
        stage('Unit tests') {
            steps {
                checkout scm
                echo 'Hello'
                //sh '. /data/demo/env/bin/activate && nosetests --with-xunit'
                archiveArtifacts 'nosetests.xml'
            }
        }
    }
}