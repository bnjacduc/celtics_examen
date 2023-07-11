$(document).ready(function() {
  $("#buscar").click(function() {
    $.getJSON("https://www.balldontlie.io/api/v1/teams", function(data) {

     
      var equipos = data.data;
      console.log(equipos)
      var tabla = $("#tabla-equipos tbody");
      tabla.empty();
      $.each(equipos, function(index, equipo) {
        var nombre = equipo.full_name;
        var ciudad = equipo.city;
        var division = equipo.division;
        var conferencia = equipo.conference;
        var tr = $("<tr>");
        tr.append($("<td>").text(nombre));
        tr.append($("<td>").text(ciudad));
        tr.append($("<td>").text(division));
        tr.append($("<td>").text(conferencia));
        tabla.append(tr);
      });
    });
  });
});
