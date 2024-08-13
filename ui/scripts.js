document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('categorySelect');
    const titleSelect = document.getElementById('titleSelect');
    const valuesList = document.getElementById('valuesList');
    const addButton = document.getElementById('addButton');
    
    const modifierName = document.getElementById('modifierName');
    const modifierDropdown = document.getElementById('modifierDropdown');
    const modifierValue = document.getElementById('modifierValue');
    const addModifierButton = document.getElementById('addModifierButton');
    
    const dialogPurposeInput = document.getElementById('dialogPurposeInput');
    const addDialogPurposeButton = document.getElementById('addDialogPurposeButton');

    const jsonEditor = document.getElementById('jsonEditor');
    const generateDialogButton = document.getElementById('generateDialogButton');
    const useMockButton = document.getElementById('useMockButton'); // New button
    const responseOutput = document.getElementById('responseOutput');

    const mockJsonObject = {
        "relevent_lore": {
          "Locations": {
            "Lucky 38": [
              "Background"
            ]
          },
          "Characters": {
            "Benny": [
              "Background"
            ]
          }
        },
        "npc_modifiers": {
          "main_dialog_purpose": "NPC who doesn't like Benny and wants to see him gone by any means",
          "role": "person living on the strip",
          "goal": "seeking someone to take out Benny",
          "personality": "upbeat",
          "conversation_context": "Person talking to themselves about how they want Benny taken out"
        }
      }
    let jsonObject = {
        "relevent_lore": {},
        "npc_modifiers": {}
    };

    // Populate the category dropdown dynamically based on master_tags keys
    function populateCategoryDropdown(selectElement) {
        selectElement.innerHTML = '<option value="">Select Category</option>';
        const categories = Object.keys(master_tags);
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            selectElement.appendChild(option);
        });
    }

    // Populate the modifier dropdown dynamically based on npc_modifiers_examples keys
    function populateModifierDropdown(selectElement) {
        selectElement.innerHTML = '<option value="">Select Modifier</option>';
        const modifiers = Object.keys(npc_modifiers_examples);
        modifiers.forEach(modifier => {
            const option = document.createElement('option');
            option.value = modifier;
            option.textContent = modifier;
            selectElement.appendChild(option);
        });
    }

    // Call the functions to populate the dropdowns on page load
    populateCategoryDropdown(categorySelect);
    populateModifierDropdown(modifierDropdown);

    function handleCategoryChange(categorySelect, titleSelect, valuesList, addButton) {
        const category = categorySelect.value;
        titleSelect.innerHTML = '<option value="">Select Title</option>';
        valuesList.innerHTML = '';
        addButton.disabled = true;

        if (category) {
            // Fetch titles dynamically based on the selected category from master_tags
            const titles = Object.keys(master_tags[category]);
            titles.forEach(title => {
                const option = document.createElement('option');
                option.value = title;
                option.textContent = title;
                titleSelect.appendChild(option);
            });
            titleSelect.disabled = false;
        } else {
            titleSelect.disabled = true;
        }
    }

    categorySelect.addEventListener('change', function () {
        handleCategoryChange(categorySelect, titleSelect, valuesList, addButton);
    });

    titleSelect.addEventListener('change', function () {
        const title = titleSelect.value;
        valuesList.innerHTML = '';
        addButton.disabled = true;

        if (title) {
            // Fetch values dynamically based on the selected title
            const values = master_tags[categorySelect.value][title];
            values.forEach(value => {
                const formCheckDiv = document.createElement('div');
                formCheckDiv.className = 'form-check';

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.value = value;
                checkbox.className = 'form-check-input';

                const label = document.createElement('label');
                label.className = 'form-check-label';
                label.appendChild(checkbox);
                label.appendChild(document.createTextNode(value));

                formCheckDiv.appendChild(label);
                valuesList.appendChild(formCheckDiv);
            });
            addButton.disabled = false;
        }
    });

    modifierDropdown.addEventListener('change', function () {
        const selectedModifier = modifierDropdown.value;
        if (selectedModifier) {
            modifierName.value = selectedModifier;
            modifierValue.placeholder = npc_modifiers_examples[selectedModifier];
        } else {
            modifierName.value = '';
            modifierValue.placeholder = 'Value';
        }
    });

    addButton.addEventListener('click', function () {
        const category = categorySelect.value;
        const title = titleSelect.value;
        const selectedValues = Array.from(valuesList.querySelectorAll('input:checked')).map(checkbox => checkbox.value);

        if (!jsonObject.relevent_lore[category]) {
            jsonObject.relevent_lore[category] = {};
        }
        jsonObject.relevent_lore[category][title] = selectedValues;

        jsonEditor.value = JSON.stringify(jsonObject, null, 2);

        // Reset the form
        categorySelect.value = '';
        titleSelect.innerHTML = '<option value="">Select Title</option>';
        titleSelect.disabled = true;
        valuesList.innerHTML = '';
        addButton.disabled = true;
    });

    addModifierButton.addEventListener('click', function () {
        const name = modifierName.value.trim();
        const value = modifierValue.value.trim();

        if (name && value) {
            jsonObject.npc_modifiers[name] = value;

            jsonEditor.value = JSON.stringify(jsonObject, null, 2);

            // Reset the form
            modifierName.value = '';
            modifierDropdown.value = '';
            modifierValue.value = '';
            modifierValue.placeholder = 'Value';
        }
    });

    addDialogPurposeButton.addEventListener('click', function () {
        const dialogPurpose = dialogPurposeInput.value.trim();

        if (dialogPurpose) {
            jsonObject.npc_modifiers['main_dialog_purpose'] = dialogPurpose;

            jsonEditor.value = JSON.stringify(jsonObject, null, 2);

            // Reset the form
            dialogPurposeInput.value = '';
        }
    });

    generateDialogButton.addEventListener('click', function () {
        // Update the jsonObject with the latest value from the jsonEditor
        try {
            jsonObject = JSON.parse(jsonEditor.value);
        } catch (e) {
            alert('Invalid JSON format in the editor');
            return;
        }

        // Call the API function to generate dialog
        generateDialog(jsonObject);
    });

    useMockButton.addEventListener('click', function () {
        // Update the jsonObject with mockJsonObject
        jsonObject = mockJsonObject;
        jsonEditor.value = JSON.stringify(jsonObject, null, 2);
    });

    function generateDialog(jsonObject) {
        console.log('making a request:', jsonObject);
        fetch('http://localhost:8080/npc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonObject)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the response as JSON
        })
        .then(data => {
            console.log(data); // Log the entire data to inspect its structure
            if (data.response) {
                document.getElementById('responseOutput').textContent = data.response;
            } else {
                document.getElementById('responseOutput').textContent = 'Response results will be displayed here...';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('responseOutput').textContent = 'An error occurred. Try again.';
        });
    }
    
});
