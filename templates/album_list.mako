<%namespace name="album" file="./album.mako" />
<div id='container'>
% for a in albums:
  ${album.element(a)}
%endfor
</div>
