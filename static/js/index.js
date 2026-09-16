const nickname = document.getElementById("nickname");
const password = document.getElementById("password");
const submit = document.getElementById("submit");

nickname.addEventListener('input', event => {
    event.preventDefault();
    if (event.target.value.trim().length > 0) {
        password.classList.remove("hide-element");
    } else {
        password.classList.add("hide-element");
        submit.classList.add("hide-element");
    }
});

password.addEventListener('input', event => {
    event.preventDefault();
    if (event.target.value.trim().length > 0) {
        submit.classList.remove("hide-element");
    } else {
        submit.classList.add("hide-element");
    }
});

nickname.addEventListener('keydown', event => {
    if (event.key === "Enter") {
        event.preventDefault();
        if (nickname.value.trim().length > 0) {
            password.classList.remove("hide-element");
            password.focus();
        }
    }
});

password.addEventListener('keydown', event => {
    if (event.key === "Enter") {
        event.preventDefault();
        if (nickname.value.trim().length > 0 && password.value.trim().length > 0) {
            submit.classList.remove("hide-element");
            submit.click();
        } else if (nickname.value.trim().length === 0) {
            nickname.focus();
        }
    }
});