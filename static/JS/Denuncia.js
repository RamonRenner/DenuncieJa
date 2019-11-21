function validacao(){
	var usuario = document.getElementById('usuario').value;
	var senha = document.getElementById('senha').value;
	var CPF = document.getElementById('CPF').value;
	var certo = 0;
	

	if(usuario == ""){
		alert("Obrigatorio informar o usuario");
	}else{
		certo++;
	}

	if(senha == ""){
		alert("Obrigatorio informar a senha");
	}else{
			certo++;
		}

	if(CPF == ""){
		alert("Obrigatorio informar o CPF");
	}else{
			certo++;
		}
}