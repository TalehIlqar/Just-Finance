
const SubsciberLogic = {
	emailManager(email) {
		fetch('/api/subscriberapi/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				'email': email,
			})
		})
			.then(response => response.json())
			.then(data => {
                console.log(data);
				subscribeModalLongTitle = document.getElementById('subscribeModalLongTitle');
				if (data['success'] === true) {
					emailinput.value = '';
					emailinput.placeholder = 'Enter your email';
					subscribeModalLongTitle.innerText = data['message'];
				} else {
					subscribeModalLongTitle.innerText = data['email'][0];
				}
			});
	}
}

emailbutton = document.getElementById('emailbutton')
emailinput = document.getElementById('emailinput')

emailbutton.onclick = function () {
	const email = emailinput.value;
	SubsciberLogic.emailManager(email);
}
