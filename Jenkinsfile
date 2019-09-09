#!/usr/bin/groovy

// load pipeline functions
// Requires pipeline-github-lib plugin to load library from github

@Library('github.com/lachie83/jenkins-pipeline@dev')
def pipeline = new io.estrado.Pipeline()


node {
  def app



  def pwd = pwd()
  def tool_name = "rpms"
  def user_id = ''
  wrap([$class: 'BuildUser']) {
      echo "userId=${BUILD_USER_ID},fullName=${BUILD_USER},email=${BUILD_USER_EMAIL}"
      user_id = "${BUILD_USER_ID}"
  }

  sh "env"

  stage('Clone repository') {
      /* Let's make sure we have the repository cloned to our workspace */
      checkout scm
  }

  stage('Make the RPMS') {
      sh "make rpms"
  }

  stage('Output of the directory') {
      sh "ls -la"
  }

  stage('Current Location on the Docker Container of the files.  To access them you must access the Jenkins container and then copy the files over') {
      sh "pwd"
  }

}