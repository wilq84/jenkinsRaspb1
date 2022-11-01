pipeline {
  agent any
  stages {
    stage('python config') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install boto3'
        sh 'mkdir .aws'
        sh 'cp /home/pi/.aws/* .aws/'
      }
    }
    stage('aws instance stop') {
      steps {
        sh 'python3 aws_docker_stop.py'
      }
    }
  }
}
