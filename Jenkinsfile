def image

stage('Clone') {
    node {
        checkout scm
    }
}

stage('Build image') {
    image = docker.build('my/image/demo')
}

stage('Unit tests') {
    image.inside {
        sh 'nosetests --exe --with-xunit --with-coverage --cover-xml --cover-package=demo'
        junit 'nosetests.xml'
        step([
                $class             : 'CoberturaPublisher',
                coberturaReportFile: 'coverage.xml',
                maxNumberOfBuilds  : 0,
                onlyStable         : false,
                sourceEncoding     : 'ASCII',
                zoomCoverageChart  : false
        ])
    }
}
stage('Regression') {
    echo 'Doing regression test...'
}

stage('Publishing image') {
    docker.withRegistry('http://localhost:5000/my/image/demo') {
        image.push("latest")
    }
}
