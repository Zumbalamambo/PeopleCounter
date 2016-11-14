document.getElementById( "image-upload" ).addEventListener( "change", function( event ) {
  var image = this.files[0];

  var data = new FormData();
  data.append( 'file', image );
  data.append( 'csrfmiddlewaretoken', $( '[name="csrfmiddlewaretoken"]' ).val() );

  if( image.type.match( /image.*/ ) ) {
    $.ajax({
        url: 'http://localhost:8001/counter/analyze',
        type: 'POST',
        data:data,
        processData: false,
        contentType: false
    }).done( function( data ) {
      var jsonData = JSON.parse( data );
      $( "#image-results" ).html( '<h1>Found ' + jsonData.count + ' people!</h1><br/><img src="' + jsonData.path + '"/>' );
    });
  }
}, false );
