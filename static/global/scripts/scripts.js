function toggleReplyForm(commentId) {
    const form = document.getElementById(`reply-form-${commentId}`);
    form.style.display = (form.style.display === 'none') ? 'block' : 'none';
}

function toggleEditForm(commentId) {
    const form = document.getElementById(`comment-edit-form-${commentId}`);
    form.style.display = (form.style.display === 'none') ? 'block' : 'none';
}