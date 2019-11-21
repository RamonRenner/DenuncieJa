function validacao(){
	var usuario = document.getElementById('usuario').value;
	var senha = document.getElementById('senha').value;
	var email = document.getElementById('email').value;
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

	if(email == ""){
		alert("Obrigatorio informar o email");
	}else{
			certo++;
		}

	if(certo == 3){
		alert("Você foi cadastrado com sucesso, faça sua denuncia");
	}
}