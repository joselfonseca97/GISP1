/*Medidas iniciales*/
var xmin=0;
var ymax=0;
var ancho=0;
var alto=0;
/*Capas*/
var datosEdificios={};
var datosAceras={};
var datosRutasEvacuacion={};
var datosVialidad={}
var datosZonasVerdes={}
var datosZonasSeguras={}

var showEdificios=true

function mostrarOcultarCapas(svgId,elementId){
    if (document.getElementById(svgId).style.display=='none')
        document.getElementById(svgId).style.display='inline'
    else
        document.getElementById(svgId).style.display='none'

    
}

function cargarMedidas()
{
    fetch('http://localhost:8080/medidas')
                .then(response=>response.json())
                .then(data=>verMapa('100%','100%',data))
}
/*
function cargarEdificios() 
{
    fetch('http://localhost:8080/edificios')
        .then(response=>response.json())
        .then(data=>datosEdificios=data)
}

function cargarAceras() 
{
    fetch('http://localhost:8080/aceras')
        .then(response=>response.json())
        .then(data=>datosAceras=data)
}

function cargarRutasEvacuacion()
{
    fetch('http://localhost:8080/rutasEvacuacion')
    .then(response=>response.json())
    .then(data=>datosRutasEvacuacion=data)
}

function cargarVialidad()
{
    fetch('http://localhost:8080/vialidad')
    .then(response=>response.json())
    .then(data=>datosVialidad=data)
}

function cargarZonasVerdes()
{
    fetch('http://localhost:8080/zonasVerdes')
    .then(response=>response.json())
    .then(data=>datosZonasVerdes=data)
}

function cargarZonasSeguras()
{
    fetch('http://localhost:8080/zonasSeguras')
    .then(response=>response.json())
    .then(data=>datosZonasSeguras=data)
}
*/

/*Orden del json
    - datos metricos
    -vialidad
    -aceras
    -zonas_verdes
    -zonasSeguras
    -rutasevacuacion
    -edificios
*/
function verMapa(width, height,data) 
{
    for(var i=1;i<data.length;i++){
        svg = crearSVG(width, height,data[0],i)
        ancho = parseFloat(data[0].ancho)
        alto = parseFloat(data[0].alto)
        if (alto > ancho)
            ancho_proporcional = alto / height;
        else
            ancho_proporcional = ancho / width;
        crear_path(svg, data[i], ancho_proporcional,i);
        document.getElementById("mapa").appendChild(svg);
    }
}

function crearSVG(width, height,dimensiones,nombre) { //done
    var xmlns = "http://www.w3.org/2000/svg";
    let o_svg = document.createElementNS(xmlns, "svg");
    o_svg.setAttribute('id', 'svg'+nombre);
    o_svg.setAttribute('width', width);
    o_svg.setAttribute('height', height);
    vb = dimensiones.xmin + ' ' + dimensiones.ymax + ' ' + dimensiones.ancho + ' ' + dimensiones.alto
    o_svg.setAttribute('viewBox', vb);
    return (o_svg)
}

function crear_path(svg, geometrias, ancho_proporcional,nombre) {
    let xmlns = "http://www.w3.org/2000/svg";
    for (geom in geometrias) {
        figura = document.createElementNS(xmlns, "path");
        figura.setAttribute("d", geometrias[geom].svg);
        figura.setAttribute("stroke", "black");
        figura.setAttribute("class", "objeto_espacial");
        figura.setAttribute("fill", colorRGB());
        figura.setAttribute("stroke-width", ancho_proporcional);
        figura.setAttribute("onclick", "mostrarEdificio(" + geometrias[geom].id + ")");
        svg.appendChild(crear_grupoSVG(figura, "Capa "+nombre));
    }
}

function crear_grupoSVG(svg, descripcion) {
    var xmlns = "http://www.w3.org/2000/svg";
    grupo = document.createElementNS(xmlns, "g");
    titulo = document.createElementNS(xmlns, "title");
    titulo.innerHTML = descripcion
    grupo.appendChild(titulo);
    grupo.appendChild(svg);
    return (grupo)
}

function mostrarEdificio(id)
{
    alert("Soy el edificio id:"+id)
}

function generarNumero(numero) {
    return (Math.random() * numero).toFixed(0);
}

function colorRGB() {
    var coolor = "(" + generarNumero(255) + "," + generarNumero(255) + "," + generarNumero(255) + ", 0.5)";
    return "rgba" + coolor;
}
