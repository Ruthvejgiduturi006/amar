pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ruthvejgiduturi006/amar.git'
            }
        }

        stage('Compile') {
            steps {
                echo 'Compiling Java file...'
                bat 'javac Main.java'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Java Program...'
                bat 'java Main'
            }
        }
    }
}
