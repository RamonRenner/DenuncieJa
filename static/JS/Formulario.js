function validacao(){
	var Nome = document.getElementById('nome').value;
	var Sobrenome = document.getElementById('sobrenome').value;
	var CPF = document.getElementById('CPF').value;
	var Bairro = document.getElementById('bairro').value;
	var Rua = document.getElementById('rua').value;
	var Cidade = document.getElementById('cidade').value;
	var Estado = document.getElementById('estado').value;
	var Pais = document.getElementById('pais').value;
	var Idade = document.getElementById('idade').value;
	var Telefone = document.getElementById('telefone').value;
	var Email = document.getElementById('email').value;
	var a = document.getElementById('a').value;
	var b = document.getElementById('b').value;
	var ok = 0;
	

	if(Nome == ""){
		alert("Digite seu nome!");
	}else{
		ok++;
	}

	if(Sobrenome == ""){
		alert("Digite seu sobrenome!");
	}else{
		ok++;
	}

	if(CPF == ""){
		alert("Digite seu CPF!");
	}else{
		ok++;
	}
    
    if(Bairro == ""){
		alert("Informe seu bairro!");
		
	}else{
		ok++;
	}

	if(Rua == ""){
		alert("Informe sua rua!");
		
	}else{
		ok++;
	}

	if(Cidade == ""){
		alert("Informe sua Cidade!");
		
	}else{
		ok++;
	}

	if(Estado == ""){
		alert("Informe seu Estado!");
		
	}else{
		ok++;
	}

	if(Pais == ""){
		alert("Informe seu Pais!");
		
	}else{
		ok++;
	}
	
	if(Idade == ""){
		alert("Informe sua idade!");
		
	}else{
		ok++;
	}

	if(Telefone == ""){
		alert("Informe seu Telefone!");
		
	}else{
		ok++;
	}

	if(Email.indexOf('@')==-1 || Email.indexOf('.com')==-1){
		alert("Email inválido! Digite novamente.");
	}else{
		ok++;
	}

	if(a == ""){
		alert("Preenche o campo vazio!");
		
	}else{
		ok++;
	}

	if(b == ""){
		alert("Preenche o campo vazio!");
		
	}else{
		ok++;
	}

	if(ok == 13){
		alert("Entraremo em contato com você")
	}
}