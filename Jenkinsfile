pipeline {
  agent any
  stages {
    stage('check out code') {
      steps {
        git(url: 'https://github.com/azuzishouba/appium.git', branch: 'master')
      }
    }

    stage('test') {
      steps {
        sh '''pip install pytest
'''
      }
    }

  }
}