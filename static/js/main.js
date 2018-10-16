var map = L.map('mapid').setView([52.78345, 18.24154], 18);
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);

// Get info about free and occupied parking spots from API
var freeSpots = {}
fetch('/get_data', {
	method: 'GET',
	headers: {
		'Content-type': 'application/json'
	}
})
.then(data => data.json())
.then(data => {
	data.forEach(function(parking) {
		parking['spots'].forEach(function(spot) {
			coord = spot['coord'];
			occupied = spot['occupied']
			// If number of free spots value is undefined
			if(freeSpots[coord] == undefined) {
				freeSpots[coord] = 0;
			}

			if(!occupied) {
				freeSpots[coord] += 1;
			}
		})
	})

	Object.keys(freeSpots).forEach(function(spot) {
		x_coord = parseFloat(spot.split(',')[0]);
		y_coord = parseFloat(spot.split(',')[1]);
		console.log(x_coord)
		console.log(y_coord)

		// Defined the look and value of the marker
		var markerIcon = L.divIcon({
			className: 'marker-icon-green',
			iconSize: [30, 30],
			iconAnchor: [15, 15],
			popupAnchor: [3, -40],
			html: '<span style="font-size: 20px;">' + freeSpots[spot] + '</span>'
		});

		// Place the marker
		console.log(freeSpots)
		var marker = new L.marker([x_coord, y_coord], {icon: markerIcon}).addTo(map);		
	})
})

/*
var markerIcon = L.divIcon({
		className: 'marker-icon-red',
		iconSize: [30, 30],
		iconAnchor: [15, 15],
		popupAnchor: [3, -40],
		html: '<span style="font-size: 20px;">0</span>'
});
 
var marker = new L.marker([52.78317,18.24167], {icon: markerIcon}).addTo(map);

var markerIcon = L.divIcon({
		className: 'marker-icon-green',
		iconSize: [30, 30],
		iconAnchor: [15, 15],
		popupAnchor: [3, -40],
		html: '<span style="font-size: 20px;">3</span>'
});

var marker = new L.marker([52.78310,18.24147], {icon: markerIcon}).addTo(map);

var markerIcon = L.divIcon({
		className: 'marker-icon-green',
		iconSize: [30, 30],
		iconAnchor: [15, 15],
		popupAnchor: [3, -40],
		html: '<span style="font-size: 20px;">8</span>'
});

var marker = new L.marker([52.78299,18.24128], {icon: markerIcon}).addTo(map);
*/