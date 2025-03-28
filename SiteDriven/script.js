// script.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("DriveOn site loaded successfully!");
    
    const navLinks = document.querySelectorAll(".nav-links a");
    
    navLinks.forEach(link => {
        link.addEventListener("mouseover", () => {
            link.style.color = "#6c63ff";
        });
        link.addEventListener("mouseout", () => {
            link.style.color = "#333";
        });
    });
    
    const signupButton = document.querySelector(".signup");
    signupButton.addEventListener("click", (event) => {
        event.preventDefault();
        alert("Signup functionality will be available soon!");
    });
});
