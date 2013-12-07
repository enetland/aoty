<div id='container'>
% for a in albums:
  ${element(a)}
%endfor
</div>

<%def name="element(album)">
  <div class="album ${' '.join(album.tags())}">
    <img alt='${album.artist} - ${album.title}' src='${album.image}'>
  </div>
</%def>