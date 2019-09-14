$(document).ready(function() {
  //add search functionality

  $(".song-search").keyup(function(e) {
      if(e.which == 13) {
        let element = this;
        let query = this.value;
        console.log(query);
        let safe_query = encodeURIComponent(query);


        //do the ajax call
        let server_url = "http://127.0.0.1:5005/getData"; //TODO get the server_url
        $.get(server_url+"?q="+safe_query, function(data) {
            console.log(data);
            ids = data;

            for (let i = 0; i < ids.length; i++){
              element.append('<iframe src="https://open.spotify.com/embed/track/' + ids[i] +  'width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>');
            }

          }, "json");

      }
  });
});
