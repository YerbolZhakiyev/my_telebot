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
        stage('Deploy') {
            steps {
                echo 'Starting Deployment....'
                echo '---------------------------------------------'
                sh 'ssh root@$HOST_ADDRESS -tt "cd /root/my_telebot; docker-compose stop db backend nginx tg_bot; docker-compose build; docker-compose up -d"'
                echo '------------------Success--------------------'
                echo '---------------------------------------------'
            }
        }
        stage('Testing backend') {
            steps {
                echo 'Starting test.....'
                echo '---------------------------------------------'
                sh 'ssh root@$HOST_ADDRESS -tt "python3 /root/my_telebot/test/test_flask.py"'
                echo '------------------Success--------------------'
                echo '---------------------------------------------'
            }
        }
    }
}