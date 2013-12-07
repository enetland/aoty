<%def name="element(album)">
<div class="album ${' '.join(album.tags())}">${album.artist} - ${album.title}</div>
</%def>