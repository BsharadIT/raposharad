node {

stage("Fetch code from git") {
        echo 'Hello World'
        result = sh(script:'ls -al', returnStdout: true)
        echo result
}

}
