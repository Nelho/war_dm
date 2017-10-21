var teste = ""
function request_ajax_relatorio(filtro, descricao, numero_cap){
		$("#title_conteudo").text("Lista de Relatórios " + descricao)
        console.log(numero_cap)
        $.ajax({
            url: '/avaliador/relatorios/' + filtro,
            type: 'GET',
            dataType: 'json',
            data: {'numero_cap':numero_cap},
        })
        .done(function(data) {
            console.log("success");
            console.log(data);
            $("#container_relatorios").empty();
            teste = data;
            create_relatorios(data)
        })
        .fail(function(data) {
            console.log(data);
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
    }

function create_relatorios(relatorios){
    var elemento_relatorio = $("#container_relatorios");
    var table_initial = '<table class="w3-table-all w3-hoverable">' +
									
                                    '<table class="w3-table-all w3-hoverable">' +  
                                        '<thead>' +
    										'<tr class="w3-light-gray">' +
    											'<th>Capítulo</th>' +
    											'<th>Data Envio</th>' +
    											'<th>Território</th>' +
    											'<th>Ação</th>' +
    										'</tr>' +
    									'</thead>';

    for(i = 0; i < relatorios["relatorios"].length; i++){
		var aux = relatorios["relatorios"][i]["data_envio"].split("-")
    	relatorios["relatorios"][i]["data_envio"] = aux[2] + "-" + aux[1] + "-" + aux[0]
    	table_initial += ('<tr>' + 
										'<td>'+ relatorios["relatorios"][i]["capitulo"] +'</td>' + 
    									'<td>'+ relatorios["relatorios"][i]["data_envio"] +'</td>' + 
    									'<td>'+ relatorios["relatorios"][i]["territorio"] +'</td>')
                                        if(relatorios["abrir_relatorio"]){
                                            table_initial += '<td><a href="/avaliador/relatorio/' + relatorios["relatorios"][i]["pk"] + '/?next=' + window.location.pathname +'" class="w3-btn w3-green">Abrir</a></td>';
                                        }else{
                                            table_initial += '<td><button class="w3-btn w3-green" disabled>Abrir</button></td>';
                                        }
    	}
    table_initial += '</tr>' +
    						'</table>' +
    						'</div>'
    elemento_relatorio.append(table_initial)
}
