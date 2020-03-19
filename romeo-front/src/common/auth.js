import Axios from "axios";

export const setAuthToken = token => {
	Axios.defaults.headers.common["Authorization"] = token;
	localStorage.setItem("token", token);
};

export const removeAuthToken = () => {
	delete Axios.defaults.headers.common["Authorization"];
	localStorage.removeItem("token");
};

export const setCurrentClient = (username, type) => {
	console.log(username);
	localStorage.setItem("currentClient", JSON.stringify({username, type }));
};

export const getCurrentClient = () => {
	return JSON.parse(localStorage.getItem("currentClient"));
}

export const removeCurrentClient = () => {
	localStorage.removeItem("currentClient");
};