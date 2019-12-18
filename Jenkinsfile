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
                sh 'cp -r diskCheck.py /scripts/'
            }
        }
        
        }
    }
