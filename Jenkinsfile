#!/usr/bin/groovy

// load pipeline functions
// Requires pipeline-github-lib plugin to load library from github

@Library('github.com/lachie83/jenkins-pipeline@dev')
def pipeline = new io.estrado.Pipeline()


node {
  def app



  def pwd = pwd()
  def chart_dir = "$pwd/helm/"
  def tool_name = "suricata"
  def container_dir = "$pwd/container/"
  def custom_image = "images.suricata"
  def custom_values_url = "http://repos.sealingtech.com/cisco-c240-m5/suricata/values.yaml"
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
}