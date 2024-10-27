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
                    const resnormal = document.createElement('li');
                    resnormal.textContent = `${item.Date || 'N/A'} - ${item.Quiz_Winners || 'N/A'} - ${item.Second_Place || 'N/A'} - ${item.Third_Place || 'N/A'}`;
                    resnormal.classList.add('list-group-item');
                    resultsNormalList.appendChild(resnormal);
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