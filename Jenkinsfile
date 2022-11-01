pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('aws instance stop') {
      steps {
        sh 'python3 aws_docker_stop.py'
      }
    }
  }
}
