fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b', {
    method: 'GET',
    headers: { 'Authorization': 'Bearer vmit8bqsm403wpk770oic8pjx691iqtnto847iii' }
})
    .then((response) => response.json())
    .then((data) => {
        
        const gsList = document.getElementById('gs-dates-list');
        const cityList = document.getElementById('city-dates-list');

        gsList.innerHTML = '';
        cityList.innerHTML = '';

        data.forEach((item) => {
            if (item.GS) {
                const gsli = document.createElement('li');
                gsli.className = 'list-group-item';
                gsli.textContent = item.GS;
                gsList.appendChild(gsli);
            }

            if (item.City) {
                const cityli = document.createElement('li');
                cityli.className = 'list-group-item';
                cityli.textContent = item.City;
                cityList.appendChild(cityli);
            }
        });
    })
    .catch((error) => console.log('Error:', error));