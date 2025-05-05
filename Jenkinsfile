pipeline {
    agent any

    environment {
        PROJECT_ID = "group-python"
        IMAGE_NAME = "surveypython-app"
        IMAGE_TAG = "cleanlatest"
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
                sh 'docker build -t $GCR_URL .'
            }
        }

        stage('Authenticate with GCR') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud auth configure-docker'
            }
        }

        stage('Push to GCR') {
            steps {
                sh 'docker push $GCR_URL'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f $DEPLOY_YAML'
                sh 'kubectl rollout restart deployment surveypython-app'
            }
        }
    }
}
