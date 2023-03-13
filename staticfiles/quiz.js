function getName(){
	login = document.getElementById("login").value;
	alert("Hi, " + login);
	return login;
}
function submitAnswers(answers){

	var total = answers.length;
	var score = 0;
	var choice = []

	for(var i = 1; i <= total; i++){

		choice[i] = document.forms["quizForm"]["q"+i].value;
	}

	for(i = 1; i <= total; i++){
		if(choice[i] == answers[i - 1]){
			score++;
		}
	}

}

