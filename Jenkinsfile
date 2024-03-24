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
                sh 'python Test.login_test.py' // Modify this command according to how you run your tests
            }
        }
    }
}

