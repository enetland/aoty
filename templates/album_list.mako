<%!
    import re

    def class_char_filter(text):
        return re.sub('[^\w]', '', text)
%>


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
        <p>
          <div id='sort' class='btn-group' data-toggle="buttons-radio">
            <button type='button' class="btn btn-primary" data-sort-by='rank'>Rank</button>
            <button type='button' class="btn btn-primary" data-sort-by='listeners'>Popularity</button>
          </div>
        </p>
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
      $(document).ready(function() {
        $('#container').isotope({
          itemSelector : '.album',
          layoutMode : 'fitRows',
           getSortData : {
            rank : function ( $elem ) {
              return parseInt($elem.data('rank'));
            },
            listeners : function ( $elem ) {
              return parseInt($elem.data('listeners'));
            }
          }
        });

        $('#sort .btn').click(function(){
          if($(this).hasClass('active')){
            return true;
          }
          else{
            $(this).addClass('active');
            $(this).siblings().removeClass('active');
            $('#container').isotope({ sortBy : $(this).data('sort-by') });
          }
        });

        $('#filters .btn').click(function(){
          $(this).toggleClass('active');

          // JQuery select all buttons with active state, get data-filter-values
          selectors = $('#filters .active').map(function(){return $(this).data('filter-value');}).get();

          ///Set Isotope filter to this long selector
          var selector = selectors.join('');
          $('#container').isotope({ filter: selector });
        });
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
  <div class="label inside bottom fade album ${' '.join([class_char_filter(tag) for tag in album.tags()])}" data-label="${album.artist} - ${album.title}" data-rank='${album.rank}' data-listeners='-${album.listeners}'>
    <a href='${album.lastfm_url}'>
      <img alt="${album.artist} - ${album.title}" src="${album.image}">
    </a>
  </div>
</%def>

<%def name="filter_elememt(tag)">
  <button type="button" class="btn btn-default" data-filter-value=".${class_char_filter(tag.name)}">${tag.name}</button>
</%def>

