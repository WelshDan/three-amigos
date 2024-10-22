fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b', {
    method: 'GET',
    headers: { 'Authorization': 'Bearer vmit8bqsm403wpk770oic8pjx691iqtnto847iii' }
})
    .then((response) => response.json())
    .then((data) => {
        const datesList = document.getElementById('dates-list');

        data.forEach((item) => {
            const li = document.createElement('li');
            li.textContent = item.Dates;
            datesList.appendChild(li);
        });
    })
    .catch((error) => console.log('Error:', error));