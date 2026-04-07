window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const functionApi = 'https://hxoj0ksiak.execute-api.us-east-1.amazonaws.com/prod/visitor'; // Real Lambda API URL

const getVisitCount = () => {
    let count = 30; // Initial placeholder value
    fetch(functionApi)
        .then(response => {
            return response.json()
        })
        .then(response => {
            console.log("Website called function API.");
            count = response.count;
            document.getElementById('counter').innerText = count;
        }).catch(function (error) {
            console.log(error);
        });
    return count;
}
