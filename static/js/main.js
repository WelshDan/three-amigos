fetch('https://sheetdb.io/api/v1/fvi6b7rkv2z2b', {
    method: 'GET',
    headers: { 'Authorization': 'Bearer {token}' }
})
    .then((response) => response.json())
    .then((data) => console.log(data));