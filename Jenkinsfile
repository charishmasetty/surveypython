pipeline {
    agent any

    environment {
        PROJECT_ID = "group-python"
        IMAGE_NAME = "surveypython-app"
        IMAGE_TAG = "v1-${new Date().getTime()}" // dynamic timestamp tag
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
                sh 'docker buildx create --use || echo "buildx already exists"'
                sh 'docker buildx build --platform=linux/amd64 --no-cache -t $GCR_URL --push .'
            }
        }

        stage('Authenticate with GCR') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud auth configure-docker'
            }
        }

        stage('Update YAML with New Image Tag') {
            steps {
                // Update image tag inside deployment.yaml
                sh "sed -i '' 's|image: gcr.io/.\\+|image: $GCR_URL|' $DEPLOY_YAML"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f $DEPLOY_YAML'
                sleep(time: 2, unit: 'SECONDS')
                sh 'kubectl rollout restart deployment surveypython-app'
            }
        }
    }
}
