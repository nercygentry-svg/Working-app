<!DOCTYPE html>
<html>
<head>
  <title>Mathematics - SmartLearn</title>
</head>
<body>
  <h2>Mathematics Quiz</h2>
  <p>What is 12 × 8?</p>
  <button onclick="checkAnswer(96)">96</button>
  <button onclick="checkAnswer(88)">88</button>
  <button onclick="checkAnswer(108)">108</button>

  <p id="result"></p>

  <script>
    function checkAnswer(answer) {
      if(answer === 96) {
        document.getElementById("result").innerHTML = "✅ Correct!";
      } else {
        document.getElementById("result").innerHTML = "❌ Try again!";
      }
    }
  </script>
</body>
</html>
