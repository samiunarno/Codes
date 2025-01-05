const authors = [
        { name: "Fleur Hassan-Nahoum and Dorian Barak", title: "Co-Founders", country: "UAE", topic: "Business Council", photo: "PHOTO-2022-09-04-09-39-17" },
        { name: "Amb. Aviva Raz Shechter", title: "Ambassador", country: "Israel", topic: "Special Envoy for Women, Peace & Security", photo: "PHOTO-2022-02-09-22-30-28" },
        { name: "Amb. Houda Nonoo", title: "Former Ambassador", country: "Bahrain", topic: "Ambassador to the United States", photo: "Houda Nonoo image" },
        { name: "Amb. Amir Hayek", title: "Ambassador", country: "Israel", topic: "Israel’s Ministry of Foreign Affairs", photo: "PHOTO-2022-08-11-16-26-39" },
        { name: "Amb. Neil Wigan", title: "British Ambassador", country: "UK", topic: "Foreign and Commonwealth Office", photo: "s465_s960_Neil_Wigan_photo" },
        { name: "Aryeh Lightstone", title: "Special Envoy", country: "Israel", topic: "Economic Normalization", photo: "80aedf29-e90e-4048-8358-29584708b262" },
        { name: "Ariella Steinreich", title: "Senior Vice President", country: "USA", topic: "Steinreich Communications", photo: "Ariella Headshot New" },
        // More authors can be added here following the same structure...
    ];

    function displayAuthors(filteredAuthors) {
        const authorsList = document.getElementById("authors-list");
        authorsList.innerHTML = ""; // Clear the previous list
        filteredAuthors.forEach(author => {
            const authorCard = `
                <div class="card">
                    <img src="https://via.placeholder.com/100" alt="Photo of ${author.name}">
                    <h4>${author.name}</h4>
                    <p><strong>Title:</strong> ${author.title}</p>
                    <p><strong>Country:</strong> ${author.country}</p>
                    <p><strong>Topic:</strong> ${author.topic}</p>
                    <button>Read More</button>
                </div>
            `;
            authorsList.innerHTML += authorCard;
        });
    }

    function filterAuthors() {
        const nameFilter = document.getElementById('name-filter').value.toLowerCase();
        const titleFilter = document.getElementById('title-filter').value.toLowerCase();
        const countryFilter = document.getElementById('country-filter').value.toLowerCase();
        const topicFilter = document.getElementById('topic-filter').value.toLowerCase();

        const filteredAuthors = authors.filter(author => {
            return (
                (author.name.toLowerCase().includes(nameFilter) || nameFilter === "") &&
                (author.title.toLowerCase().includes(titleFilter) || titleFilter === "") &&
                (author.country.toLowerCase().includes(countryFilter) || countryFilter === "") &&
                (author.topic.toLowerCase().includes(topicFilter) || topicFilter === "")
            );
        });

        displayAuthors(filteredAuthors);
    }

    // Display all authors initially
    displayAuthors(authors);
