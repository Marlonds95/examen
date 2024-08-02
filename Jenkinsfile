node {
    // Define las variables de entorno
    def pythonPath = 'C:\\Users\\EQUIPO\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    def emailScriptPath = 'C:\\ProgramData\\Jenkins\\.jenkins\\scripts\\send_email.py'
    def repoUrl = 'https://github.com/Marlonds95/app-web2-ejer3-mat-activida.git'
    def repoBranch = 'master'
    def serverPath = 'C:\\servidor\\examen'

    try {
        stage('Revisión') {
            // Checkout del código fuente desde el repositorio bifurcado
            checkout([
                $class: 'GitSCM',
                branches: [[name: "*/${repoBranch}"]],
                userRemoteConfigs: [[url: repoUrl]]
            ])
        }

        stage('Mover al servidor') {
            // Limpia la carpeta en el servidor
            bat "del /q ${serverPath}\\*"
            bat "for /D %%p IN (${serverPath}\\*) DO rd /s /q \"%%p\""

            // Verifica que la carpeta esté vacía
            bat "echo Verificando que la carpeta esté vacía..."
            bat "dir ${serverPath}"

            // Copia los archivos del repositorio al servidor
            bat "xcopy C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\${env.JOB_NAME}\\* ${serverPath} /E /I /Y"

            // Verifica que los archivos se hayan copiado
            bat "echo Verificando que los archivos se hayan copiado..."
            bat "dir ${serverPath}"
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
