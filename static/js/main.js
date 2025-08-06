document.addEventListener('DOMContentLoaded', () => {
    const difficultySlider = document.getElementById('difficulty');
    const difficultyValueSpan = document.getElementById('difficulty-value');
    const randomizeButton = document.getElementById('randomize-button');
    const routeDisplay = document.getElementById('route-display');

    const stations = [
        "Willowfield",
        "Hemdon Park",
        "Beechley",
        "Financial Quarter",
        "Stepford Victoria",
        "City Hospital",
        "Stepford Central",
        "Four Ways",
        "Stepford East",
        "Stepford High Street",
        "Whitefield Lido",
        "Stepford UFC",
        "Woodhead Lane",
        "Houghton Rake",
        "Whitefield",
        "St. Helens Bridge",
        "New Harrow",
        "Elsemere Pond",
        "Elsemere Junction",
        "Berrily",
        "East Berrily",
        "Beaulieu Park",
        "Morganstown",
        "Angel Pass",
        "Bodin",
        "Coxly Newtown",
        "Barton",
        "Coxly",
        "West Benton",
        "Faraday Road",
        "Eden Quay",
        "Newry",
        "Newry Harbour",
        "Benton",
        "Port Benton",
        "Morganstown Docks",
        "Whitney Green",
        "Greenslade",
        "Cambridge Street Parkway",
        "Ashlan Park",
        "Connolly",
        "Airport West",
        "James Street",
        "Farleigh",
        "Rosedale Village",
        "Esterfield",
        "Benton Bridge",
        "Airport Parkway",
        "Airport Central",
        "Terminal 1",
        "Terminal 2",
        "Terminal 3",
        "Hampton Hargate",
        "Upper Staploe",
        "Water Newton",
        "Rocket Parade",
        "Leighton Stepford Road",
        "Leighton City",
        "Leighton West",
        "Aslockby",
        "Carnalea Bridge",
        "Rayleigh Bay",
        "Edgemead",
        "Faymere",
        "Westercoast",
        "Millcastle Racecourse",
        "Millcastle",
        "Westwyvern",
        "Starryloch",
        "Northshore",
        "Llyn-by-the-Sea"
    ];

    // Set initial values on page load
    difficultySlider.value = 1;
    difficultyValueSpan.innerText = 1;

    randomizeButton.addEventListener('click', () => {
        if (stations.length === 0) {
            return;
        }
        const difficulty = difficultySlider.value;
        let startPoint = stations[Math.floor(Math.random() * stations.length)];
        let endPoint = stations[Math.floor(Math.random() * stations.length)];
        while (endPoint === startPoint) {
            endPoint = stations[Math.floor(Math.random() * stations.length)];
        }
        routeDisplay.innerText = `Starting station: ${startPoint}\nEnding station: ${endPoint}`;
    });

    difficultySlider.addEventListener('input', (event) => {
        difficultyValueSpan.innerText = event.target.value;
    });
});