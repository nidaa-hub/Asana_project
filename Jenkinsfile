pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control
                git 'https://github.com/nidaa-hub/Asana_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any required dependencies using pip
                sh 'pip install -r requirements.txt' // Assuming you have a requirements.txt file
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python test script
                sh 'python Test.UI_test.non_functional_test.py' // Modify this command according to how you run your tests
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

