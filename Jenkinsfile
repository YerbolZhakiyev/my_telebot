pipeline {
    agent any
   //sdfsdf
    stages {
        stage('Pull changes') {
            steps {
		script {
                sh 'git fetch origin'
		sh 'git pull origin main'
            	}
	    }
        }

	stage('Build') {
            steps {
                // Remove old version and build new
		script {
		sh 'rm -rf /root/my_telebot/'
                sh 'scp /var/jenkins_home/workspace/'First pipeline'/ root@64.227.127.179:/root/my_telebot'
        	}
	    }
        }
	
	stage('Restart bot') {
            steps {
                // Restarting service
		sh 'systemctl restart bot_start'
            }
        }

        // Add more stages here as needed
    }
    
    // Add post-build actions here as needed
}

