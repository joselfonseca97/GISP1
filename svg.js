function cargar_figura() 
{
    fetch('http://localhost:8080/edificios')
    .then(response=>console.log(response.json()))
    //.then(response => response.json())
    //.then(data=>console.log(data));
    //.then(data => verMapa('100%', '100%', data));
}
var test;
function verMapa(width, height, geometrias) 
{
    svg = crearSVG(width, height, geometrias.dimensiones[0])
    ancho = parseFloat(geometrias.dimensiones[0].ancho)
    alto = parseFloat(geometrias.dimensiones[0].alto)
    if (alto > ancho)
        ancho_proporcional = alto / height;
    else
        ancho_proporcional = ancho / width;
    crear_path(svg, geometrias.objetos, ancho_proporcional);

    document.getElementById("mapa").appendChild(svg);
}

function crearSVG(width, height, dimensiones) {
    var xmlns = "http://www.w3.org/2000/svg";
    let o_svg = document.createElementNS(xmlns, "svg");
    o_svg.setAttribute('id', 'svg');
    o_svg.setAttribute('width', width);
    o_svg.setAttribute('height', height);
    vb = dimensiones.xmin + ' ' + dimensiones.ymax + ' ' + dimensiones.ancho + ' ' + dimensiones.alto
    o_svg.setAttribute('viewBox', vb);
    return (o_svg)
}

function crear_path(svg, geometrias, ancho_proporcional) {
    let xmlns = "http://www.w3.org/2000/svg";
    for (geom in geometrias) {
        figura = document.createElementNS(xmlns, "path");
        figura.setAttribute("d", geometrias[geom].svg);
        figura.setAttribute("stroke", "black");
        figura.setAttribute("class", "objeto_espacial");
        figura.setAttribute("fill", colorRGB());
        figura.setAttribute("stroke-width", ancho_proporcional);
        figura.setAttribute("onclick", "mostrarEdificio(" + geometrias[geom].id + ")");
        svg.appendChild(crear_grupoSVG(figura, geometrias[geom].nombre));
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
