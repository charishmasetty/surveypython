pipeline {
    agent any

    environment {
        IMAGE_NAME = "gcr.io/group-python/surveypython-app:cleanlatest"
        PROJECT_ID = "group-python"
        CLUSTER = "group-python-cluster"
        ZONE = "us-east1-b"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://your-git-repo-url.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Push to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcr-json-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                    sh 'gcloud auth configure-docker --quiet'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy to GKE') {
            steps {
                withCredentials([file(credentialsId: 'gcr-json-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                    gcloud container clusters get-credentials $CLUSTER --zone $ZONE --project $PROJECT_ID
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                    '''
                }
            }
        }
    }
}
