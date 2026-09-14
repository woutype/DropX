const nick = document.getElementById('nick');
const pass = document.getElementById('pass');
const submit = document.getElementById('submit');

nick.addEventListener('input', () => {
    if (nick.value.trim().length > 0) {
        pass.classList.remove('pass-hidden');
    } else {
        pass.classList.add('pass-hidden');
        pass.value = '';
        submit.classList.add('pass-hidden');
    }
});

nick.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        if (nick.value.trim().length > 0) {
            event.preventDefault();
            pass.classList.remove('pass-hidden');
            pass.focus();
        }
    }
});

pass.addEventListener('input', () => {
    if (pass.value.trim().length > 0) {
        submit.classList.remove('pass-hidden');
    } else {
        submit.classList.add('pass-hidden');
    }
});