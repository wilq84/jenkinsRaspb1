pipeline {
  agent any
  stages {
    stage('python config') {
      steps {
        sh 'python3 --version'
        sh 'echo $PATH'
      }
    }
    stage('aws instance stop') {
      steps {
        sh 'python3 aws_docker_stop.py'
      }
    }
  }
}
