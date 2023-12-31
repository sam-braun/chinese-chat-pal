document.getElementById("userMessage").addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

document.getElementById("userNote").addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        addNote();
    }
});

function sendMessage() {
    const userMessage = document.getElementById("userMessage").value;
    const chatbox = document.getElementById("chatbox");
    const showPinyin = document.getElementById("showPinyin").checked;
    const showSimplified = document.getElementById("showSimplified").checked;

    const currentTime = new Date().toLocaleTimeString();
    chatbox.innerHTML += `<p><strong>[${currentTime} - You]:</strong><br>${userMessage}</p>`;
    document.getElementById("userMessage").value = "";

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'user_message': userMessage,
            'show_pinyin': showPinyin,
            'show_simplified': showSimplified
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        
        const currentTime = new Date().toLocaleTimeString();
        let gptResponse = `<p><FONT COLOR="AD291F"><strong>[${currentTime} - GPT-3]:</strong>`;

        if (data.chinese) {
            gptResponse += ` <br><strong>中文: </strong>${data.chinese}`;
        }

        if (showPinyin && data.pinyin) {
            gptResponse += ` <br><strong>Pīnyīn: </strong>${data.pinyin}`;
        }

        gptResponse += `</p>`;
        chatbox.innerHTML += gptResponse;
    });
}

function addNote() {
    const userNote = document.getElementById("userNote").value;
    if(userNote) {
        const notesbox = document.getElementById("notesbox");
        const currentTime = new Date().toLocaleTimeString();
        notesbox.innerHTML += `<p><strong>[${currentTime}]:</strong> ${userNote}</p>`;
        document.getElementById("userNote").value = ""; // Clear the note box
    }
}

// modal
// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Get the start chatting button
var startChatting = document.getElementById("startChatting");

// When the page loads, open the modal 
window.onload = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks on "Start Chatting", close the modal
startChatting.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
