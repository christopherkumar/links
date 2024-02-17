document.addEventListener('DOMContentLoaded', function() {
    const socialsContainer = document.getElementById('socials-container');
    const imgUrls = [
        "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
        "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
        "https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg"
    ];
    const links = [
        "https://www.linkedin.com/in/christopher-kumar-26b5792b1/",
        "https://github.com/christopherkumar",
        "https://www.instagram.com/christopherkumar812/"
    ];

    imgUrls.forEach(function(imgUrl, index) {
        const anchor = document.createElement('a');
        anchor.href = links[index];
        anchor.target = '_blank';
        const img = document.createElement('img');
        img.src = imgUrl;
        anchor.appendChild(img);
        socialsContainer.appendChild(anchor);
    });
});
