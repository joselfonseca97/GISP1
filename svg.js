//buildings available for details
const idEdificios=[29,16,6,8,148]

function showBtns()
{
    try{
        document.getElementById("btnEdificios").removeAttribute('disabled')
        document.getElementById("btnVialidad").removeAttribute('disabled')
        document.getElementById("btnAceras").removeAttribute('disabled')
        document.getElementById("btnZonasVerdes").removeAttribute('disabled')
        document.getElementById("btnZonasSeguras").removeAttribute('disabled')
        document.getElementById("btnRutasEvacuacion").removeAttribute('disabled')
        document.getElementById("btnBack").setAttribute('disabled','disabled')
    }
    catch(err){console.log(err)}
}
function hideBtns()
{   
    document.getElementById("btnEdificios").setAttribute('disabled','disabled')
    document.getElementById("btnVialidad").setAttribute('disabled','disabled')
    document.getElementById("btnAceras").setAttribute('disabled','disabled')
    document.getElementById("btnZonasVerdes").setAttribute('disabled','disabled')
    document.getElementById("btnZonasSeguras").setAttribute('disabled','disabled')
    document.getElementById("btnRutasEvacuacion").setAttribute('disabled','disabled')
    document.getElementById("btnBack").removeAttribute('disabled')
}
//request for an specific building (zoom in option)
function mostrarEdificio(id)
{
    if(idEdificios.includes(id))
    {
        hideBtns()
        limpiarMapa();
        fetch('http://localhost:8080/edificio/'+id)
        .then(response=>response.json())
        .then(data=>guardarDatos(data))
        .then(data=>verMapa('100%','100%',data))
    }else{
        alert("No hay informacion disponible para este edificio");
    }
}
//clear all svg within the canvas. Clear details labels
function limpiarMapa(){
    parent=document.getElementById('mapa')
    while(parent.firstChild)
        parent.removeChild(parent.firstChild);

    //edificios
    document.getElementById('lblNombreEdificio').setAttribute('value','')
    document.getElementById('lblNiveles').setAttribute('value','')
    document.getElementById('lblAreaEdificio').setAttribute('value','')
    //zonasSeguras
    document.getElementById('lblNombreZonaSegura').setAttribute('value','')
    document.getElementById('lblCapacidad').setAttribute('value','')
    document.getElementById('lblAreaZonaSegura').setAttribute('value','')
    document.getElementById('lblTipoTerreno').setAttribute('value','')
}
//show or hide layers
function mostrarOcultarCapas(svgId){
    if (document.getElementById(svgId).style.display=='none')
        document.getElementById(svgId).style.display='inline'
    else
        document.getElementById(svgId).style.display='none' 
}
//request that gets all layers data from DB
function cargarMedidas()
{
    limpiarMapa()
    showBtns()
    fetch('http://localhost:8080/medidas')
                .then(response=>response.json())
                .then(data=>verMapa('100%','100%',data))
}
//set information labels text
function guardarDatos(data)
{   
    //edificios
    document.getElementById('lblNombreEdificio').setAttribute('value','Nombre: '+data[1][0].nombre)
    document.getElementById('lblNiveles').setAttribute('value','Niveles: '+data[1][0].niveles)
    document.getElementById('lblAreaEdificio').setAttribute('value','Area: '+data[1][0].area)
    //zonasSeguras
    document.getElementById('lblNombreZonaSegura').setAttribute('value','Nombre: '+data[2][0].nombre)
    document.getElementById('lblCapacidad').setAttribute('value','Capacidad: '+data[2][0].capacidad)
    document.getElementById('lblAreaZonaSegura').setAttribute('value','Area: '+data[2][0].area)
    document.getElementById('lblTipoTerreno').setAttribute('value','Tipo Terreno: '+data[2][0].tipoterreno)
    return data;
}

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
        if(nombre==6)
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

function generarNumero(numero) {
    return (Math.random() * numero).toFixed(0);
}

function colorRGB() {
    var coolor = "(" + generarNumero(255) + "," + generarNumero(255) + "," + generarNumero(255) + ", 0.5)";
    return "rgba" + coolor;
}
