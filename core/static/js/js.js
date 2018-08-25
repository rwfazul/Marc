// This file will contains some aux js functions
   

$('#id_file').change(function () {
	var filename = $(this).val();

	$.ajax({
        url: '/validaCurriculo/',
        data: {
          'filename': filename
        },
        dataType: 'json',
        success: function (data) {
         	if (!data.response) {
            	
            	$('#alerta-curriculo-invalido').show();
            	$('#alerta-curriculo-invalido').html("Arquivo inválido: o arquivo dever ter a extensão .xml");

            	$('#id_file').val('');

            }else{
            	$('#alerta-curriculo-invalido').hide();
            }
        }
    });


});



/*$("#form_curriculo").submit(function () {
 	var username = "Leonardo"

  	$.ajax({
    	url: '/processaCurriculo/',
    	dataType: 'json',
    	success: function (data) {
      		if (data.is_taken) {
        		alert("A user with this username already exists.");
      		}
    	}
  	});

});*/


