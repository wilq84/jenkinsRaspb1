pipeline {
  agent any
  stages {
    stage('python config') {
      steps {
        sh 'python3 --version'
        sh 'export PYTHONPATH=$WORKSPACE:$PYTHONPATH'
      }
    }
    stage('aws instance stop') {
      steps {
        sh 'python3 aws_docker_stop.py'
      }
    }
  }
}
