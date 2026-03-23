/* ❄️ Snow Effect */
const snowContainer = document.querySelector(".snow");

function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.classList.add("snowflake");

    snowflake.innerHTML = "❄";

    snowflake.style.left = Math.random() * 100 + "vw";
    snowflake.style.fontSize = Math.random() * 10 + 10 + "px";

    const duration = Math.random() * 5 + 5;
    snowflake.style.animationDuration = duration + "s";

    snowContainer.appendChild(snowflake);

    setTimeout(() => {
        snowflake.remove();
    }, duration * 1000);
}

setInterval(createSnowflake, 100);

/* 🔍 Analyze Function */
function analyzeText() {
    const text = document.getElementById("inputText").value;

    if (!text) return alert("Enter text!");

    const result = document.getElementById("result");
    result.classList.remove("hidden");

    typeText("truth", "Truth: Analyzing...");
    typeText("deception", "Deception: Analyzing...");
    typeText("emotion", "Emotion: Analyzing...");

    setTimeout(() => {
        typeText("truth", "Truth: Medium");
        typeText("deception", "Deception: High");
        typeText("emotion", "Emotion: Neutral");
    }, 1500);
}

/* ⌨️ Typing Effect */
function typeText(id, text) {
    let i = 0;
    const element = document.getElementById(id);
    element.innerHTML = "";

    const interval = setInterval(() => {
        element.innerHTML += text.charAt(i);
        i++;
        if (i >= text.length) clearInterval(interval);
    }, 30);
}