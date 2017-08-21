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
                    script {
                        step([
                                $class: 'CoberturaPublisher',
                                coberturaReportFile: 'coverage.xml',
                                maxNumberOfBuilds: 0,
                                onlyStable: false,
                                sourceEncoding: 'ASCII',
                                zoomCoverageChart: false
                        ])
                    }
                }
            }
        }
        stage('Regression') {
            steps {
                echo 'Doing regression test...'
            }
        }
        stage('Publishing image') {
            agent any
            steps {
                script {
                    image = docker.build('my/image/demo')
                    docker.withRegistry('http://localhost:5000') {
                        image.push("$env.BUILD_NUMBER")
                        image.push("latest")
                    }
                }
            }
        }
    }
}