function toggleForm(formId, parentId) {
    const form = document.getElementById(formId);
    const parentDiv = document.getElementById(parentId);
    const buttons = parentDiv.querySelectorAll('.reply-btn, .edit-btn, .delete-btn');

    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
        buttons.forEach(btn => btn.style.display = 'none');

        const textarea = form.querySelector('textarea');
        if (textarea) textarea.focus();

        function outsideClickListener(event) {
            if (!form.contains(event.target) && !Array.from(buttons).includes(event.target)) {
                form.style.display = 'none';
                buttons.forEach(btn => btn.style.display = 'inline-block');
                document.removeEventListener('click', outsideClickListener);
            }
        }

        setTimeout(() => {
            document.addEventListener('click', outsideClickListener);
        }, 0);
    } else {
        form.style.display = 'none';
        buttons.forEach(btn => btn.style.display = 'inline-block');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.message').forEach(msg => {
        setTimeout(() => msg.remove(), 4000);
    });
});