pipeline {
    agent any

    environment {
        PROJECT_ID = "group-python"
        IMAGE_NAME = "surveypython-app"
        IMAGE_TAG = "v1-${BUILD_NUMBER}"
        GCR_URL = "gcr.io/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG}"
        DEPLOY_YAML = "deployment.yaml"
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-service-account-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/charishmasetty/surveypython.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker buildx build --platform=linux/amd64 -t $GCR_URL --push .'
            }
        }

        stage('Authenticate with GCR') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud auth configure-docker'
            }
        }

        stage('Update Kubernetes Deployment') {
            steps {
                script {
                    // Patch deployment image with new tag
                    sh """
                        kubectl set image deployment/surveypython-app surveypython-app=$GCR_URL
                        kubectl rollout status deployment/surveypython-app
                    """
                }
            }
        }
    }
}
