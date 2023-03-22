pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting git pull.....'
                echo '---------------------------------------------'
                sh 'ssh root@$HOST_ADDRESS -tt "cd /root/my_telebot; git pull origin"'
                echo '------------------Success--------------------'
                echo '---------------------------------------------'
            }
        }

        stage('Testing backend') {
            steps {
                echo 'Starting test.....'
                echo '---------------------------------------------'
                echo '------------------Success--------------------'
                echo '---------------------------------------------'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Deployment....'
                echo '---------------------------------------------'
                sh "ssh root@${HOST_ADDRESS} -tt 'cd /root/my_telebot; export URL_GF=http://${HOST_ADDRESS}/grafana/; export HOST_ADDR=${HOST_ADDRESS}; docker-compose stop db nginx backend tg_bot; docker-compose build; docker-compose up -d'"
                echo '------------------Success--------------------'
                echo '---------------------------------------------'
            }
        }
    }
}