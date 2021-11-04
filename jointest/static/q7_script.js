// JS

$(document).ready(function() {
    $('.datepicker').datepicker({dateFormat: 'yy-mm-dd'});

    //Coletar os alvos e marcar eles ao carregar a pagina
    $.ajax({
        url: '/api/alvos',
        success: function (data) {
            
            for (x in data){
                marcar_mapa(
                    data[x]['pk'], 
                    data[x]['longitude'], 
                    data[x]['latitude']
                );
            }
        }
    })
});

// Declara camadas para o mapa
const vectorSource = new ol.source.Vector({});
  
const vectorLayer = new ol.layer.Vector({
    source: vectorSource,
});

// Declara mapa com as camadas
const map = new ol.Map({
    layers:[
        new ol.layer.Tile({
            source: new ol.source.OSM()
        }),
        vectorLayer
    ],
    target: document.getElementById('map'),
    view: new ol.View({
        center: [0, 0],
        zoom: 0,
        maxZoom: 3,
    }),
});

var last_feature; //armazena ultima feature clicada
// mostra modal ao clicar
map.on('click', function (evt) {
    const feature = map.forEachFeatureAtPixel(evt.pixel, function (feature) {
        return feature;
    });
    
    if(feature){ // Se o usuário tiver clicaco em um marcador
        last_feature = feature;
        get_alvo(feature.get('pk'));
    }    
});
  
// muda cursor do mouse sob o marcador
map.on('pointermove', function (e) {
    const pixel = map.getEventPixel(e.originalEvent);
    const hit = map.hasFeatureAtPixel(pixel);
    map.getTarget().style.cursor = hit ? 'pointer' : '';
});

//marca ponto no mapa
function marcar_mapa(new_pk, new_lon, new_lat) {
    f1 = new ol.Feature({
        geometry: new ol.geom.Point(ol.proj.fromLonLat([new_lon, new_lat])),
        pk: new_pk
    })
    vectorSource.addFeature(f1)
}

function desmarcar_mapa(feature){
    vectorSource.removeFeature(feature)
}

// Pega informaçoes do alvo ao clicar nele no mapa
function get_alvo(pk){

    $.ajax({        
        url: '/api/alvos/'+pk,
        success: function (response) {           
            
            $('#updateModal #id_nome').val(response['nome']);
            $('#updateModal #id_latitude').val(response['latitude']);
            $('#updateModal #id_longitude').val(response['longitude']);
            $('#updateModal #id_expiration_date').val(response['expiration_date']);

            $('#updateModal').modal('show')
        }
    })

}

// salva modificações do alvo no banco de dados
function update_alvo(feature){

    let my_pk = feature.get('pk')
    let form_serialized = $("#updateModal #form-modal").serialize();
    
    $.ajax({
        type:'POST',
        url: '/ajax/update_alvo/'+my_pk,
        data: form_serialized,
        success: function (response) {
            
            let new_lon = $("#updateModal #id_longitude").val()
            let new_lat = $("#updateModal #id_latitude").val()
            $("#updateModal #form-modal").trigger('reset')

            // atualiza ponto no mapa
            desmarcar_mapa(feature)
            marcar_mapa(my_pk, new_lon, new_lat);
        }
    })
}

$("#createAlvo").on('click', function(){
    let form_serialized = $("#createModal #form-modal").serialize();

    //console.log(form_serialized)
    $.ajax({
        type:'POST',
        url: '/ajax/create_alvo',
        data: form_serialized,
        success: function (response) {
            
            let new_lon = $("#createModal #id_longitude").val()
            let new_lat = $("#createModal #id_latitude").val()
            $("#createModal #form-modal").trigger('reset')

            marcar_mapa(response, new_lon, new_lat);
        }
    })
})

$("#btnUpdate").on('click', function(){
    update_alvo(last_feature);
})

$("#btnRemove").on('click', function(){

    let my_pk = last_feature.get('pk')
    
    $.ajax({
        url: '/ajax/delete_alvo/'+my_pk,
        success: function (response) {
            
            $("#updateModal #form-modal").trigger('reset')
            // atualiza ponto no mapa
            desmarcar_mapa(last_feature)
            $('#updateModal').modal('hide')

        }
    })
})