pipeline {
    agent {
        docker {
            image 'abhilashmishra89/my_image:1.0.1'
        }
    }
    stages {
        stage('Build'){
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'echo "in Build Stage"'
                sh 'yum install sshpass -y'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "cp -r /scripts/bashrc /root/.bashrc"'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "source /root/.bashrc"'
                // sh 'sshpass -f password141 ssh -o strictHostKeyChecking=no root@localhost "cp -r /scripts/hosts /etc/"'
                // sh 'source ~/.bashrc'
                }
            }
        }    
        stage('Test'){
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'echo "in stage test"'
                // sh 'python test.py'
                }
            }
        }
        stage('Deploy'){
            steps{withEnv(["HOME=${env.WORKSPACE}"]) {
                // sh 'scp -r diskCheck.py my_config.py mailer.py  192.168.11.141:/scripts/'
                sh 'sshpass -p drishti123 scp -o strictHostKeyChecking=no  diskCheck.py  mailer.py  192.168.11.141:/scripts/'
                // sh 'sshpass -p drishti123 scp -o strictHostKeyChecking=no  my_config.py  192.168.11.141:/scripts/'
            }
        }
        }
        }
    }
