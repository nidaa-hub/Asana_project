pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Building..'
                git 'https://github.com/nidaa-hub/Asana_project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Testing..'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Deploying..'
                bat 'python Test.UI_test.non_functional_test.py'
            }
        }
    }
    post {
        success {
            echo 'Tests passed successfully!'
            slackSend channel: "#asana_jenkins_update", message: "Build deployed successfully - ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
        }
        failure {
            echo 'Tests failed!'
            slackSend(channel: "#asana_jenkins_update", failOnError: true, message: "Build failed - ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}
