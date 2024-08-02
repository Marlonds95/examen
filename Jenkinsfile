node {
    // Define las variables de entorno
    def pythonPath = 'C:\\Users\\EQUIPO\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    def emailScriptPath = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Examen-uno\\envioCorreo.py'

    try {
        stage('Revisión') {
            // Checkout del código fuente desde el repositorio bifurcado
            checkout([
                $class: 'GitSCM',
                branches: [[name: '*/master']],
                userRemoteConfigs: [[url: 'https://github.com/Marlonds95/examen.git']]
            ])
        }

        stage('Mover al servidor') {
            bat 'del /q C:\\servidor\\examen\\*'
            bat 'for /d %i in (C:\\servidor\\examen\\*) do rd /s /q "%i"'
            
            // Copia los archivos del repositorio al servidor
            bat 'xcopy C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\${env.JOB_NAME}\\* C:\\servidor\\examen /E /I /Y'
        }

    } catch (Exception e) {
        // Manejo de errores en caso de que algo falle en las etapas
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        stage('Enviar correo') {
            // Ejecuta el script de Python para enviar un correo electrónico
            bat "${pythonPath} ${emailScriptPath}"
        }
    }
}
