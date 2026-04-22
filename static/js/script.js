document.addEventListener('DOMContentLoaded', () => {
    const titleInput = document.getElementById('search-title');
    const speakerInput = document.getElementById('search-speaker');
    const categorySelect = document.getElementById('search-category');
    const talkCards = document.querySelectorAll('.talk-card');

    function filterTalks() {
        const titleQuery = titleInput.value.toLowerCase();
        const speakerQuery = speakerInput.value.toLowerCase();
        const categoryQuery = categorySelect.value;

        talkCards.forEach(card => {
            // Logic for lunch break visibility
            if (card.classList.contains('lunch-break')) {
                // Keep lunch break visible if no filters are applied
                if(titleQuery === '' && speakerQuery === '' && categoryQuery === '') {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
                return;
            }

            const title = card.getAttribute('data-title') || '';
            const speaker = card.getAttribute('data-speaker') || '';
            const category = card.getAttribute('data-category') || '';

            const matchesTitle = title.includes(titleQuery);
            const matchesSpeaker = speaker.includes(speakerQuery);
            const matchesCategory = categoryQuery === "" || category === categoryQuery;

            if (matchesTitle && matchesSpeaker && matchesCategory) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    titleInput.addEventListener('input', filterTalks);
    speakerInput.addEventListener('input', filterTalks);
    categorySelect.addEventListener('change', filterTalks);
});
