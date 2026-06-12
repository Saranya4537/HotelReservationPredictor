pipeline{
    agent any

    stages{
        stage('Cloning Github repo to Jenkins') {
            steps {
                script {
                    // Build the Docker image using the custom Jenkinsfile
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins_git_integration', url: 'https://github.com/Saranya4537/HotelReservationPredictor.git']])
                }
            }
        }
        stage('Setting up our virtual environment and installing dependencies') {
            steps {
                script {
                    echo 'Setting up our virtual environment and installing dependencies'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }
            }
        }
        
    }
}
