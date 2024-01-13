pipeline {
    agent any

    stages {
        stage('Generate Table of 17') {
            steps {
                script {
                    echo "Multiplication Table of 17:"
                    for (int i = 1; i <= 10; i++) {
                        def result = 17 * i
                        echo "17 x $i = $result"
                    }
                }
            }
        }
    }
}
