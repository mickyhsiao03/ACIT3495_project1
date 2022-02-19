// function sendJSON(){
			
//     let name = document.querySelector('#userName');
//     let password = document.querySelector('#pw');
    
//     // Creating a XHR object
//     let xhr = new XMLHttpRequest();
//     let url = "submit.php";

//     // open a connection
//     xhr.open("POST", url, true);

//     // Set the request header i.e. which type of content you are sending
//     xhr.setRequestHeader("Content-Type", "application/json");

//     // Create a state change callback
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4 && xhr.status === 200) {

//             // Print received data from server
//             result.innerHTML = this.responseText;

//         }
//     };

//     // Converting JSON data to string
//     var data = JSON.stringify({ "userName": name.value, "password": password.value });

//     // Sending data with the request
//     xhr.send(data);
//     console.log(data)
// }
