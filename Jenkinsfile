pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting git pull'
                sh 'ssh root@$HOST_ADDRESS -tt "cd /root/my_telebot; git pull origin"'
                echo '------------------Success--------------------'
            }
        }

        stage('Testing') {
            steps {
                echo 'Starting tests.....'
                sh "ssh root@${HOST_ADDRESS} -tt 'cd /root/my_telebot; docker-compose stop db backend; cd /root/my_telebot/test; docker-compose build; docker-compose up -d backend db; sleep 5; docker-compose up -d tests; docker logs tests > test.log; cat test.log; docker-compose down'"
                echo '------------------Success--------------------'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Deployment....'
                sh "ssh root@${HOST_ADDRESS} -tt 'cd /root/my_telebot; export URL_GF=http://${HOST_ADDRESS}/grafana/; export HOST_ADDR=${HOST_ADDRESS}; docker-compose stop db nginx backend tg_bot; docker-compose build; docker-compose up -d'"
                echo '------------------Success--------------------'
            }
        }
    }
}