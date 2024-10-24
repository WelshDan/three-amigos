// dates.html - fetch upcoming dates from worksheet
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
                gsli.textContent = item.GS;
                gsList.appendChild(gsli);
            }

            if (item.City) {
                const cityli = document.createElement('li');
                cityli.textContent = item.City;
                cityList.appendChild(cityli);
            }
        });
    })
    .catch((error) => console.log('Error:', error));

// dates.html - navlist change active upcoming dates


// results.html - fetch results from previous quizzes from worksheet
fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b', {
    method: 'GET',
    headers: { 'Authorization': 'Bearer vmit8bqsm403wpk770oic8pjx691iqtnto847iii' }
})
    .then((response) => response.json())
    .then((data) => {

        const resultsDateList = document.getElementById('results-date-list');
        const resultsWinnerList = document.getElementById('results-winner-list');
        const resultsSecondList = document.getElementById('results-second-list');
        const resultsThirdList = document.getElementById('results-third-list');

        resultsDateList.innerHTML = '';
        resultsWinnerList.innerHTML = '';
        resultsSecondList.innerHTML = '';
        resultsThirdList.innerHTML = '';

        data.forEach((item) => {
            if (item.Date) {
                const resdate = document.createElement('li');
                resdate.textContent = item.Date;
                resultsDateList.appendChild(resdate);
            }

            if (item.Quiz_Winner) {
                const reswin = document.createElement('li');
                reswin.textContent = item.Quiz_Winner;
                resultsWinnerList.appendChild(reswin);
            }

            if (item.Second_Place) {
                const ressecond = document.createElement('li');
                ressecond.textContent = item.Second_Place;
                resultsSecondList.appendChild(ressecond);
            }

            if (item.Third_Place) {
                const resthird = document.createElement('li');
                resthird.textContent = item.Third_Place;
                resultsThirdList.appendChild(resthird);
            }
        });
    })
    .catch((error) => console.log('Error:', error));
