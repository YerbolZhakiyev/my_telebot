pipeline {
    agent any
    
    stages {

	stage('Delete Repository') {
            steps {
		script {
                // Delete old repository
		sh 'rm -rf var/jenkins_home/workspace/'First pipeline'/*'
            	}
	    }
        }
        stage('Clone Repository') {
            steps {
		script {
                // Clone the repository
                sh 'git clone https://github.com/YerbolZhakiyev/my_telebot.git'
            	}
	    }
        }
        
	stage('Build') {
            steps {
                // Remove old version and build new
		script {
		sh 'rm -rf /root/my_telebot/*'
                sh 'docker cp my_jenkins:/var/jenkins_home/workspace/'First pipeline'/* /root/my_telebot'
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

