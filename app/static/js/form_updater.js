function updateForm() {
    var otherPetField = document.getElementById('other_pet');
    var petField = document.getElementById('pet');
    otherPetField.style.display = petField.options[petField.selectedIndex].value === 'other' ? 'block' : 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    updateForm();
    document.getElementById('pet').onchange = updateForm;
});
