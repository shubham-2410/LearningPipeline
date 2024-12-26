pipeline{
  agent any
  stages{
    stage('Breakfast'){
      steps{
        echo "I am doing breakfast"
      }
    }
    stage('Workout'){
      steps{
        echo "I am doing Workout"
      }
    }
    stage('Study'){
      steps{
        echo "I am doing Study"
      }
    }
    stage('Family Time'){
      steps{
        echo "Its family Time"
      }
    }
    stage('Play Time'){
      steps{
        echo "Its Play Time"
      }
    }
  }
  post{
    success{
      echo "My day went well"
    }
    failure{
      echo "My day didn't go well"
    }
  }
}
