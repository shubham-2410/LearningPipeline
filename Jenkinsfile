// pipeline{
//   agent any
//   stages{
//     stage('Breakfast'){
//       steps{
//         echo "I am doing breakfast"
//       }
//     }
//     stage('Workout'){
//       steps{
//         echo "I am doing Workout"
//       }
//     }
//     stage('Study'){
//       steps{
//         echo "I am doing Study"
//       }
//     }
//     stage('Family Time'){
//       steps{
//         echo "Its family Time"
//       }
//     }
//     stage('Play Time'){
//       steps{
//         echo "Its Play Time"
//       }
//     }
//   }
//   post{
//     success{
//       echo "My day went well"
//     }
//     failure{
//       echo "My day didn't go well"
//     }
//   }
// }



// node{
//   stage('Build'){
//         echo 'building'
//   }
//   stage('Test'){
//     echo 'testing'
//   }

//   if(currentBuild.result =='SUCCESS'){
//     echo 'looks good'
//   }
//   else{
//     echo 'failed'
//   }
    
// }


pipeline{
	agent any
	environment{
		PYTHON_PATH = 'C:\Users\HP\AppData\Local\Programs\Python\Python311;C:\Users\HP\AppData\Local\Programs\Python\Python311\Scripts'
	}
	
	stages{
		stage('Checkout'){
			step{
				checkout scm
			}
		}

		stage('Build'){
			step{
				bat '''
					set PATH = %PYTHON_PATH%;%PATH%
					pip install -r requirements.txt
				'''
			}
		}
	
		stage('SonarAnalysis'){
			environment{
				SONAR_TOKEN = credentials('sonarqube-token')
			}

			steps{
				bat '''
					set PATH = %PYTHON_PATH%;%PATH%
					sonar-scanner -Dsonar.projectKey=LearnPipeline ^
          				-Dsonar.sources=. ^
          				-Dsonar.host.url=http://localhost:9000 ^
          				-Dsonar.token=%SONAR_TOKEN%
				'''
			}
		}
	}

  post{
    success{
      echo "Pipeline Successfull"
    }
    failure{
      echo "Pipeline Failure"
    }
  }
}

