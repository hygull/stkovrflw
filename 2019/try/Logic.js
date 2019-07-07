function getSessionData() {
	let data = {
		sessionId: localStorage.getItem("sessionId")
	}

	return data
}

function allOk() {
	let data = getSessionData()
	let response = validateSession(data.sessionId)

	if(response is ok) {
		return true
	}

	return false
}

function getCustomers() {
	if(allOk()) {
		// Make API calls to get customers

	} else {
		// redirect to login page

	}
} 


function getSchemes() {
	if(allOk()) {
		// Make API calls to get schemes

	} else {
		// redirect to login page

	}
} 




