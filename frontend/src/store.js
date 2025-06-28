import { reactive } from "vue";

export const store = reactive({
	balance: "",
	email: "",
	picture: "",
	username: "",
	url: "http://192.168.10.107:8000/",
	chatrespone: [],
	content: "",
	sessionid: "",
});
