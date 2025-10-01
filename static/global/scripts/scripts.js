function toggleReplyForm(commentId) {
    const form = document.getElementById(`reply-form-${commentId}`);
    form.style.display = (form.style.display === 'none') ? 'block' : 'none';
}

function toggleEditForm(objectId) {
    const form = document.getElementById(`edit-form-${objectId}`);
    form.style.display = (form.style.display === 'none') ? 'block' : 'none';
}