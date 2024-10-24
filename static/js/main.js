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

    const tabs= document.querySelectorAll('.nav-link');
    const all_content= document.querySelectorAll('.tab-content');

    tabs.forEach((tab, index)=>{
        tab.addEventListener('click', ()=>{
            tabs.forEach(tab=>{tab.classList.remove('active')});
            tab.classList.add('active');
        
        all_content.forEach(content=>{content.classList.remove('active')});
        all_content[index].classList.add('active');
        })
    })