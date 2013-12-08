<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/label.min.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <title>AOTY</title>
  </head>
  <body>
  <div class='continer'>
    <div class='row'>
      <div class="col-sm-2">
        ${filters(tags)}
      </div>
      <div class="col-sm-10">
        ${list(albums)}
      </div>
    </div>
  </div>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script language="javascript" type="text/javascript" src="js/bootstrap.min.js"></script>
    <script language="javascript" type="text/javascript" src="js/jquery.isotope.min.js"></script>
    <script language="javascript" type="text/javascript">
      $('#container').isotope({
        itemSelector : '.album',
        layoutMode : 'fitRows'
      });

      $('#filters .filter_btn').click(function(){
        $(this).toggleClass('active');

        // JQuery select all buttons with active state, get data-filter-values
        selectors = $('#filters .filter_btn.active').map(function(){return $(this).data('filter-value');}).get();

        ///Set Isotope filter to this long selector
        var selector = selectors.join('');
        $('#container').isotope({ filter: selector });
        return false;
      });

    </script>
  </body>
</html>

<%def name="filters(tags)">
  <div id='filters'>
    % for t in tags:
      ${filter_elememt(t)}
    %endfor
  </div>
</%def>

<%def name="list(albums)">
  <div id='container'>
    % for a in albums:
      ${album_element(a)}
    %endfor
  </div>
</%def>

<%def name="album_element(album)">
  <div class="label inside bottom fade album ${' '.join(album.tags())}" data-label="${album.artist} - ${album.title}">
    <img alt="${album.artist} - ${album.title}" src="${album.image}">
  </div>
</%def>

<%def name="filter_elememt(tag)">
  <button type="button" class="filter_btn btn btn-default" data-filter-value=".${tag.name}">${tag.name}</button>
</%def>