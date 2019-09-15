$(document).ready(function() {
  //add search functionality

  $(".song-search").keyup(function(e) {
    if(e.which == 13) {
      let element = this.parentElement;
      let query = this.value;
      console.log(query);
      let safe_query = encodeURIComponent(query);


      //do the ajax call
      let server_url = "http://127.0.0.1:5005/getData"; //TODO get the server_url
      $.get(server_url+"?q="+safe_query, function(data) {
        console.log(data);
        ids = data;
        console.log(element);

        for (let i = 0; i < ids.length; i++){
          let link = "https://open.spotify.com/embed/track/" + ids[i];
          let iframe_container = document.createElement("div");
          let iframe_el = document.createElement("iframe");
          let attr = {
            "src":link,
            "width": "300",
            "height": "80",
            "frameborder": "0",
            "allowtransparency": "true",
            "allow": "encrypted-media"
          };
          for (key in attr){
            iframe_el.setAttribute(key, attr[key]);
          }
          iframe_container.appendChild(iframe_el);
          iframe_container.classList.add("iframe-container");
          iframe_container.addEventListener("click", function() {
            if (element.classList.contains("ms")) {
              sessionStorage.setItem("melodyId", ids[i]);
              this.classList.toggle("iframe-container-toggle");
            }
            else if (element.classList.contains("hs")) {
              sessionStorage.setItem("harmonyId", ids[i]);
              this.classList.toggle("iframe-container-toggle");
            }
            else {
              sessionStorage.setItem("beatId", ids[i]);
              this.classList.toggle("iframe-container-toggle");
            }
          });
          element.appendChild(iframe_container);

        }

      }, "json");

    }
  });
});
