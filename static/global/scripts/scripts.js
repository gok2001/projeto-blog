function toggleReplyForm(commentId) {
    const form = document.getElementById(`reply-form-${commentId}`);
    const commentDiv = document.getElementById(`comment-${commentId}`);
    const buttons = commentDiv.querySelectorAll('.reply-btn, .edit-btn, .delete-btn');

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

function toggleEditForm(objectId) {
    const form = document.getElementById(`edit-form-${objectId}`);
    const commentDiv = document.getElementById(`comment-${objectId}`);
    const buttons = commentDiv.querySelectorAll('.reply-btn, .edit-btn, .delete-btn')

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