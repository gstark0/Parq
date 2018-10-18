var map = L.map('mapid').setView([52.78345, 18.24154], 18);
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);

// Add addresses to search bar suggestions list
addrList = '';
Object.keys(addr).forEach(function(address) {
	addrList += '<div class="address" onclick="goToAddress(\'' + address + '\')">' + address + '</div>'
})
document.getElementById('address-list-inner').innerHTML = addrList;

// Get info about free and occupied parking spots from API
var freeSpots = {}
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
	marker = new L.marker([x_coord, y_coord], {icon: markerIcon}).addTo(map)

	// On marker click
	marker.on('click', function() { loadTable(spot) })
})

function loadTable(coord) {
	x_coord = coord.split(',')[0];
	y_coord = coord.split(',')[1];

	fetch('/get_table?x=' + x_coord + '&y=' + y_coord, {
		method: 'GET',
		headers: {
			'Content-type': 'application/json'
		}
	})
	.then(data => data.json())
	.then(data => {
		console.log(data);
		document.getElementById('parking-table').style.display = 'flex';

		posTable = [];
		data.forEach(function(spot) {
			pos = spot['position']
			if(posTable[pos[0]] == undefined)
				posTable[pos[0]] = [];
			posTable[pos[0]][pos[1]] = spot['occupied'];
		})
		
		tableContent = '';
		posTable.forEach(function(row) {
			tableContent += '<tr>';
			row.forEach(function(spot) {
				if(!spot)
					tableContent += '<td><div class="empty-spot"></div></td>'
				else
					tableContent += '<td><div class="occupied-spot"></div></td>'
			})
			tableContent += '</tr>';
		})
		document.getElementById('spots-table').innerHTML = tableContent;
	})
}

function goToAddress(address) {
	document.getElementById('search-bar').value = address;
	map.setView([addr[address][0], addr[address][1]], 18);
	document.getElementById('address-list').style.display = 'none';
}

function focusSearchBar() {
	document.getElementById('address-list').style.display = 'block';
}

function focusoutSearchBar() {
	//document.getElementById('address-list').style.display = 'none';
}

function hideTable() {
	document.getElementById('parking-table').style.display = 'none';
}