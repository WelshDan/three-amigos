// dates.html - fetch upcoming dates from worksheet
const fetchUpcomingQuizzes = () => {
    fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b?sheet=upcoming_quizzes', {
        method: 'GET',
        headers: { 'Authorization': 'Bearer vmit8bqsm403wpk770oic8pjx691iqtnto847iii' }
    })
        .then((response) => response.json())
        .then((data) => {
            
            const gsList = document.getElementById('gs-dates-list');
            const cityList = document.getElementById('city-dates-list');

            gsList.innerHTML = '';
            cityList.innerHTML = '';

            let gsActive = false;
            let cityActive = false;

            data.forEach((item, index) => {

                if (index === 0 && item.GS === 'GS' && item.City === 'City') return;

                if (item.GS) {
                    gsActive = true;
                    const gsli = document.createElement('tr');
                    gsli.innerHTML = `<td>${item.GS}</td>`;
                    gsList.appendChild(gsli);
                }

                if (item.City) {
                    cityActive = true;
                    const cityli = document.createElement('tr');
                    cityli.innerHTML = `<td>${item.City}</td>`;
                    cityList.appendChild(cityli);
                }
            });
            
            if (gsActive = false) {
                gsList.innerHTML = `<tr><td>"No dates available"</td></tr>`;
            }

            if (cityActive = false) {
                cityList.innerHTML = `<tr><td>"No dates available"</td></tr>`;
            }            

        })
        .catch((error) => console.log('Error fetching upcoming quizzes:', error));
};

// results.html - fetch results from previous quizzes from worksheet
const fetchPreviousQuizzes = () => {
    fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b?sheet=past_quizzes_normal', {
        method: 'GET',
        headers: { 'Authorization': 'Bearer vmit8bqsm403wpk770oic8pjx691iqtnto847iii' }
    })
        .then((response) => response.json())
        
        .then((data) => {
            console.log("Previous quizzes data:", data);
            const resultsNormalList = document.getElementById('results-normal-list');
            if (resultsNormalList) {
                resultsNormalList.innerHTML = '';

                data.forEach((item) => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.Date || 'N/A'}</td>
                        <td>${item.Quiz_Winners || 'N/A'}</td>
                        <td>${item.Second_Place || 'N/A'}</td>
                        <td>${item.Third_Place || 'N/A'}</td>
                    `;
                    resultsNormalList.appendChild(row);
                });
            } else {
                console.error("results-normal-list item not found");
            } 
        })
        .catch((error) => console.log('Error fetching previous quizzes:', error));
};

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('gs-dates-list') || document.getElementById('city-dates-list')) {
        fetchUpcomingQuizzes();
    }

    if (document.getElementById('results-normal-list')) {
        fetchPreviousQuizzes();
    }
});