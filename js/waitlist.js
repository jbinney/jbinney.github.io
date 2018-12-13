function update() {
  var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('GET', 'https://api.robinhood.com/midlands/tailgate/mcduckling/spot/joe%40robinhood.com/', true);
	xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == 4) {
					if(xmlhttp.status == 200) {
							var obj = JSON.parse(xmlhttp.responseText);
							var number = obj.spot_number_total;
							document.getElementById("number").innerHTML = number;
					 }
			}
	};
	xmlhttp.send(null);
}

setInterval(update, 3000);
