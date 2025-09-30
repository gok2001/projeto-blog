const replyButtons = document.querySelectorAll('.reply-button')
const parentInput = document.querySelector('input[name="parentid"]')

replyButtons.forEach(button => {
    button.addEventListener('click', () => {
        parentInput.value = button.dataset.commentId;
        parentInput.scrollIntoView({ behavior: 'smooth' });
    });
});