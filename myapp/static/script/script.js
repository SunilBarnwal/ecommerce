$('.carousel').carousel({
    interval: 2500
})



if (!window.location.pathname.endsWith("courses.html")) {

    const sections = document.querySelectorAll("section[id]");
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    window.addEventListener("scroll", () => {

        let current = "";

        // Page ke bottom par pahunchne par Contact Us active
        if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 50) {

            current = "z";

        } else {

            sections.forEach(section => {

                const sectionTop = section.offsetTop - 100;
                const sectionHeight = section.clientHeight;

                if (window.scrollY >= sectionTop &&
                    window.scrollY < sectionTop + sectionHeight) {

                    current = section.getAttribute("id");
                }

            });
        }

        navLinks.forEach(link => {

            link.parentElement.classList.remove("active");

            if (link.getAttribute("href") === "#" + current) {
                link.parentElement.classList.add("active");
            }

        });

    });

}








// const sections = document.querySelectorAll("section");
// const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

// window.addEventListener("scroll", () => {

//     let current = "";

//     sections.forEach(section => {
//         const sectionTop = section.offsetTop - 100;
//         const sectionHeight = section.clientHeight;

//         if (window.scrollY >= sectionTop &&
//             window.scrollY < sectionTop + sectionHeight) {
//             current = section.getAttribute("id");
//         }
//     });

//     navLinks.forEach(link => {
//         link.parentElement.classList.remove("active");

//         if (link.getAttribute("href") === "#" + current) {
//             link.parentElement.classList.add("active");
//         }
//     });

// });