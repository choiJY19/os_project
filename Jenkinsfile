node {
        def app
        stage('Clone repository') {
        git 'https://github.com/choiJY19/os_project.git'
        }
        stage('Build image') {
                app = docker.build("bombgame")
        }
        stage('Push image') {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                }
        }
}
