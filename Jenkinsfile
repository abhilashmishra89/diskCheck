pipeline {
    agent {
        docker {
            image 'python:3.7.2'
        }
    }
    stages {
        stage('Build'){
            steps {
                sh 'echo "in Build Stage"'
                sh 'yum install sshpass -y'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "cp -r /scripts/bashrc /root/.bashrc"'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "source /root/.bashrc"'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "cp -r /scripts/hosts /etc/"'
                // sh 'source ~/.bashrc'
                
            }
        }    
        stage('Test'){
            steps{
                sh 'echo "in stage test"'
                // sh 'python test.py'
            }
        }
        stage('Deploy'){
            steps{
                // sh 'scp -r diskCheck.py my_config.py mailer.py  192.168.11.141:/scripts/'
                sh 'sshpass -p drishti123 scp -o strictHostKeyChecking=no  diskCheck.py my_config.py mailer.py  192.168.11.141:/scripts/'
            }
        }
        
        }
    }
